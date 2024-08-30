import time

from selenium.webdriver.common.by import By

from utilities.commom_utils import webdriver_wait


class CreateTask:
    task_btn_id = "createtask_driver"
    task_input = "//input[@id='inputId']"
    task_save_btn = "//button[normalize-space()='Save']"
    task_name_xpath = "//span[@class='text-ellipsis d-inline-block edit__taskname' and @title='Task 123']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnTask(self):
        self.driver.find_element(By.ID, self.task_btn_id).click()

    def setTaskName(self, taskname):
        self.driver.find_element(By.XPATH, self.task_input).clear()
        self.driver.find_element(By.XPATH, self.task_input).send_keys(taskname)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.task_save_btn).click()

    def verify_task_name(self):
        time.sleep(50)
        task_name_element = self.driver.find_element(By.XPATH, self.task_name_xpath)
        return task_name_element.text
