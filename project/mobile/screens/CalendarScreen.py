from appium.webdriver.common.mobileby import MobileBy

from framework.mobile.elements.MobileButton import MobileButton
from framework.mobile.elements.MobileLabel import MobileLabel
from framework.mobile.screens.MobileScreen import MobileScreen


class CalendarScreen(MobileScreen):
    def __init__(self):
        super().__init__(MobileBy.XPATH, "//d.b.k.a.c[@content-desc='Calendar']", "CalendarScreen")
        self.btn_calendar = MobileLabel(MobileBy.XPATH, "//d.b.k.a.c[@content-desc='Calendar']", "CalendarScreen")
        self.btn_current_date = MobileButton(MobileBy.ID, "com.yocto.wenote:id/month_year_text_view",
                                             "CurrentDateButton")

    def go_to_calendar_screen(self):
        self.btn_calendar.click()

    def get_current_date(self):
        date = self.btn_current_date.get_text()
        return date


