from selenium.webdriver.common.by import By
from utilities.commom_utils import *


class CreateTask:
    task_btn_id = "createtask_driver"
    task_input = "//input[@id='inputId']"
    task_save_btn = "//button[normalize-space()='Save']"
    task_name_xpath = "//span[@class='text-ellipsis d-inline-block edit__taskname' and @title='Task 1025']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnTask(self):
        locator = (By.ID, "createtask_driver")
        webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=locator, timeout=60)
        self.driver.find_element(*locator).click()

    def setTaskName(self, task_name):
        self.driver.find_element(By.XPATH, self.task_input).clear()
        self.driver.find_element(By.XPATH, self.task_input).send_keys(task_name)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.task_save_btn).click()

    def verify_task_toast_message(self):
        toast_locator = (
            By.XPATH, "//div[contains(@class, 'v-toast__item') and contains(@class, 'v-toast__item--success')]")
        webdriver_wait_for_visibility_of_element_located(driver=self.driver, element_tuple=toast_locator, timeout=60)
        toast_element = self.driver.find_element(*toast_locator)
        return toast_element.text

    def verify_task_name(self, task_name):
        locator = (By.XPATH, f"//span[@class='text-ellipsis d-inline-block edit__taskname' and @title='{task_name}']")
        webdriver_wait_for_visibility_of_element_located(driver=self.driver, element_tuple=locator, timeout=60)
        task_name_element = self.driver.find_element(*locator)
        return task_name_element.text
