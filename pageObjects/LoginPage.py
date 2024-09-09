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
        webdriver_wait_for_title_contains(driver=self.driver, element_title="Alian Hub | Home", timeout=60)

    def retrieve_warning_message(self):
        # Wait for the warning message to be visible and then retrieve its text
        warning_message_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(("xpath", self.toast_message_xpath))
        )
        return warning_message_element.text
