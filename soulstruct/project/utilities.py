from functools import wraps

from soulstruct.ai import DarkSoulsAIScripts
from soulstruct.core import SoulstructError
from soulstruct.maps import DarkSoulsMaps
from soulstruct.params import DarkSoulsGameParameters, DarkSoulsLightingParameters
from soulstruct.text import DarkSoulsText
from soulstruct.utilities import word_wrap

__all__ = ["SoulstructProjectError", "RestoreBackupError", "error_as_dialog",
           "ActionHistory", "ViewHistory", "bind_events", "data_type_caps", "DATA_TYPES"]

from soulstruct.utilities.window import SmartFrame


class SoulstructProjectError(SoulstructError):
    pass


class RestoreBackupError(SoulstructError):
    pass


def bind_events(widget, bindings: dict):
    for event, func in bindings.items():
        widget.bind(event, func)


def error_as_dialog(window, func):
    @wraps(func)
    def window_method(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except SoulstructProjectError as e:
            window.CustomDialog(
                title="Runtime Manager Error",
                message=word_wrap(str(e), 50),
            )
        except Exception as e:
            window.CustomDialog(
                title="Unknown Internal Error",
                message="Internal Error:\n\n" + word_wrap(str(e), 50) + "\n\nPlease report this error.",
            )

    return window_method


class ViewHistory(object):
    """Global window timeline of selected tab, category, entry, and (if applicable) field.

    Note that view changes that are caused by undo and redo functions are not treated differently here.
    """
    def __init__(self):
        self._back_stack = []
        self._forward_stack = []

    def record_view_change(self, back, forward):
        if not callable(back) or not callable(forward):
            raise TypeError("Back and forward view-changing functions must be callable and have no arguments.")
        self._back_stack.append((back, forward))
        self._forward_stack = []  # old future timeline dies

    def back(self, _=None):
        if self._back_stack:
            back, forward = self._back_stack.pop()
            back(from_history=True)
            self._forward_stack.append((back, forward))
            return True
        else:
            return False

    def forward(self, _=None):
        if self._forward_stack:
            back, forward = self._forward_stack.pop()
            forward(from_history=True)
            self._back_stack.append((back, forward))
            return True
        else:
            return False


class ActionHistory(object):
    """Each tab maintains a separate ActionHistory timeline of action/inverse-action data-modifying pairs for undo and
    redo."""
    def __init__(self):
        self._undo_stack = []
        self._redo_stack = []

    def record_action(self, undo, redo):
        """Record the undo and redo callbacks (no arguments) for an action."""
        if not callable(undo) or not callable(redo):
            raise TypeError("Action and inverse action functions must be callable and have no arguments.")
        self._undo_stack.append((undo, redo))
        self._redo_stack = []  # old future timeline dies

    def undo(self, _=None):
        if self._undo_stack:
            undo, redo = self._undo_stack.pop()
            undo(from_history=True)
            self._redo_stack.append((undo, redo))
            return True
        else:
            return False

    def redo(self, _=None):
        if self._redo_stack:
            undo, redo = self._redo_stack.pop()
            redo(from_history=True)
            self._undo_stack.append((undo, redo))
            return True
        else:
            return False


def data_type_caps(data_type):
    if data_type.lower() == "ai":
        return "AI"
    return data_type.capitalize()


DATA_TYPES = {
    'maps': DarkSoulsMaps,
    'params': DarkSoulsGameParameters,
    'lighting': DarkSoulsLightingParameters,
    'text': DarkSoulsText,
    'events': None,  # modified via EVS event script files
    'ai': DarkSoulsAIScripts,
    'talk': None,  # modified via ESP state machine script files
}


class TextEditBox(SmartFrame):
    """Small pop-out widget that allows you to modify longer strings more freely, with newlines and all."""
    WIDTH = 16  # characters
    HEIGHT = 1  # lines

    def __init__(self, master, initial_text='', allow_newlines=True, window_title="Editing Text"):
        super().__init__(toplevel=True, master=master, window_title=window_title)
        self.master = master
        self.initial_text = initial_text
        self.output = None
        self.allow_newlines = allow_newlines

        self._text = None

        self.build()

    def build(self):
        with self.set_master(auto_rows=0):
            self._text = self.TextBox(padx=20, pady=20, width=self.WIDTH, height=self.HEIGHT)
            self._text.insert('end', self.initial_text)
            with self.set_master(auto_columns=0, padx=10, pady=10, grid_defaults={'padx': 10}):
                self.Button(
                    text="Confirm changes", command=lambda: self.done(True), **self.master.DEFAULT_BUTTON_KWARGS['YES'])
                self.Button(
                    text="Cancel changes", command=lambda: self.done(False), **self.master.DEFAULT_BUTTON_KWARGS['NO'])

        self.bind_all('<Escape>', lambda e: self.done(False))
        self.protocol('WM_DELETE_WINDOW', lambda: self.done(False))
        self.resizable(width=False, height=False)
        self.set_geometry(relative_position=(0.5, 0.3), transient=True)

    def go(self):
        self.wait_visibility()
        self.grab_set()
        self.mainloop()
        self.destroy()
        return self.output

    def done(self, confirm=True):
        if confirm:
            new_text = self._text.get('1.0', 'end' + '-1c')
            if not self.allow_newlines and '\n' in new_text:
                self.editor.CustomDialog("Text Error", "Entry cannot contain newlines.")
                return
            if new_text == self.initial_text:
                self.output = None
            else:
                self.output = self._text.get('1.0', 'end' + '-1c')
        self.quit()


class NameSelectionBox(SmartFrame):
    """Small pop-out widget that allows you to select a name from some list."""
    WIDTH = 50  # characters
    HEIGHT = 20  # lines

    def __init__(self, master, names, list_name='List'):
        super().__init__(toplevel=True, master=master, window_title=f"Select Entry from {list_name}")

        self.output = None

        with self.set_master(padx=20, pady=20):
            self._names = self.Listbox(
                values=names, width=self.WIDTH, height=self.HEIGHT, vertical_scrollbar=True, selectmode='single',
                font=("Consolas", 14), padx=20, pady=20)

        self._names.bind('<Double-Button-1>', lambda e: self.done(True))

        self.bind_all('<Escape>', lambda e: self.done(False))
        self.protocol('WM_DELETE_WINDOW', lambda: self.done(False))
        self.resizable(width=False, height=False)
        self.set_geometry(relative_position=(0.5, 0.3), transient=True)

    def go(self):
        self.wait_visibility()
        self.grab_set()
        self.mainloop()
        self.destroy()
        return self.output

    def done(self, confirm=True):
        if confirm:
            self.output = self._names.get(self._names.curselection())
        self.quit()