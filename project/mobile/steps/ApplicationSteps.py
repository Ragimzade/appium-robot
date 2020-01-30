from selenium.common.exceptions import TimeoutException

from framework.utils.DataReader import DataReader
from framework.utils.robot_wrappers.RobotAsserts import RobotAsserts
from framework.utils.robot_wrappers.RobotCommonMethods import RobotCommonMethods
from framework.utils.robot_wrappers.RobotLogger import RobotLogger
from project.mobile.screens.alerts.PresentInCityAlert import PresentInCityAlert
from project.mobile.screens.alerts.UserRegistrationAlert import UserRegistrationAlert
from project.mobile.screens.CategoryScreen import CategoryScreen
from project.mobile.screens.CityProductsScreen import CityProductsScreen
from project.mobile.screens.ProductWithDiscountScreen import ProductWithDiscountScreen
from project.mobile.screens.SellerInfoScreen import SellerInfoScreen
from project.mobile.screens.StartScreen import StartScreen


class ApplicationSteps:
    @staticmethod
    def click_city_label():
        StartScreen().lbl_city.click()
        if ApplicationSteps.is_city_alert_present():
            PresentInCityAlert().click_do_not_show()

    @staticmethod
    def fill_city_search(data_path_string):
        city = DataReader().read_env_test_data(data_path_string)
        StartScreen().fill_city_search(city)

    @staticmethod
    def is_city_alert_present():
        try:
            PresentInCityAlert()
            RobotLogger.info('City alert is present')
            return True
        except TimeoutException:
            RobotLogger.info("City alert isn't present")
            return False

    @staticmethod
    def click_first_search_result():
        StartScreen().select_search_result()

    @staticmethod
    def check_selected_region_and_return_product_model(data_path_string, product_info_model):
        city = DataReader().read_env_test_data(data_path_string)
        CityProductsScreen(city)
        product_info = CityProductsScreen(city).get_product_info()
        RobotCommonMethods.set_test_variable(product_info_model, product_info)

    @staticmethod
    def select_first_item_with_discount_and_return_product_model_with_discount(data_path_string,
                                                                               product_with_discount_model):
        city = DataReader().read_env_test_data(data_path_string)
        CityProductsScreen(city).tap_top_product_with_discount()
        product_with_discount = ProductWithDiscountScreen().get_product_with_discount_info()
        RobotCommonMethods.set_test_variable(product_with_discount_model, product_with_discount)

    @staticmethod
    def check_that_products_parameters_are_correct(act_product, exp_product):
        RobotAsserts.should_be_equal(exp_product, act_product)

    @staticmethod
    def click_to_seller_info():
        ProductWithDiscountScreen().click_seller_name()

    @staticmethod
    def check_that_seller_information_is_correct(product_with_discount):
        seller_info = SellerInfoScreen().get_seller_info(product_with_discount.seller_info.seller_name)
        RobotAsserts.should_be_equal(seller_info, product_with_discount.seller_info)

    @staticmethod
    def click_back_from_seller_info():
        SellerInfoScreen().click_back()

    @staticmethod
    def click_buy_for_product_with_discount_screen():
        ProductWithDiscountScreen().click_buy()

    @staticmethod
    def check_that_user_registration_alert_is_present():
        user_registration_alert = UserRegistrationAlert()
        RobotAsserts.should_be_true(user_registration_alert.is_btn_sign_in_is_present(), "Button SIGN IN isn't present"
                                                                                         "for user registration alert")

    @staticmethod
    def close_user_registration_alert():
        UserRegistrationAlert().click_ok()

    @staticmethod
    def check_that_btn_favorite_present_for_product_screen():
        RobotAsserts.should_be_true(ProductWithDiscountScreen().is_btn_favorite_present(),
                                    "Button FAVORITE isn't present for product screen")

    @staticmethod
    def click_back_from_product_info_screen():
        ProductWithDiscountScreen().click_btn_back()

    @staticmethod
    def click_to_category_with_name(data_path_string):
        category_name = DataReader().read_env_test_data(data_path_string)
        StartScreen().click_to_category_with_name(category_name)

    @staticmethod
    def check_that_opened_category_screen_is_correct(data_path_string):
        category_name = DataReader().read_env_test_data(data_path_string)
        category_screen = CategoryScreen()
        RobotAsserts.should_be_true(category_screen.is_button_search_present(),
                                    "Button SEARCH isn't present for category screen")
        RobotAsserts.should_be_true(category_screen.is_category_title_with_name_present(category_name),
                                    "Title isn't present for category {category_name}".format(
                                        category_name=category_name))
