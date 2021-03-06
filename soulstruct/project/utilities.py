from functools import wraps

from soulstruct.ai import DarkSoulsAIScripts
from soulstruct.core import SoulstructError
from soulstruct.maps import DarkSoulsMaps
from soulstruct.params import DarkSoulsGameParameters, DarkSoulsLightingParameters
from soulstruct.text import DarkSoulsText
from soulstruct.utilities import word_wrap

__all__ = ["SoulstructProjectError", "RestoreBackupError", "error_as_dialog",
           "ActionHistory", "ViewHistory", "bind_events", "data_type_caps", "DATA_TYPES"]


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
