from enum import IntEnum

from soulstruct.project.base.core import BaseFieldDataTab, _LOGGER
from soulstruct.project.utilities import bind_events
from soulstruct.utilities import camel_case_to_spaces
from soulstruct.utilities.window import ToolTip, SmartFrame


class FieldRow(object):
    """Container/manager for widgets in a single field row in the Editor.

    These are only created once, and their contents are refreshed when needed (e.g. when a new entry is selected).
    Unlike entries, field value widgets may be Labels (which turn into Entries for editing), Checkbuttons, or
    Comboboxes. Each of these widgets is created for each row, so they can be hidden/dispalyed when needed by a
    given field type, rather than dynamically creating and destroying them every time a new entry/category is
    selected.
    """
    def __init__(self, editor: BaseFieldDataTab, row_index: int, main_bindings: dict = None):
        self.master = editor
        self.STYLE_DEFAULTS = editor.STYLE_DEFAULTS

        self.row_index = row_index
        self._active = False
        self._default_value = False
        self.field_name = ""
        self.field_type = None
        self.field_nickname = ""
        self.field_docstring = ""
        self.link_missing = False

        bg_color = self._get_color()

        self.row_box = editor.Frame(
            width=editor.FIELD_BOX_WIDTH, height=editor.FIELD_ROW_HEIGHT, bg=bg_color,
            row=row_index, columnspan=2, sticky='nsew')
        bind_events(self.row_box, main_bindings)

        self.field_name_box = editor.Frame(row=row_index, column=0, bg=bg_color, sticky='w')
        bind_events(self.field_name_box, main_bindings)

        self.field_name_label = editor.Label(
            self.field_name_box, text='', fg=editor.FIELD_NAME_FG, width=editor.FIELD_NAME_WIDTH,
            bg=bg_color, anchor='w', font_size=10)
        bind_events(self.field_name_label, main_bindings)

        self.value_box = editor.Frame(
            width=editor.FIELD_VALUE_BOX_WIDTH, row=row_index, column=1, bg=bg_color, sticky='ew')
        bind_events(self.value_box, main_bindings)

        # VALUE WIDGETS

        self.value_label = editor.Label(
            self.value_box, text='', bg=bg_color, width=editor.FIELD_VALUE_WIDTH, anchor='w')
        bind_events(self.value_label, main_bindings)

        self.value_checkbutton = editor.Checkbutton(
            self.value_box, label=None, bg=bg_color, no_grid=True, selectcolor='#000',
            command=self._checkbutton_toggle)
        # Main focus bindings are not bound to Checkbutton.

        self.value_combobox = editor.Combobox(
            self.value_box, values=None, width=editor.FIELD_VALUE_WIDTH, no_grid=True, font=("Segoe UI", 10),
            on_select_function=self._combobox_choice)
        self.value_combobox.bind('<MouseWheel>', lambda _: 'break')  # prevent scrolling on collapsed Combobox
        # Main focus bindings are not bound to Combobox.

        # TODO: BEHAVIOR_REF_TYPE combobox should also force a refresh, as it may change field names.
        #  (Class will need access to ParamEntry for this, which is fine.)

        self.context_menu = editor.Menu(self.row_box)
        self.tool_tip = ToolTip(self.row_box, self.field_name_box, self.field_name_label, text=None)

        self.active_value_widget = self.value_label
        self.hide()

    def _combobox_choice(self, _=None):
        """Updates field value with integer value from Combobox enum or unknown integer."""
        combobox_string = self.value_combobox.var.get()
        if combobox_string.startswith('Unknown: '):
            value = int(combobox_string[len('Unknown: '):])
        else:
            value = getattr(self.field_type, self.value_combobox.var.get().replace(' ', '')).value
        self.master.change_field_value(self.field_name, value)

    def _activate_value_widget(self, widget):
        if id(self.active_value_widget) != id(widget):
            self.active_value_widget.grid_remove()
        self.active_value_widget = widget

    def _checkbutton_toggle(self):
        new_value = self.value_checkbutton.var.get()
        if self.master.change_field_value(self.field_name, new_value):
            self.value_checkbutton.config(fg='#3F3' if new_value else '#F33', text='ON' if new_value else 'OFF')
        else:
            self.value_checkbutton.var.set(not new_value)

    def update_field(self, entry, name, nickname, value, field_type, docstring="DOC-TODO"):
        """Update widgets with given field information."""
        self.field_name = name
        self.field_type = field_type
        self.field_nickname = camel_case_to_spaces(nickname)
        self.field_docstring = docstring

        if self.field_name_label.var.get() != self.field_nickname:
            self.field_name_label.var.set(self.field_nickname)

        if isinstance(self.field_type, str):
            # Note that the *argument* `field_type` is used below, not attribute `self.field_type`.
            field_links = self.master.get_field_links(self.field_type, value)
            field_type = int
        else:
            field_links = []

        if not isinstance(field_type, str) and issubclass(field_type, IntEnum):
            self.value_combobox['values'] = [camel_case_to_spaces(e.name) for e in field_type]
            try:
                # noinspection PyUnresolvedReferences
                enum_name = camel_case_to_spaces(field_type(value).name)
            except ValueError:
                enum_name = f'Unknown: {value}'
            self.value_combobox.var.set(enum_name)
            self._activate_value_widget(self.value_combobox)
        elif field_type in {float, int}:
            value_text = f'{value:.3f}' if field_type == float else str(value)
            if field_links:
                if len(field_links) > 1:
                    value_text += '    {AMBIGUOUS}'
                if field_links[0].name is None:
                    value_text += '    {BROKEN LINK}'
                else:
                    value_text += f'    {{{field_links[0].name}}}'
            if self.value_label.var.get() != value_text:
                self.value_label.var.set(value_text)  # TODO: probably redundant in terms of update efficiency
            self._activate_value_widget(self.value_label)
        elif field_type == bool:
            if value not in {0, 1}:
                raise ValueError(f"Field with 'bool' type has non-boolean value: {value}")
            self.value_checkbutton.var.set(value)
            self.value_checkbutton.config(fg='#3F3' if value else '#F33', text='ON' if value else 'OFF')
            self._activate_value_widget(self.value_checkbutton)

        if field_links and not any(link.name for link in field_links) and not self.link_missing:
            self.link_missing = True
            self._update_colors()
        elif (not field_links or any(link.name for link in field_links)) and self.link_missing:
            self.link_missing = False
            self._update_colors()

        if self._is_default(field_type, value, self.field_nickname):
            self.field_name_label["fg"] = self.master.FIELD_NAME_FG_DEFAULT
            self.value_label["fg"] = self.master.FIELD_VALUE_FG_DEFAULT
        else:
            self.field_name_label["fg"] = self.master.FIELD_NAME_FG
            self.value_label["fg"] = self.master.FIELD_VALUE_FG

        self.build_field_context_menu(field_links)
        self.tool_tip.text = docstring

        self.unhide()

    def hide(self):
        """Called when this row has no field to display (e.g. for smaller ParamTables or unselected entry)."""
        self.row_box.grid_remove()
        self.field_name_box.grid_remove()
        self.field_name_label.grid_remove()
        self.value_box.grid_remove()
        self.active_value_widget.grid_remove()

    def unhide(self):
        self.row_box.grid()
        self.field_name_box.grid()
        self.field_name_label.grid()
        self.value_box.grid()
        self.active_value_widget.grid()

    def build_field_context_menu(self, field_links=()):
        # TODO: other stuff? Pop out a scroll box to select an entry, for linked fields?
        self.context_menu.delete(0, 'end')
        if field_links:
            for field_link in field_links:
                field_link.add_to_context_menu(self.context_menu, foreground=self.STYLE_DEFAULTS['text_fg'])

    @property
    def editable(self):
        return self.active_value_widget is self.value_label

    def confirm_edit(self, new_text):
        """Inspects new text and returns new field value, or None if the field shouldn't be changed."""
        if not self.editable:
            raise TypeError("Cannot edit a boolean or dropdown field. (Internal error, tell the developer!)")

        if isinstance(self.field_type, str):
            new_value = int(new_text)
            field_links = self.master.get_field_links(self.field_type, new_value)
            if len(field_links) > 1:
                new_text += '    {AMBIGUOUS}'
            elif field_links and field_links[0].name is None:
                new_text += '    {BROKEN LINK}'
            elif field_links:
                new_text += f'    {{{field_links[0].name}}}'
            self.value_label.var.set(new_text)
            return new_value

        if self.field_type in {float, int}:
            if new_text == "-":
                return None  # no change
            if self.field_type == float:
                new_value = float(new_text)
                self.value_label.var.set(f"{new_value:.3f}")
                if self._is_default(self.field_type, new_value, self.field_nickname):
                    self.field_name_label["fg"] = self.master.FIELD_NAME_FG_DEFAULT
                    self.value_label["fg"] = self.master.FIELD_VALUE_FG_DEFAULT
                else:
                    self.field_name_label["fg"] = self.master.FIELD_NAME_FG
                    self.value_label["fg"] = self.master.FIELD_VALUE_FG
                return new_value
            elif self.field_type == int:
                new_value = int(new_text)
                self.value_label.var.set(str(new_value))
                if self._is_default(self.field_type, new_value, self.field_nickname):
                    self.field_name_label["fg"] = self.master.FIELD_NAME_FG_DEFAULT
                    self.value_label["fg"] = self.master.FIELD_VALUE_FG_DEFAULT
                else:
                    self.field_name_label["fg"] = self.master.FIELD_NAME_FG
                    self.value_label["fg"] = self.master.FIELD_VALUE_FG
                return new_value

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

        # All widget backgrounds need updating (except Combobox).
        self._update_colors()

    def _update_colors(self):
        bg_color = self._get_color()
        for widget in (self.row_box, self.field_name_box, self.field_name_label, self.value_box,
                       self.value_label, self.value_checkbutton):
            widget['bg'] = bg_color

    def _get_color(self):
        """Inspects field name/data and returns an RGB string."""
        base_bg = int(self.STYLE_DEFAULTS['bg'].lstrip('#'))  # dark grey
        if self.link_missing:
            base_bg += 100
        if self._active:
            base_bg += 123
        if self.row_index % 2:
            base_bg += 111
        return f'#{base_bg}'

    def _is_default(self, field_type, value, field_nickname=""):
        if self.master.TAB_NAME == "params":
            if field_type == int:
                if value in (-1, 0, 1):
                    # TODO: Will have some false positives.
                    return True
            elif field_type == float:
                if field_nickname.endswith("Multiplier"):
                    if value == 1.0:
                        return True
                else:
                    if value in (0.0, 1.0):
                        return True
        return False


class BaseFieldFrame(SmartFrame):
    FIELD_CANVAS_BG = '#1d1d1d'
    FIELD_BOX_WIDTH = 450
    FIELD_BOX_HEIGHT = 400
    FIELD_ROW_HEIGHT = 30
    FIELD_NAME_WIDTH = 30
    FIELD_VALUE_BOX_WIDTH = 200
    FIELD_VALUE_WIDTH = 50
    FIELD_ROW_COUNT = 0  # must be set in child
    FIELD_NAME_FG = '#DDE'
    FIELD_NAME_FG_DEFAULT = '#777'
    FIELD_VALUE_FG = '#FFF'
    FIELD_VALUE_FG_DEFAULT = '#777'

    def __init__(self):
        if self.FIELD_ROW_COUNT == 0:
            raise AttributeError("Class attribute `FIELD_ROW_COUNT` must be set by child of SoulstructBaseFieldEditor.")
        self.show_hidden_fields = None
        self.field_canvas = None
        self.field_i_frame = None
        self.e_field_value_edit = None
        self.selected_field_row_index = None
        self.displayed_field_count = 0
        self.field_rows = []  # type: List[BaseFieldDataTab.FieldRow]

    def build_hidden_fields_checkbutton(self, **kwargs):
        self.show_hidden_fields = self.Checkbutton(
            label='Show hidden fields', initial_state=False,
            command=lambda: self.refresh(reset_display=True), pady=10, **kwargs).var

    def build_field_frame(self):
        self.field_canvas = self.Canvas(
            yscrollincrement=self.FIELD_ROW_HEIGHT, vertical_scrollbar=True, horizontal_scrollbar=True,
            borderwidth=10, highlightthickness=0, bg=self.FIELD_CANVAS_BG, sticky='nsew',
            row_weights=[1], column_weights=[1])
        self.field_i_frame = self.Frame(frame=self.field_canvas, width=self.FIELD_BOX_WIDTH, sticky='nsew')
        self.field_i_frame.bind("<Configure>", lambda e, c=self.field_canvas: self.reset_canvas_scroll_region(c))
        self.field_canvas.create_window(0, 0, window=self.field_i_frame, anchor='nw')

        with self.set_master(self.field_i_frame):
            for row in range(self.FIELD_ROW_COUNT):
                self.field_rows.append(FieldRow(
                    self, row_index=row,
                    main_bindings={
                        '<Button-1>': lambda _, i=row: self.select_displayed_field_row(i),
                        '<Button-3>': lambda e, i=row: self._right_click_field(e, i),
                        '<Up>': self._field_press_up,
                        '<Down>': self._field_press_down,
                    }))

    def refresh(self, reset_display=False):
        """Refresh all field information."""
        # TODO: what is setting focus in here?
        field_dict = self.get_selected_field_dict()

        self._cancel_field_value_edit()

        show_hidden_fields = self.show_hidden_fields.get()
        field_info_dict = self.get_field_info(field_dict)
        # field_names = self.get_field_names(field_dict)

        row = 0
        for field_name in field_info_dict:

            try:
                field_nickname, is_main, field_type, field_doc = self.get_field_info(field_dict, field_name)
            except ValueError as e:
                raise ValueError(f"Could not get field information for field {field_name}. Error: {str(e)}")

            if (isinstance(field_type, str) and '<Pad:' in field_type) or (not is_main and not show_hidden_fields):
                continue  # Skip hidden field (or always skip Pad field).

            try:
                field_value = field_dict[field_name]
            except KeyError:
                # Only some DSR-specific fields are allowed to be absent.
                if field_doc.startswith("<DSR>"):
                    continue
                raise

            self.field_rows[row].update_field(
                entry=field_dict,
                name=field_name,
                nickname=field_nickname,
                value=field_value,
                field_type=field_type,
                docstring=field_doc,
            )
            row += 1

        self.displayed_field_count = row

        for remaining_row in range(row, self.FIELD_ROW_COUNT):
            self.field_rows[remaining_row].hide()

        self.field_i_frame.grid_columnconfigure(1, weight=1)

        if reset_display:
            self.select_displayed_field_row(0, edit_if_already_selected=False)
            self.update_idletasks()
            self.field_canvas.yview_moveto(0)

    def _right_click_field(self, event, field_index):
        self.select_displayed_field_row(field_index, edit_if_already_selected=False)
        self.field_rows[field_index].context_menu.tk_popup(event.x_root, event.y_root)

    def select_field_name(self, field_name, set_focus_to_value=True, edit_if_already_selected=False, auto_scroll=True):
        row_index = self.get_field_row_index_from_name(field_name)
        self.select_displayed_field_row(row_index, set_focus_to_value=set_focus_to_value,
                                        edit_if_already_selected=edit_if_already_selected)
        self.refresh()

        self.field_canvas.yview_moveto(0)
        if auto_scroll:
            self.field_canvas.yview_scroll(row_index, "units")

    def select_displayed_field_row(self, row_index, set_focus_to_value=True, edit_if_already_selected=True):
        old_row_index = self.selected_field_row_index

        if old_row_index is not None and row_index is not None:
            if row_index == old_row_index:
                if edit_if_already_selected and self.field_rows[row_index].editable:
                    return self._start_field_value_edit(row_index)
                return
        else:
            self._cancel_field_value_edit()

        self.selected_field_row_index = row_index

        if old_row_index is not None:
            self.field_rows[old_row_index].active = False
        if row_index is not None:
            self.field_rows[row_index].active = True
            if set_focus_to_value:
                self.field_rows[row_index].active_value_widget.focus_set()

    def _field_press_up(self, _=None):
        if self.selected_field_row_index is not None:
            edit_new = self.e_field_value_edit is not None
            self._confirm_field_value_edit(self.selected_field_row_index)
            self._shift_selected_field(-1)
            if edit_new and self.field_rows[self.selected_field_row_index].editable:
                self._start_field_value_edit(self.selected_field_row_index)
            if self.field_canvas.yview()[1] != 1.0 or self.selected_field_row_index < self.displayed_field_count - 5:
                self.field_canvas.yview_scroll(-1, 'units')

    def _field_press_down(self, _=None):
        if self.selected_field_row_index is not None:
            edit_new = self.e_field_value_edit is not None
            self._confirm_field_value_edit(self.selected_field_row_index)
            self._shift_selected_field(+1)
            if edit_new and self.field_rows[self.selected_field_row_index].editable:
                self._start_field_value_edit(self.selected_field_row_index)
            if self.field_canvas.yview()[0] != 0.0 or self.selected_field_row_index > 5:
                self.field_canvas.yview_scroll(1, 'units')

    def _shift_selected_field(self, relative_index):
        if (self.selected_field_row_index is None
                or not 0 <= self.selected_field_row_index + relative_index < self.displayed_field_count):
            return
        self.select_displayed_field_row(self.selected_field_row_index + relative_index)

    def _get_field_edit_widget(self, row_index):
        field_row = self.field_rows[row_index]
        if not field_row.editable:
            raise TypeError("Cannot edit a boolean or dropdown field. (Internal error, tell the developer!)")
        field_type = field_row.field_type
        field_value = self.get_entry_data(self.get_entry_id(self.active_row_index))[field_row.field_name]
        if field_type in {int, float} or isinstance(field_type, str):
            return self.Entry(
                field_row.value_box,
                integers_only=field_type == int,
                numbers_only=field_type == float,
                initial_text=str(field_value),
                sticky='ew', width=5)
        raise TypeError(f"Could not determine editing box from type {field_type}.")

    def _start_field_value_edit(self, row_index):
        if not self.e_field_value_edit:
            self.e_field_value_edit = self._get_field_edit_widget(row_index)
            if not self.e_field_value_edit:
                return  # Edit attempt was rejected.
            self.e_field_value_edit.bind('<Return>', lambda e, i=row_index: self._confirm_field_value_edit(i))
            self.e_field_value_edit.bind('<Up>', self._field_press_up)
            self.e_field_value_edit.bind('<Down>', self._field_press_down)
            self.e_field_value_edit.bind('<FocusOut>', lambda e: self._cancel_field_value_edit())
            self.e_field_value_edit.bind('<Escape>', lambda e: self._cancel_field_value_edit())
            self.e_field_value_edit.focus_set()
            self.e_field_value_edit.select_range(0, 'end')

    def _cancel_field_value_edit(self):
        if self.e_field_value_edit:
            self.e_field_value_edit.destroy()
            self.e_field_value_edit = None

    def _confirm_field_value_edit(self, index):
        if self.e_field_value_edit:
            try:
                true_value = self.field_rows[index].confirm_edit(new_text=self.e_field_value_edit.var.get())
            except ValueError as e:
                # Entry input restrictions are supposed to prevent this.
                _LOGGER.error(f"Could not interpret field value. Error: {str(e)}")
                self.bell()
                return
            if true_value is not None:
                self.change_field_value(self.field_rows[index].field_name, true_value)
            self._cancel_field_value_edit()

    def change_field_value(self, field_name: str, new_value):
        """New value should have already been converted to its appropriate type."""
        field_dict = self.get_selected_field_dict()
        old_value = field_dict[field_name]
        if old_value == new_value:
            return False  # Nothing to change.
        field_dict[field_name] = new_value
        return True

    def get_field_row_index_from_name(self, field_name):
        for row in self.field_rows:
            if row.field_name == field_name:
                return row.row_index
        raise KeyError(f"Field name {field_name} does not exist in active category/entry.")

    def get_selected_field_dict(self):
        """Returns None if no field is selected."""
        if self.active_row_index is not None:
            entry_id = self.get_entry_id(self.active_row_index)
            return self.get_entry_data(entry_id)
        else:
            return None

    def get_field_names(self, field_dict):
        raise NotImplementedError

    def get_field_info(self, field_dict, field_name=None):
        """This method should return the full field information dictionary if field_name is None."""
        raise NotImplementedError

    def get_field_links(self, field_type, field_value, special_values=None) -> list:
        raise NotImplementedError
