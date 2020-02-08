from __future__ import annotations

import typing as tp
from functools import partial

from soulstruct.project.utilities import bind_events, TextEditBox
from soulstruct.utilities import camel_case_to_spaces
from soulstruct.utilities.window import SmartFrame, ToolTip

if tp.TYPE_CHECKING:
    from .core import BaseDataTab


class EntryRow(SmartFrame):
    """Container/manager for widgets of a single entry row."""
    ENTRY_ANCHOR = 'center'
    ENTRY_ROW_HEIGHT = 30
    SHOW_ENTRY_ID = True
    EDIT_ENTRY_ID = True
    ENTRY_ID_WIDTH = 15
    ENTRY_ID_FG = '#CDF'
    ENTRY_TEXT_WIDTH = 150
    ENTRY_TEXT_FG = '#FFF'

    def __init__(self, master: BaseEntryFrame, row_index: int, bindings: dict, context_menu_commands: dict):
        self.STYLE_DEFAULTS = master.STYLE_DEFAULTS
        super().__init__(master=master, toplevel=False)

        self.row_index = row_index
        self._entry_id = None
        self._entry_text = None
        self._active = False

        bg_color = self._get_color()

        self.row_box = master.Frame(
            width=self.ENTRY_ID_WIDTH + self.ENTRY_TEXT_WIDTH, height=self.ENTRY_ROW_HEIGHT, bg=bg_color,
            row=row_index, columnspan=2 if self.SHOW_ENTRY_ID else 1, sticky='nsew')
        bind_events(self.row_box, bindings["text"])

        if self.SHOW_ENTRY_ID:
            self.id_box = master.Frame(row=row_index, column=0, bg=bg_color, sticky='ew')
            self.id_label = master.Label(
                self.id_box, text='', width=self.ENTRY_ID_WIDTH, bg=bg_color, fg=self.ENTRY_ID_FG, font_size=11,
                sticky='e')
            if self.EDIT_ENTRY_ID:
                bind_events(self.id_box, bindings["id"])
                bind_events(self.id_label, bindings["id"])
            else:
                bind_events(self.id_box, bindings["text"])
                bind_events(self.id_label, bindings["text"])
        else:
            self.id_label = None

        self.text_box = master.Frame(row=row_index, column=1 if self.SHOW_ENTRY_ID else 0, bg=bg_color, sticky='ew')
        bind_events(self.text_box, bindings["text"])

        self.text_label = master.Label(
            self.text_box, text='', bg=bg_color, fg=self.ENTRY_TEXT_FG, anchor='w', font_size=11,
            justify='left', width=self.ENTRY_TEXT_WIDTH)
        bind_events(self.text_label, bindings["text"])

        self.context_menu = master.Menu(self.row_box)
        self.context_menu_commands = context_menu_commands
        self.build_entry_context_menu()

        self.tool_tip = ToolTip(
            self.row_box, self.id_box, self.id_label, self.text_box, self.text_label, text=None, wraplength=350)

    def update_entry(self, entry_id: int, entry_text: str):
        self.entry_id = entry_id
        self.entry_text = entry_text
        self._update_colors()

    def hide(self):
        """Called when this row has no entry to display."""
        self.row_box.grid_remove()
        if self.SHOW_ENTRY_ID:
            self.id_box.grid_remove()
            self.id_label.grid_remove()
        self.text_box.grid_remove()
        self.text_label.grid_remove()

    def unhide(self):
        self.row_box.grid()
        if self.SHOW_ENTRY_ID:
            self.id_box.grid()
            self.id_label.grid()
        self.text_box.grid()
        self.text_label.grid()

    def build_entry_context_menu(self):
        self.context_menu.delete(0, 'end')
        self.context_menu.add_command(
            label="Edit Entry Text in Floating Box (Shift + Click)", foreground=self.STYLE_DEFAULTS['text_fg'],
            command=self._popout_entry_text_edit)
        self.context_menu.add_command(
            label="Duplicate Entry to Next ID", foreground=self.STYLE_DEFAULTS['text_fg'],
            command=self._add_relative_entry)
        self.context_menu.add_command(
            label="Delete Entry", foreground=self.STYLE_DEFAULTS['text_fg'],
            command=self._delete_entry)

    def _popout_entry_text_edit(self):
        return self.context_menu_commands["popout_entry_text_edit"](self.row_index)

    def _add_relative_entry(self):
        return self.context_menu_commands["add_relative_entry"](self.entry_id, offset=1)

    def _delete_entry(self):
        return self.context_menu_commands["delete_entry"](self.row_index)

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value: bool):
        if not self._active and value:
            self._active = True
        elif self._active and not value:
            self._active = False
        else:
            return  # No change to active state.

        self._update_colors()

    @property
    def entry_id(self):
        return self._entry_id

    @entry_id.setter
    def entry_id(self, value):
        self._entry_id = value
        if self.SHOW_ENTRY_ID:
            self.id_label.var.set(str(self._entry_id))

    @property
    def entry_text(self):
        return self._entry_text

    @entry_text.setter
    def entry_text(self, value):
        self._entry_text = value
        self.text_label.var.set(self._entry_text)

    def _update_colors(self):
        bg_color = self._get_color()
        for widget in (self.row_box, self.id_box, self.id_label, self.text_box, self.text_label):
            widget['bg'] = bg_color

    def _get_color(self):
        """Inspects entry text/state and assembles a tuple of 'bg' color values."""
        base_bg = int(self.STYLE_DEFAULTS['bg'].lstrip('#'))  # dark grey
        if self._entry_text is not None:
            if not self._entry_text:
                base_bg += 200  # entry text is empty (red)
            elif not self._entry_text.strip():
                base_bg += 110  # entry text contains only space (yellow)
        if self._active:
            base_bg += 123  # turquoise boost
        if self.row_index % 2:
            base_bg += 111  # every second row is slightly brighter
        return f'#{base_bg}'


class BaseEntryFrame(SmartFrame):
    ENTRY_CANVAS_BG = '#1d1d1d'
    ENTRY_BOX_WIDTH = 800
    ENTRY_BOX_HEIGHT = 400
    ENTRY_RANGE_SIZE = 50

    def __init__(self, master: BaseDataTab):
        super().__init__(master=master, toplevel=False)
        self.MASTER = master
        self.entry_rows = []  # type: tp.List[EntryRow]
        self.active_row_index = None  # deselected
        self.first_display_index = 0
        self.displayed_entry_count = 0

        self.entry_canvas = None
        self.entry_i_frame = None
        self.previous_range_button = None
        self.next_range_button = None
        self._e_entry_text_edit = None
        self._e_entry_id_edit = None

    def build(self):
        with self.set_master(sticky='nsew', row_weights=[0, 1, 0], column_weights=[1], auto_rows=0):
            self.build_previous_range_button()
            with self.set_master(sticky='nsew', row_weights=[1], column_weights=[1]):
                self.build_entry_canvas()
            self.build_next_range_button()

    def build_previous_range_button(self, **kwargs):
        self.previous_range_button = self.Button(
            text=f"Previous {self.ENTRY_RANGE_SIZE}", font_size=10, bg='#111', width=30,
            command=self._go_to_previous_entry_range, padx=10, pady=10, **kwargs)

    def build_next_range_button(self, **kwargs):
        self.next_range_button = self.Button(
            text=f"Next {self.ENTRY_RANGE_SIZE}", font_size=10, bg='#111', width=30,
            command=self._go_to_next_entry_range, padx=10, pady=10, **kwargs)

    def build_entry_canvas(self):
        """Master should already be set."""
        self.entry_canvas = self.Canvas(
            width=self.ENTRY_BOX_WIDTH, height=self.ENTRY_BOX_HEIGHT, borderwidth=0,
            vertical_scrollbar=True, horizontal_scrollbar=True, sticky='nsew',
            highlightthickness=0, yscrollincrement=EntryRow.ENTRY_ROW_HEIGHT, bg=self.ENTRY_CANVAS_BG,
            row_weights=[1], column_weights=[1])
        self.entry_i_frame = self.Frame(frame=self.entry_canvas, sticky='ew', column_weights=[1, 1])
        self.entry_i_frame.bind("<Configure>", lambda e, c=self.entry_canvas: self.reset_canvas_scroll_region(c))
        self.entry_canvas.create_window(0, 0, window=self.entry_i_frame, anchor='nw')

        with self.set_master(self.entry_i_frame):
            for row in range(self.ENTRY_RANGE_SIZE):

                bindings = {
                    "text": {
                        '<Button-1>': lambda _, i=row: self.select_entry_row_index(i),
                        '<Shift-Button-1>': lambda e, i=row: self.popout_entry_text_edit(i),
                        '<Button-3>': lambda e, i=row: self._right_click_entry(e, i),
                        '<Up>': self._entry_press_up,
                        '<Down>': self._entry_press_down,
                        '<Prior>': lambda e: self._go_to_previous_entry_range(),
                        '<Next>': lambda e: self._go_to_next_entry_range(),
                    }
                }
                bindings["id"] = bindings["text"].copy()
                bindings["id"]['<Button-1>'] = lambda _, i=row: self.select_entry_row_index(i, id_clicked=True)
                bindings["id"]['<Shift-Button-1>'] = lambda _, i=row: self.popout_entry_id_edit(i)

                context_menu_commands = {
                    "popout_entry_id_edit": self.popout_entry_id_edit,
                    "add_relative_entry": self.add_relative_entry,
                    "delete_entry": self.delete_entry,
                }

                self.entry_rows.append(EntryRow(
                    self, row_index=row, bindings=bindings, context_menu_commands=context_menu_commands))

    def get_entry_id(self, row_index: int = None) -> tp.Optional[int]:
        """Retrieves true entry ID from the displayed row index (which is relative to `.first_display_index`).
        Row index defaults to active row index.
        """
        if row_index is None:
            row_index = self.active_row_index
            if row_index is None:
                return None
        return self.entry_rows[row_index].entry_id

    @property
    def active_entry_id(self):
        return self.entry_rows[self.active_row_index].entry_id

    def select_entry_id(self, entry_id, set_focus_to_text=True, edit_if_already_selected=True, as_row_index=None):
        """Select entry based on ID and set the category display range to a value such that the selected entry has
        row index `as_row_index` (or as close as possible).

        Optionally sets window focus to text (default True) and edits text if it's already selected (default True).

        Never counts as a view change (more primitive method `select_entry_row_index` can, though).
        """
        if as_row_index is None:
            # Default value is 5 if no newlines are in the target entry and 1 if there are.
            as_row_index = 1 if '\n' in self.get_entry_name(entry_id) else 5

        entry_index = self.get_entry_index(entry_id)
        row_index = self._update_first_entry_display_index(entry_index, as_row_index=as_row_index)
        self.refresh_entries()
        self.entry_canvas.yview_moveto(0)
        self.select_entry_row_index(
            row_index, set_focus_to_text=set_focus_to_text, edit_if_already_selected=edit_if_already_selected)

    def select_entry_row_index(self, row_index, set_focus_to_text=True, edit_if_already_selected=True,
                               id_clicked=False, view_change=False):
        """Select entry from row index, based on currently displayed category and ID range.

        Optionally counts as a view change (default False).
        """
        old_row_index = self.active_row_index

        if old_row_index is not None and row_index is not None:
            if row_index == old_row_index:
                if edit_if_already_selected:
                    if id_clicked:
                        return self._start_entry_id_edit(row_index)
                    else:
                        return self._start_entry_text_edit(row_index)
                return
        else:
            self._cancel_entry_id_edit()
            self._cancel_entry_text_edit()

        self.active_row_index = row_index

        if old_row_index is not None:
            self.entry_rows[old_row_index].active = False
        if row_index is not None:
            self.entry_rows[row_index].active = True
            if set_focus_to_text:
                self.entry_rows[row_index].text_label.focus_set()

        if view_change and old_row_index is not None:
            # View history operates on entry ID rather than row index.
            self.master.view_history.record_view_change(
                back=lambda: self.select_entry_id(self.get_entry_id(old_row_index), edit_if_already_selected=False),
                forward=lambda: self.select_entry_id(self.get_entry_id(row_index), edit_if_already_selected=False),
            )

        if self.MASTER.refresh_fields():
            # TODO: does it only steal focus because I'm telling it to?
            # `refresh_fields()` seems to steal focus aggressively, so end by setting it back to entry name.
            if row_index is not None and set_focus_to_text:
                self.entry_rows[row_index].text_label.focus_set()

    def refresh_entries(self):
        """Refresh entry display. Doesn't affect selected entry row (unless no entries are displayed, in which case
        all rows are deselected)."""
        self._cancel_entry_id_edit()
        self._cancel_entry_text_edit()

        entry_id_range = self.MASTER.get_entry_id_range(
            first_index=self.first_display_index,
            last_index=self.first_display_index + self.ENTRY_RANGE_SIZE,
        )

        row = 0
        for entry_id in entry_id_range:
            self.entry_rows[row].update_entry(entry_id, self.get_entry_name(entry_id))
            self.entry_rows[row].unhide()
            row += 1

        self.displayed_entry_count = row
        for remaining_row in range(row, self.ENTRY_RANGE_SIZE):
            self.entry_rows[remaining_row].hide()

        if self.displayed_entry_count == 0:
            self.select_entry_row_index(None)
        self._refresh_range_buttons(entry_count=len(self.MASTER.get_category_data()))

    def change_entry_id(self, row_index, new_entry_id, category=None, record_action=True):
        """Set ID of given entry row index in the displayed category (if different from current).

        Optionally recorded as an action (default True).
        """
        if category is None:
            category = self.MASTER.active_category
        old_entry_id = self.get_entry_id(row_index)
        if old_entry_id == new_entry_id:
            return  # No change.
        if new_entry_id in self.MASTER.get_category_data():
            self.CustomDialog(
                title="Entry ID Clash",
                message=f"Entry ID {new_entry_id} already exists in {self.MASTER.DATA_NAME}.{category}. You must "
                        f"change or delete it first.")
            return

        if not self._set_entry_id(old_entry_id, new_entry_id, category, update_row_index=row_index):
            return

        if record_action:
            self.MASTER.action_history.record_action(
                    undo=partial(self._set_entry_id,
                                 entry_id=new_entry_id, new_id=old_entry_id, category=category),
                    redo=partial(self._set_entry_id,
                                 entry_id=old_entry_id, new_id=new_entry_id, category=category),
                )
        else:
            self.MASTER.jump_to_entry(category, new_entry_id)

    def change_entry_text(self, row_index, new_text, category=None, record_action=True):
        """Set text of given entry index in the displayed category (if different from current).

        Optionally recorded as an action (default True).
        """
        if category is None:
            category = self.MASTER.active_category
        entry_id = self.get_entry_id(row_index)
        old_text = self.get_entry_name(entry_id, category=category)
        if old_text == new_text:
            return  # Nothing to change.

        if not self._set_entry_name(entry_id, new_text, category=category, update_row_index=row_index):
            return

        if record_action:
            self.MASTER.action_history.record_action(
                    undo=partial(self._set_entry_name,
                                 entry_id=entry_id, new_text=new_text, category=category),
                    redo=partial(self._set_entry_name,
                                 entry_id=entry_id, new_text=old_text, category=category),
                )
        else:
            self.MASTER.jump_to_entry(category, entry_id)

    def popout_entry_id_edit(self, row_index):
        entry_id = self.get_entry_id(row_index)
        if not self._e_entry_text_edit and not self._e_entry_id_edit:
            initial_text = str(entry_id)
            popout_editor = TextEditBox(self, initial_text, allow_newlines=False, window_title="Editing Entry ID")
            new_text = popout_editor.go()
            if new_text is not None:
                try:
                    new_id = int(new_text)
                    if new_id < 0:
                        raise ValueError
                except ValueError:
                    self.CustomDialog("Invalid Entry ID", "Entry ID must be a non-negative integer.")
                    return
                self.change_entry_id(row_index, new_id)

    def popout_entry_text_edit(self, row_index):
        entry_id = self.get_entry_id(row_index)
        if not self._e_entry_text_edit and not self._e_entry_id_edit:
            initial_text = self.get_entry_name(entry_id)
            popout_editor = EntryNameEditBox(self.MASTER, self.MASTER.active_category, entry_id, initial_text)
            _, new_text = popout_editor.go()
            if new_text is not None:
                self.change_entry_text(row_index, new_text)

    def _add_entry(self, entry_id, text, category=None, entry_data=None):
        if category is None:
            category = self.MASTER.active_category
            if category is None:
                raise ValueError("Cannot add entry without specifying category if 'active_category' is None.")
        if entry_id < 0:
            self.CustomDialog("Entry ID Error", message=f"Entry ID cannot be negative.")
            return
        if entry_id in self.MASTER.get_category_data():
            self.CustomDialog(
                title="Entry ID Error",
                message=f"Entry ID {entry_id} already exists in category "
                        f"{camel_case_to_spaces(self.MASTER.active_category)}.")
            return

        self._cancel_entry_id_edit()
        self._cancel_entry_text_edit()
        self._set_entry_name(entry_id, text)

        if entry_data is not None:
            self.MASTER.set_entry_data(entry_id, entry_data, category)

        self.select_entry_id(entry_id, set_focus_to_text=True, edit_if_already_selected=False)

        # TODO: Action/view history.

    def add_relative_entry(self, entry_id, offset=1, text=None, copy_entry_data=False):
        if text is None:
            text = self.get_entry_name(entry_id)  # Copies name of origin entry by default.
        entry_data = self.MASTER.get_entry_data(entry_id).copy() if copy_entry_data else None
        self._add_entry(entry_id=entry_id + offset, text=text, entry_data=entry_data)

    def delete_entry(self, row_index, category=None):
        """Deletes entry and returns it (or False upon failure) so that the action manager can undo the deletion."""
        self._cancel_entry_id_edit()
        self._cancel_entry_text_edit()
        entry_id = self.get_entry_id(row_index)
        # TODO: define `delete_entry()` for each data structure to avoid subclassing
        deleted_entry = self.MASTER.get_category_data(category=category).pop(entry_id)
        self.refresh_entries()

        # TODO: Action/view history.

        return deleted_entry  # TODO: or return False?

    def _update_first_entry_display_index(self, new_entry_index, as_row_index=0):
        """Updates first display index so that 'new_entry_index' becomes displayed index 'as_row_index' (or as close
        to it as possible, for very early entries).

        Returns the resulting displayed row index of new_entry_index (for after '.refresh_entries()' is called).
        """
        self.first_display_index = max(0, new_entry_index - as_row_index)
        return new_entry_index - self.first_display_index

    def _right_click_entry(self, event, entry_index):
        self.select_entry_row_index(entry_index, edit_if_already_selected=False)
        self.entry_rows[entry_index].context_menu.tk_popup(event.x_root, event.y_root)

    def _update_range(self, first_index):
        delta = first_index - self.first_display_index
        self.first_display_index = first_index
        self.refresh_entries()
        self.select_entry_row_index(0, edit_if_already_selected=False)
        self.update_idletasks()
        self.entry_canvas.yview_moveto(0)
        return delta

    def _go_to_previous_entry_range(self):
        first_index = max(self.first_display_index - self.ENTRY_RANGE_SIZE, 0)
        if first_index == self.first_display_index:
            return
        return self._update_range(first_index)

    def _go_to_next_entry_range(self):
        entry_count = len(self.MASTER.get_category_data())
        first_index = min(self.first_display_index + self.ENTRY_RANGE_SIZE, max(entry_count - self.ENTRY_RANGE_SIZE, 0))
        if first_index == self.first_display_index:
            return
        return self._update_range(first_index)

    def _start_entry_id_edit(self, row_index):
        if not self._e_entry_text_edit and not self._e_entry_id_edit:
            entry_id = self.get_entry_id(row_index)
            initial_text = str(entry_id)
            self._e_entry_id_edit = self.Entry(
                self.entry_rows[row_index].id_box, initial_text=initial_text,
                integers_only=True, sticky='ew', width=int(EntryRow.ENTRY_ID_WIDTH * 0.5))
            self._e_entry_id_edit.bind('<Return>', lambda e, i=row_index: self._confirm_entry_id_edit(i))
            self._e_entry_id_edit.bind('<Up>', self._entry_press_up)
            self._e_entry_id_edit.bind('<Down>', self._entry_press_down)
            self._e_entry_id_edit.bind('<FocusOut>', lambda e: self._cancel_entry_id_edit())
            self._e_entry_id_edit.bind('<Escape>', lambda e: self._cancel_entry_id_edit())
            self._e_entry_id_edit.focus_set()
            self._e_entry_id_edit.select_range(0, 'end')

    def _cancel_entry_id_edit(self):
        if self._e_entry_id_edit:
            self._e_entry_id_edit.destroy()
            self._e_entry_id_edit = None

    def _confirm_entry_id_edit(self, row_index):
        if self._e_entry_id_edit:
            try:
                new_id = int(self._e_entry_id_edit.var.get())
            except ValueError:
                if self._e_entry_id_edit.var.get() != "-":
                    raise
            else:
                self.change_entry_id(row_index, new_id)
            self._cancel_entry_id_edit()

    def _start_entry_text_edit(self, row_index):
        if not self._e_entry_text_edit and not self._e_entry_id_edit:
            entry_id = self.get_entry_id(row_index)
            initial_text = self.get_entry_name(entry_id)
            if '\n' in initial_text:
                return self.popout_entry_text_edit(row_index)
            self._e_entry_text_edit = self.Entry(
                self.entry_rows[row_index].text_box, initial_text=initial_text, sticky='ew',
                width=5)
            self._e_entry_text_edit.bind('<Return>', lambda e, i=row_index: self._confirm_entry_text_edit(i))
            self._e_entry_text_edit.bind('<Up>', self._entry_press_up)
            self._e_entry_text_edit.bind('<Down>', self._entry_press_down)
            self._e_entry_text_edit.bind('<FocusOut>', lambda e: self._cancel_entry_text_edit())
            self._e_entry_text_edit.bind('<Escape>', lambda e: self._cancel_entry_text_edit())
            self._e_entry_text_edit.focus_set()
            self._e_entry_text_edit.select_range(0, 'end')

    def _cancel_entry_text_edit(self):
        if self._e_entry_text_edit:
            self._e_entry_text_edit.destroy()
            self._e_entry_text_edit = None

    def _confirm_entry_text_edit(self, row_index):
        if self._e_entry_text_edit:
            new_text = self._e_entry_text_edit.var.get()
            self.change_entry_text(row_index, new_text)
            self._cancel_entry_text_edit()

    def _shift_selected_entry(self, relative_index):
        if self.active_row_index is None:
            return
        new_index = self.active_row_index + relative_index
        if (new_index < 0
                and self.previous_range_button and self.previous_range_button['state'] == 'normal'):
            delta = self._go_to_previous_entry_range()
            new_row_index = -1 - delta
            self.select_entry_row_index(new_row_index, edit_if_already_selected=False)
            self.entry_canvas.yview_moveto(new_row_index / (self.ENTRY_RANGE_SIZE + 1))
        elif (new_index >= self.displayed_entry_count
              and self.next_range_button and self.next_range_button['state'] == 'normal'):
            delta = self._go_to_next_entry_range()
            new_row_index = 0 + self.ENTRY_RANGE_SIZE - delta
            self.select_entry_row_index(new_row_index, edit_if_already_selected=False)
            self.entry_canvas.yview_moveto(new_row_index / (self.ENTRY_RANGE_SIZE + 1))
        elif 0 <= new_index < self.displayed_entry_count:
            self.select_entry_row_index(self.active_row_index + relative_index)
        else:
            return  # Do nothing.

    def _entry_press_up(self, _=None):
        if self.active_row_index is not None:
            edit_new_text = self._e_entry_text_edit is not None
            edit_new_id = self._e_entry_id_edit is not None
            self._confirm_entry_text_edit(self.active_row_index)
            self._confirm_entry_id_edit(self.active_row_index)
            self._shift_selected_entry(-1)
            if edit_new_text:
                self._start_entry_text_edit(self.active_row_index)
            elif edit_new_id:
                self._start_entry_id_edit(self.active_row_index)
            if self.entry_canvas.yview()[1] != 1.0 or self.active_row_index < self.displayed_entry_count - 5:
                self.entry_canvas.yview_scroll(-1, 'units')

    def _entry_press_down(self, _=None):
        if self.active_row_index is not None:
            edit_new_text = self._e_entry_text_edit is not None
            edit_new_id = self._e_entry_id_edit is not None
            self._confirm_entry_text_edit(self.active_row_index)
            self._confirm_entry_id_edit(self.active_row_index)
            self._shift_selected_entry(+1)
            if edit_new_text:
                self._start_entry_text_edit(self.active_row_index)
            elif edit_new_id:
                self._start_entry_id_edit(self.active_row_index)
            if self.entry_canvas.yview()[0] != 0.0 or self.active_row_index > 5:
                self.entry_canvas.yview_scroll(1, 'units')

    def _refresh_range_buttons(self, entry_count):
        if self.previous_range_button:
            if entry_count == 0 or self.first_display_index == 0:
                self.previous_range_button['state'] = 'disabled'
            else:
                self.previous_range_button['state'] = 'normal'
        if self.next_range_button:
            if entry_count == 0 or self.first_display_index >= entry_count - self.ENTRY_RANGE_SIZE:
                self.next_range_button['state'] = 'disabled'
            else:
                self.next_range_button['state'] = 'normal'

    # TODO: Make every data structure define all these interface functions. Then never need to subclass this.

    def get_entry_index(self, entry_id: int, category=None) -> int:
        """Get the absolute index (NOT the displayed row index) of the given entry ID in its data dictionary/list.

        Note that for some data types (such as maps), the entry index *is* the entry ID, making this a simple method.
        """
        raise NotImplementedError

    def get_entry_name(self, entry_id: int, category=None) -> str:
        """Get the name of the given entry ID. Category defaults to active category."""
        raise NotImplementedError

    def get_entry_data(self, entry_id: int, category=None):
        """Get the given entry's field dictionary. Category defaults to active category."""
        raise NotImplementedError

    def _set_entry_name(self, entry_id: int, text: str, category=None, update_row_index=None) -> bool:
        """Set the name of the given entry ID (exact implementation varies across the different data structures).
        Returns True if the change was actually made, and False otherwise.

        If `update_row_index` is given, that row index (which should contain the given entry ID) will be refreshed.

        Never recorded as an action (the calling function should handle that).
        """
        raise NotImplementedError

    def _set_entry_id(self, entry_id: int, new_id: int, category=None, update_row_index=None):
        """Set the ID of the given entry ID (exact implementation varies across the different data structures).

        If `update_row_index` is given, that row index (which should contain the given entry ID) will be refreshed.

        Never recorded as an action (the calling function should handle that).
        """
        raise NotImplementedError


class EntryNameEditBox(TextEditBox):
    WIDTH = 70  # characters
    HEIGHT = 10  # lines

    def __init__(self, master, category, entry_id, initial_name="", allow_newlines=True):
        if entry_id is None:
            window_title = f"Adding entry to {camel_case_to_spaces(category)}"
        else:
            window_title = f"Editing {camel_case_to_spaces(category)}[{entry_id}]"
        self.MASTER = master
        self.category = category
        self.entry_id = entry_id
        self._id = None
        super().__init__(master=master, initial_text=initial_name, allow_newlines=allow_newlines,
                         window_title=window_title)

        self.output = [None, None]

    def build(self):
        with self.set_master(auto_rows=0):
            if self.entry_id is None:
                self._id = self.Entry(label='New Entry ID:', label_position='left', width=10, integers_only=True,
                                      padx=20, pady=20).var
            else:
                self._id = None
            super().build()

    def done(self, confirm=True):
        if confirm:
            if self._id:
                if not self._id.get():
                    self.master.CustomDialog("ID Error", message="New entry ID must be set.")
                    return
                new_id = int(self._id.get())
                if new_id in self.MASTER.get_category_data():
                    self.MASTER.CustomDialog(
                        "ID Error", message=f"Entry ID {new_id} already exists in category "
                                            f"{camel_case_to_spaces(self.category)}.")
                    return
            else:
                new_id = None
            new_text = self._text.get('1.0', 'end' + '-1c')
            if not self.allow_newlines and '\n' in new_text:
                self.MASTER.CustomDialog("Text Error", "Entry cannot contain newlines.")
                return
            if new_text == self.initial_text:
                self.output = [None, None]
            else:
                self.output = [new_id, self._text.get('1.0', 'end' + '-1c')]
        self.quit()
