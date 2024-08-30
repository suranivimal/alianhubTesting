import time
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

        login_page = LoginPage(self.driver)
        login_page.setUserName(self.username)
        login_page.setPassword(self.password)
        login_page.clickOnLogin()

        time.sleep(5)
        actual_title = self.driver.title

        if actual_title == 'Alian Hub | Home':
            allure.attach(self.driver.get_screenshot_as_png(), name='test_login_with_valid_credentials_Pass')
            assert True
        else:
            self.logger.error("Login with valid credentials failed.")
            capture_screenshot(self.driver, "test_login_with_valid_credentials_Fail")
            assert False

    @allure.epic("Alian Hub Login Test")
    @allure.feature("TC#02 - Alian Hub Negative Test")
    @pytest.mark.negative
    def test_login_with_invalid_credentials(self, setup):
        self.logger.info("Testing Login with Invalid Credentials")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        login_page = LoginPage(self.driver)
        login_page.setUserName(self.invalid_email)
        login_page.setPassword(self.invalid_password)
        login_page.clickOnLogin()

        expected_warning_message = "Invalid username or password."

        if LoginPage.retrieve_warning_message.__eq__(expected_warning_message):
            allure.attach(self.driver.get_screenshot_as_png(), name='test_login_with_invalid_credentials_Pass')
            assert True
        else:
            self.logger.error("Login with invalid credentials did not show expected warning.")
            allure.attach(self.driver.get_screenshot_as_png(), name='test_login_with_invalid_credentials_Fail')
            capture_screenshot(self.driver, "test_login_with_invalid_credentials")
            assert False

    @allure.epic("Alian Hub Login Test")
    @allure.feature("TC#03 - Alian Hub Positive Test")
    @pytest.mark.positive
    def test_homePageTitle(self, setup):
        self.logger.info("Testing Homepage Title")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # Use implicit wait for better performance

        actual_title = self.driver.title

        if actual_title == 'Alian Hub | Login':
            allure.attach(self.driver.get_screenshot_as_png(), name='test_homePageTitle_Pass')
            assert True
        else:
            self.logger.error("Homepage title does not match expected value.")
            allure.attach(self.driver.get_screenshot_as_png(), name='test_homePageTitle_Fail')
            capture_screenshot(self.driver, "test_homePageTitle")
            assert False
