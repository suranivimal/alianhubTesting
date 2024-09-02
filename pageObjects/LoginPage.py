from selenium.webdriver.common.by import By
from utilities.commom_utils import *


class LoginPage:
    # Login Page
    textbox_email_id = "email"
    textbox_password_id = "password"
    button_login_xpath = "//button[normalize-space()='Login']"
    toast_message_xpath = "//div[contains(@class, 'v-toast--top')]"


    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_email_id).clear()
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def setInvalidUserName(self, email):
        self.driver.find_element(By.ID, self.textbox_email_id).clear()
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(email)

    def setInvalidPassword(self, userpassword):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(userpassword)


    def clickOnLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def wait_for_home_page(self):
        webdriver_wait_for_title_contains(driver=self.driver,element_title="Alian Hub | Home",timeout=50)

    def get_element(self, locator_name, locator_value):
        element = None
        if locator_name.endswith("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_name.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_name.endswith("_class_name"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_name.endswith("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_name.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_name.endswith("css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        return element

    def retrieve_element_text(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        return element.text

    def retrieve_warning_message(self):
        return self.retrieve_element_text("toast_message_xpath", self.toast_message_xpath)
