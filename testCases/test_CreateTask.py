import time

import allure
import pytest
from pageObjects.CreateProject import CreateProject
from pageObjects.CreateTask import CreateTask
from pageObjects.LoginPage import LoginPage
from utilities.commom_utils import capture_screenshot
from utilities.customlogger import LogGen
from utilities.readProperities import ReadConfig


class Test_CreateTask:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    projectname = ReadConfig.getProjectName()
    logger = LogGen.loggen()

    @allure.epic("Alian Hub Create Task Test")
    @allure.feature("TC#01 - Alian Hub Positive Test")
    @pytest.mark.positive
    def test_create_task(self, setup):
        self.logger.info("***** Testing Create Task *****")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.login_page.setUserName(self.username)
        self.login_page.setPassword(self.password)
        self.login_page.clickOnLogin()
        time.sleep(30)
        self.create_project = CreateProject(self.driver)
        time.sleep(30)
        self.create_project.clickOnMenuLink()
        time.sleep(60)

        self.create_project.select_created_project(self.projectname)
        self.login_page.wait_for_home_page()
        assert self.driver.title == "Alian Hub | Home"
        time.sleep(60)

        create_project = CreateProject(self.driver)
        create_project.clickOnMenuLink()
        assert self.driver.title == "Alian Hub | Projects"

        create_task = CreateTask(self.driver)
        create_task.clickOnTask()
        time.sleep(30)
        create_task.setTaskName("Task 123")
        time.sleep(30)
        create_task.clickOnSave()
        self.driver.refresh()
        time.sleep(60)

        # Verify task creation
        task_name = create_task.verify_task_name()
        print(task_name)
        # assert task_name == "Task 123", f"Expected task name 'Task 123' but got '{task_name}'"

        if task_name == "Task 123":
            self.logger.info("Create Task Successfully .")
            allure.attach(self.driver.get_screenshot_as_png(), name='create_task_pass')
            assert True
        else:
            self.logger.error(
                f"Task 123", f"Expected task name 'Task 123' but got '{task_name}")
            allure.attach(self.driver.get_screenshot_as_png(), name='create_task_fail')
            capture_screenshot(self.driver, "create_task_fail")
            assert False

        # Select the task and change status
        # create_task.click_task_name()
        # time.sleep(15)
        # create_task.change_task_status()
        # time.sleep(15)
