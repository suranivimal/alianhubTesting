import pytest
import allure
from pageObjects.LoginPage import LoginPage
from utilities.readProperities import ReadConfig
from utilities.customlogger import LogGen
from utilities.commom_utils import capture_screenshot


class Test_LoginPage:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    invalid_email = ReadConfig.getInvalidUserEmail()
    invalid_password = ReadConfig.getInvalidPassword()
    logger = LogGen.loggen()

    @allure.epic("Alian Hub Login Test")
    @allure.feature("TC#01 - Alian Hub Positive Test")
    @pytest.mark.positive
    def test_login_with_valid_credentials(self, setup):
        self.logger.info("Testing Login with Valid Credentials")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        try:

            login_page = LoginPage(self.driver)
            login_page.setUserName(self.username)
            login_page.setPassword(self.password)
            login_page.clickOnLogin()

            login_page.wait_for_home_page()
            actual_title = self.driver.title

            assert actual_title == 'Alian Hub | Home', f"Expected title 'Alian Hub | Home' but got '{actual_title}'"
            allure.attach(self.driver.get_screenshot_as_png(), name='test_login_with_valid_credentials_passed')
            self.logger.info("Login with valid credentials passed.")

        except Exception as e:
            self.logger.error(f"An error occurred during login with valid credentials: {str(e)}")
            capture_screenshot(self.driver, "test_login_with_valid_credentials_failed")
            assert False, f"Test failed due to {str(e)}"

    @allure.epic("Alian Hub Login Test")
    @allure.feature("TC#02 - Alian Hub Negative Test")
    @pytest.mark.negative
    def test_login_with_invalid_credentials(self, setup):
        self.logger.info("Testing Login with Invalid Credentials")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        try:

            login_page = LoginPage(self.driver)
            login_page.setUserName(self.invalid_email)
            login_page.setPassword(self.invalid_password)
            login_page.clickOnLogin()

            expected_warning_message = "Invalid username or password."
            actual_warning_message = login_page.retrieve_warning_message()

            assert actual_warning_message == expected_warning_message, (
                f"Expected warning message '{expected_warning_message}' but got '{actual_warning_message}'"
            )
            allure.attach(self.driver.get_screenshot_as_png(), name='test_login_with_invalid_credentials_passed')
            self.logger.info("Login with invalid credentials passed.")

        except Exception as e:
            self.logger.error(f"An error occurred during login with invalid credentials: {str(e)}")
            capture_screenshot(self.driver, "test_login_with_invalid_credentials_failed")
            assert False, f"Test failed due to {str(e)}"

    @allure.epic("Alian Hub Login Test")
    @allure.feature("TC#03 - Alian Hub Positive Test")
    @pytest.mark.positive
    def test_home_page_title(self, setup):
        self.logger.info("Testing Homepage Title")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        try:
            actual_title = self.driver.title

            assert actual_title == 'Alian Hub | Login', f"Expected title 'Alian Hub | Login' but got '{actual_title}'"
            allure.attach(self.driver.get_screenshot_as_png(), name='test_home_page_title_passed')
            self.logger.info("Homepage title verification passed.")
        except Exception as e:
            self.logger.error(f"An error occurred during homepage title verification: {str(e)}")
            capture_screenshot(self.driver, "test_home_page_title_failed")
            assert False, f"Test failed due to {str(e)}"