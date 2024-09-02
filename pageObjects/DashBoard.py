from selenium.webdriver.common.by import By

class Dashboard:

    button_profile_xpath = "//*[@class='profile-image asignee-profile']"
    button_logout_xpath = "//span[@class='project-mobile-desc']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnProfile(self):
        self.driver.find_element(By.XPATH, self.button_profile_xpath).click()

    def clickOnLogout(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()