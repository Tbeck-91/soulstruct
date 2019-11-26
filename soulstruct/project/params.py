from __future__ import annotations

from typing import TYPE_CHECKING

from soulstruct.project.editor import SoulstructBaseEditor, SoulstructBaseFieldEditor
from soulstruct.utilities.core import camel_case_to_spaces

if TYPE_CHECKING:
    from soulstruct.params import DarkSoulsGameParameters


# TODO: Can't jump to Conversations, because they're internal by default.


class SoulstructParamsEditor(SoulstructBaseFieldEditor):
    CATEGORY_BOX_WIDTH = 200
    ENTRY_BOX_WIDTH = 450
    ENTRY_RANGE_SIZE = 200

    class EntryRow(SoulstructBaseEditor.EntryRow):
        """Container for components of a row in the _ParamEntryFrame.

        These are only created once, and their contents are refreshed when needed.
        """
        def __init__(self, editor: SoulstructBaseEditor, row_index: int, main_bindings: dict = None):
            super().__init__(editor=editor, row_index=row_index, main_bindings=main_bindings)
            self.linked_text = ''

        def update_entry(self, entry_id: int, entry_text: str):
            """If 'linked_text' is an empty string, then text was expected, but not found (entry highlighted)."""
            self.entry_id = entry_id
            text_links = self.master.linker.param_entry_text_link(self.entry_id)
            self.linked_text = (f'    {{{text_links[0].name}}}' if text_links[0].name else '') if text_links else None
            self.entry_text = entry_text
            self._update_colors()
            self.build_entry_context_menu(text_links)
            self.tool_tip.text = text_links[2].name if text_links and text_links[2].name else None

        @property
        def entry_text(self):
            return self._entry_text

        @entry_text.setter
        def entry_text(self, value):
            self._entry_text = value
            self.text_label.var.set(self._entry_text + (self.linked_text if self.linked_text is not None else ''))

        def build_entry_context_menu(self, text_links=()):
            # TODO: 'View uses': search things that link to this type of param for this ID.
            super().build_entry_context_menu()
            text_links = self.master.linker.param_entry_text_link(self.entry_id)
            if text_links:
                self.context_menu.add_separator()
                for text_link in text_links:
                    text_link.add_to_context_menu(self.context_menu, foreground=self.STYLE_DEFAULTS['text_fg'])

    def __init__(self, params: DarkSoulsGameParameters, linker, master=None, toplevel=False):
        self.Params = params
        self.linker = linker
        super().__init__(linker, master=master, toplevel=toplevel, window_title="Soulstruct Params Editor")

    def build(self):
        with self.set_master(auto_rows=0):
            self.Frame(pady=30)
            with self.set_master(auto_columns=0):
                self.build_category_canvas()
                self.build_entry_frame()
                self.build_field_frame()

    def _get_display_categories(self):
        return self.Params.param_names

    def get_category_dict(self, category=None):
        if category is None:
            category = self.active_category
            if category is None:
                return {}
        return self.Params[category]

    def _get_category_name_range(self, category=None, first_index=None, last_index=None) -> list:
        if category is None:
            category = self.active_category
            if category is None:
                return []
        return self.Params[category].get_range(start=self.first_display_index, count=self.ENTRY_RANGE_SIZE)

    def get_entry_index(self, entry_id: int, category=None) -> int:
        """Get index of entry in category. Ignores current display range."""
        if category is None:
            category = self.active_category
            if category is None:
                raise ValueError("No param category selected.")
        if entry_id not in self.Params[category].entries:
            raise ValueError(f"Param ID {entry_id} does not appear in category {category}.")
        return sorted(self.Params[category].entries).index(entry_id)

    def get_entry_text(self, entry_id: int, category=None) -> str:
        if category is None:
            category = self.active_category
            if category is None:
                raise ValueError("No params category selected.")
        return self.Params[category][entry_id].name

    def _set_entry_text(self, entry_id: int, text: str, category=None):
        if category is None:
            category = self.active_category
            if category is None:
                raise ValueError("No params category selected.")
        self.Params[category][entry_id].name = text

    def _add_entry(self, entry_id, text, field_dict=None):
        if entry_id < 0:
            self.dialog("Entry ID Error", message=f"Entry ID cannot be negative.")
            return False
        if entry_id in self.get_category_dict():
            self.dialog("Text ID Error", message=f"Entry ID {entry_id} already exists in category "
                                                 f"{camel_case_to_spaces(self.active_category)}.")
            return False

        self._cancel_entry_name_edit()
        self.get_category_dict()[entry_id] = field_dict  # add entry to category dictionary
        self._set_entry_text(entry_id, text)
        self.select_entry_id(entry_id, set_focus_to_text=True, edit_if_already_selected=False)

        # TODO
        # if from_history:
        #     self.jump_to_category_and_entry(category, text_id)
        # if not from_history:
        #     self.action_history.record_action(
        #         undo=partial(self._delete_entry, category, text_id),
        #         redo=partial(self._add_entry, category, text_id, text),
        #     )
        # self.unsaved_changes.add((self.active_category, text_id, 'add'))

        return True

    def add_relative_entry(self, entry_id, offset=1, text=None):
        """Copies ParamEntry instance."""
        if text is None:
            text = self.get_entry_text(entry_id)  # Copies name of origin entry by default (can be overridden).
        new_field_dict = self.get_field_dict(entry_id).copy()  # Always copies entry data.
        self._add_entry(entry_id=entry_id + offset, text=text, field_dict=new_field_dict)

    def get_field_dict(self, entry_id: int, category=None):
        if category is None:
            category = self.active_category
            if category is None:
                raise ValueError("No params category selected.")
        return self.Params[category][entry_id]

    def get_field_info(self, field_dict, field_name=None, category=None):
        """This method should return the full field information dictionary if field_name is None."""
        if category is None:
            category = self.active_category
        return self.Params[category].get_field_info(field_dict, field_name=field_name)

    def get_field_links(self, field_type, field_value):
        return self.linker.soulstruct_link(field_type, field_value,
                                           valid_null_values={0: 'Default/None', -1: 'Default/None'})
