from appium.webdriver.common.mobileby import MobileBy

from framework.mobile.elements.MobileButton import MobileButton
from framework.mobile.elements.MobileLabel import MobileLabel
from framework.mobile.screens.MobileScreen import MobileScreen


class AllScreen(MobileScreen):

    def __init__(self):
        super().__init__(MobileBy.XPATH, "//d.b.k.a.c[@content-desc='All']", "All Screen")
        self.btn_all = MobileButton(MobileBy.XPATH, "//d.b.k.a.c[@content-desc='All']", "allButton")
        self.lbl_note_title = MobileLabel(MobileBy.ID, "com.yocto.wenote:id/title_text_view", "NoteTitle")
        self.lbl_note_body = MobileLabel(MobileBy.ID, "com.yocto.wenote:id/body_text_view", "NoteBody")
        self.lbl_note_footer = MobileLabel(MobileBy.ID, "com.yocto.wenote:id/label_text_view", "NoteFooter")


