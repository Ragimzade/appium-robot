# -*- coding: utf-8 -*-
from datetime import datetime

from framework.utils.TestDataReader import TestDataReader
from project.mobile.screens.CalendarScreen import CalendarScreen
from project.mobile.screens.HomeScreen import HomeScreen
from project.mobile.screens.StartScreen import StartScreen
from framework.robotwrappers.Asserts import Asserts


class AppSteps:

    @staticmethod
    def search_car(data_path_string):
        car = TestDataReader().read_test_data(data_path_string)
        StartScreen().fill_car_search(car)
        StartScreen().btn_search.click()

    @staticmethod
    def message_is_displayed(data_path_string):
        """Method assert message."""
        expected_error_text = TestDataReader().read_locale_dict(data_path_string)
        actual_error_text = StartScreen().get_error_text()
        Asserts.should_be_equal(expected_error_text, actual_error_text)

    @staticmethod
    def navigate_to_calendar():
        CalendarScreen().go_to_calendar_screen()

    @staticmethod
    def verify_current_date_is_correct():
        actual_date = CalendarScreen().get_current_date()
        expected_date = datetime.today().strftime('%b %Y')
        Asserts.should_be_equal(actual_date, expected_date)

    @staticmethod
    def navigate_to_home_screen():
        HomeScreen().go_to_home_screen()

    @staticmethod
    def create_note(data_path_string):
        value_for_note = TestDataReader().read_test_data(data_path_string)
        HomeScreen().add_note(value_for_note)

    @staticmethod
    def assert_note_title_is_correct(data_path_string):
        actual_title = HomeScreen().get_note_title()
        expected_title = TestDataReader().read_test_data(data_path_string)
        Asserts.should_be_equal(actual_title, expected_title)

    @staticmethod
    def assert_note_body_is_correct(data_path_string):
        actual_body = HomeScreen().get_note_body()
        expected_body = TestDataReader().read_test_data(data_path_string)
        Asserts.should_be_equal(actual_body, expected_body)
