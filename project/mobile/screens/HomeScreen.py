from appium.webdriver.common.mobileby import MobileBy

from framework.mobile.elements.MobileButton import MobileButton
from framework.mobile.elements.MobileLabel import MobileLabel
from framework.mobile.elements.MobileTextBox import MobileTextBox
from framework.mobile.screens.MobileScreen import MobileScreen


class HomeScreen(MobileScreen):
    def __init__(self):
        super().__init__(MobileBy.XPATH, "//d.b.k.a.c[@content-desc='Home']", "CalendarScreen")
        self.btn_home = MobileButton(MobileBy.XPATH, "//d.b.k.a.c[@content-desc='Home']", "HomeButton")
        self.btn_add_note = MobileButton(MobileBy.ID, "com.yocto.wenote:id/linear_layout", "AddNoteButton")
        self.txb_note = MobileTextBox(MobileBy.ID, "com.yocto.wenote:id/body_edit_text", "NoteTextBox")
        self.btn_confirm_note = MobileButton(MobileBy.ID, "com.yocto.wenote:id/confirm_image_button", "ConfirmNote")
        self.lbl_note_title = MobileLabel(MobileBy.ID, "com.yocto.wenote:id/title_text_view", "NoteTitle")
        self.lbl_note_body = MobileLabel(MobileBy.ID, "com.yocto.wenote:id/body_text_view", "NoteBody")

    def go_to_home_screen(self):
        self.btn_home.click()

    def add_note(self, note):
        self.btn_add_note.click()
        self.txb_note.type_text(note)
        self.btn_confirm_note.click()

    def get_note_title(self):
        title = self.lbl_note_title.get_text()
        return title

    def get_note_body(self):
        body = self.lbl_note_body.get_text()
        return body
