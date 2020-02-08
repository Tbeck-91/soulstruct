from __future__ import annotations

import typing as tp
from soulstruct.project.utilities import bind_events
from soulstruct.utilities.core import camel_case_to_spaces
from soulstruct.utilities.window import SmartFrame


class BaseCategoryFrame(SmartFrame):
    CATEGORY_BOX_WIDTH = 250
    CATEGORY_BOX_HEIGHT = 400
    CATEGORY_ROW_HEIGHT = 30
    CATEGORY_ROW_HIGHLIGHT = 1
    CATEGORY_UNSELECTED_BG = '#242424'
    CATEGORY_SELECTED_BG = '#414141'

    def __init__(self):
        self.category_selected_entry_id = {}  # maps categories to their currently selected entry IDs
        self.unsaved_changes = set()  # set of changed (category, param_id, action_type) pairs to highlight

        self.active_category = None
        self.category_boxes = {}
        self.category_canvas = None
        self.category_i_frame = None

    def build_category_canvas(self):
        with self.set_master(sticky='nsew', row_weights=[1], column_weights=[1], auto_columns=0):
            self.category_canvas = self.Canvas(
                vertical_scrollbar=True, yscrollincrement=self.CATEGORY_ROW_HEIGHT,
                width=self.CATEGORY_BOX_WIDTH, height=self.CATEGORY_BOX_HEIGHT,
                borderwidth=0, highlightthickness=0, sticky='nsew')
        with self.set_master(self.category_canvas):
            self.category_i_frame = self.Frame(sticky='nsew')
        self.link_to_scrollable(self.category_canvas, self.category_i_frame)
        self.category_canvas.create_window(0, 0, window=self.category_i_frame, anchor='n')
        self.category_i_frame.bind("<Configure>", lambda e, c=self.category_canvas: self.reset_canvas_scroll_region(c))

    def select_category(self, selected_category: tp.Optional[str], first_display_index=0, auto_scroll=False,
                        view_change=False):
        """Updates `active_category` attribute and row colors.

        By default, resets `first_display_index` to zero.
        Supports 'selected_category=None' to deselect all categories.
        Optionally recorded as a view change (e.g. from manually clicking the category).
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
                else:
                    box['bg'] = self.CATEGORY_UNSELECTED_BG
                    label['bg'] = self.CATEGORY_UNSELECTED_BG

        if auto_scroll:
            view_ratio = list(self.category_boxes).index(self.active_category) / (len(self.category_boxes) + 1)
            self.category_canvas.yview_moveto(view_ratio)

        self.first_display_index = first_display_index
        self.select_entry_row_index(None, edit_if_already_selected=False)
        self.refresh_entries()
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

    def _shift_selected_category(self, relative_index):
        """Change category by given relative index (usually +1 or -1). Doesn't count as a view change."""
        if self.active_category is None:
            return
        categories = self._get_display_categories()
        active_category_index = categories.index(self.active_category)
        new_index = active_category_index + relative_index
        if 0 <= new_index < len(categories):
            new_category = categories[new_index]
            self.select_category(new_category)
        else:
            return  # Do nothing.

    def _category_press_up(self, _=None):
        if self.active_category is not None:
            categories = self._get_display_categories()
            active_category_index = categories.index(self.active_category)
            self._shift_selected_category(-1)
            if self.category_canvas.yview()[1] != 1.0 or active_category_index < len(categories) - 5:
                self.category_canvas.yview_scroll(-1, 'units')

    def _category_press_down(self, _=None):
        if self.active_category is not None:
            categories = self._get_display_categories()
            active_category_index = categories.index(self.active_category)
            self._shift_selected_category(+1)
            if self.category_canvas.yview()[0] != 0.0 or active_category_index > 5:
                self.category_canvas.yview_scroll(1, 'units')

    def refresh_categories(self):
        """There are few enough categories changing rarely enough that the widgets can just be regenerated."""
        self.select_category(None)
        for box, label in self.category_boxes.values():
            box.destroy()
            label.destroy()
        self.category_boxes = {}
        with self.set_master(self.category_i_frame):

            categories = self._get_display_categories()

            for row, category in enumerate(categories):
                box = self.Frame(
                    row=row, width=self.CATEGORY_BOX_WIDTH, height=self.CATEGORY_ROW_HEIGHT,
                    highlightthickness=self.CATEGORY_ROW_HIGHLIGHT,
                    bg=self.CATEGORY_UNSELECTED_BG, sticky='nsew')
                label_text = camel_case_to_spaces(category).replace('_', ': ')
                label = self.Label(text=label_text, sticky='w', row=row, fg=self._get_category_text_fg(category),
                                   bg=self.CATEGORY_UNSELECTED_BG, padx=1, font_size=10)
                for widget in {label, box}:
                    bind_events(widget, {
                        "<Button-1>": lambda e, c=category: self.select_category(c, view_change=True),
                        '<Up>': self._category_press_up,
                        '<Down>': self._category_press_down,
                        '<Prior>': self._category_press_up,
                        '<Next>': self._category_press_down,
                    })
                if category == self.active_category:
                    label['bg'] = self.CATEGORY_SELECTED_BG
                    box['bg'] = self.CATEGORY_SELECTED_BG
                self.link_to_scrollable(self.category_canvas, box, label)
                self.category_boxes[category] = (box, label)

        self.category_canvas.yview_moveto(0)
        self.category_i_frame.columnconfigure(0, weight=1)

    @staticmethod
    def _get_category_text_fg(category: str):
        """Returns white text by default. Override to add custom colors based on category name."""
        return '#FFF' if category else '#000'

    def _get_display_categories(self) -> list:
        """Get a list of categories to display."""
        raise NotImplementedError

    def get_category_data(self, category=None):
        """Get a dictionary (or for some data types, a list) of entries from the active category."""
        raise NotImplementedError

    def get_entry_id_range(self, category=None, first_index=None, last_index=None) -> list:
        """Get a list of entry IDs to display (as not all can be displayed at once)."""
        raise NotImplementedError
