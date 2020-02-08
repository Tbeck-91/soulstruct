from __future__ import annotations

import logging
import typing as tp
from abc import ABC
from functools import partial

from soulstruct.project.utilities import ActionHistory, ViewHistory
from soulstruct.utilities import camel_case_to_spaces
from soulstruct.utilities.window import SmartFrame

from .categories import BaseCategoryFrame
from .entries import BaseEntryFrame
from .fields import BaseFieldFrame

if tp.TYPE_CHECKING:
    from soulstruct.project.links import WindowLinker

_LOGGER = logging.getLogger(__name__)


class BaseDataTab(SmartFrame, ABC):
    DATA_NAME = ""
    TAB_NAME = ""

    _categories: tp.Optional[BaseCategoryFrame]
    _entries: tp.Optional[BaseEntryFrame]
    _fields: tp.Optional[BaseFieldFrame]

    def __init__(self, linker: WindowLinker, master=None, toplevel=False, window_title="Soulstruct Editor",
                 with_fields=False):
        super().__init__(master=master, toplevel=toplevel, window_title=window_title)
        self.linker = linker
        self.action_history = ActionHistory()
        self.view_history = ViewHistory()

        self._categories = None
        self._entries = None
        self._fields = None

        self.build(with_fields)
        self.bind_all('<Control-z>', self.undo)
        self.bind_all('<Control-y>', self.redo)
        self._categories.refresh_categories()
        self._entries.refresh_entries()
        if with_fields:
            self._fields.refresh()

    def build(self, with_fields):
        # TODO: yeah...
        if with_fields:
            with self.set_master(sticky='nsew', row_weights=[1], column_weights=[0, 1], auto_columns=0):
                self.build_category_canvas()
                with self.set_master(sticky='nsew', row_weights=[0, 1, 0], column_weights=[1, 1]):
                    self.build_previous_range_button(row=0, column=0)
                    self.build_hidden_fields_checkbutton(row=0, column=1)
                    with self.set_master(sticky='nsew', row=1, column=0, row_weights=[1], column_weights=[1]):
                        self.build_entry_frame()
                    with self.set_master(sticky='nsew', row=1, column=1, row_weights=[1], column_weights=[1]):
                        self.build_field_frame()
                    self.build_next_range_button(row=2, column=0)
        else:
            with self.set_master(sticky='nsew', row_weights=[1], column_weights=[0, 1], auto_columns=0):
                self.category_frame = None  # TODO
                self.entry_frame = None  # TODO

    def undo(self, _=None):
        if not self.action_history.undo():
            # TODO: flash undo button red to indicate there's nothing to undo.
            pass

    def redo(self, _=None):
        if not self.action_history.redo():
            # TODO: flash redo button red to indicate there's nothing to undo.
            pass

    # ---------------- #
    #   JUMP METHODS   #
    # ---------------- #

    def jump_to_entry(self, category, entry_id):
        """Jump to given entry ID in given category and record view change."""
        from_category = self._categories.active_category
        from_entry_id = self._entries.get_entry_id()

        self.linker.jump(self.TAB_NAME, category, entry_id)
        self.view_history.record_view_change(
            back=partial(self.linker.jump, self.TAB_NAME, from_category, from_entry_id),
            forward=partial(self.linker.jump, self.TAB_NAME, category, entry_id)
        )

    # ----------------------- #
    #   CROSS-FRAME METHODS   #
    # ----------------------- #

    @property
    def active_category(self):
        return self._categories.active_category

    def get_category_data(self, category=None):
        return self._categories.get_category_data(category)

    def get_entry_id_range(self, category=None, first_index: int = None, last_index: int = None):
        return self._categories.get_entry_id_range(category, first_index, last_index)

    def get_entry_data(self, entry_id: int, category=None):
        return self._fields.get_entry_data(entry_id, category)

    def set_entry_data(self, entry_id: int, entry_data: dict, category=None):
        self.get_category_data(category)[entry_id] = entry_data

    def refresh_fields(self):
        if self._fields:
            self._fields.refresh()
            return True
        return False


class BaseFieldDataTab(BaseDataTab, ABC):

    def select_category(self, selected_category: Optional[str], first_display_index=0, auto_scroll=False,
                        view_change=False):
        """Updates `active_category` attribute and row colors.

        By default, resets `first_display_index` to zero.
        Supports 'selected_category=None' to deselect all categories.
        """
        old_category = self.active_category

        if old_category is not None:
            selected_entry_id = self.get_entry_id(self.active_row_index) if self.active_row_index else None
            self.category_selected_entry_id[old_category] = selected_entry_id

        if selected_category != self.active_category:
            self.active_category = selected_category
            for category, (box, label) in self.category_boxes.items():
                if selected_category == category:
                    box['bg'] = self.CATEGORY_SELECTED_BG
                    label['bg'] = self.CATEGORY_SELECTED_BG
                    label.focus_set()
                else:
                    box['bg'] = self.CATEGORY_UNSELECTED_BG
                    label['bg'] = self.CATEGORY_UNSELECTED_BG

        if auto_scroll:
            view_ratio = list(self.category_boxes).index(self.active_category) / (len(self.category_boxes) + 1)
            self.category_canvas.yview_moveto(view_ratio)

        self.first_display_index = first_display_index
        self.select_entry_row_index(None, edit_if_already_selected=False)
        self.refresh_entries(reset_field_display=True)  # TODO: this argument is the only difference. Better way?
        last_selected_entry_id = self.category_selected_entry_id.get(self.active_category, None)
        if last_selected_entry_id is not None:
            self.select_entry_id(last_selected_entry_id, edit_if_already_selected=False)
        else:
            # Leave no entry selected.
            self.entry_canvas.yview_moveto(0)

        if view_change and old_category is not None:
            self.view_history.record_view_change(
                back=lambda: self.select_category(old_category),
                forward=lambda: self.select_category(selected_category)
            )

    def refresh_entries(self, reset_field_display=False):
        super().refresh_entries()
        self.refresh_fields(reset_display=reset_field_display)

    def select_entry_row_index(self, row_index, set_focus_to_text=True, edit_if_already_selected=True,
                               id_clicked=False, view_change=False):
        super().select_entry_row_index(row_index, set_focus_to_text=set_focus_to_text,
                                       edit_if_already_selected=edit_if_already_selected, id_clicked=id_clicked,
                                       view_change=view_change)
        self.refresh_fields()

        # `refresh_fields()` seems to steal focus aggressively, so end by setting it back to entry name.
        if row_index is not None and set_focus_to_text:
            self.entry_rows[row_index].text_label.focus_set()
