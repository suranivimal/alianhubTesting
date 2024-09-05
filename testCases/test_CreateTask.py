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
    @pytest.mark.regression
    def test_create_task(self, setup):
        self.logger.info("***** Testing Create Task *****")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        # Login
        self.login_page = LoginPage(self.driver)
        self.login_page.setUserName(self.username)
        self.login_page.setPassword(self.password)
        self.login_page.clickOnLogin()
        self.login_page.wait_for_home_page()

        # Select Project
        self.create_project = CreateProject(self.driver)
        self.create_project.clickOnMenuLink()
        self.create_project.wait_for_projects_element()

        self.create_project.select_created_project()
        # self.login_page.wait_for_home_page()
        # assert self.driver.title == "Alian Hub | Home"

        create_project = CreateProject(self.driver)
        create_project.clickOnMenuLink()
        assert self.driver.title == "Alian Hub | Projects"

        # Create Task
        create_task = CreateTask(self.driver)
        create_task.clickOnTask()
        create_task.setTaskName("Test Task 101")
        create_task.clickOnSave()
        create_task.verify_task_toast_message()

        # Refresh to ensure task is created
        self.driver.refresh()

        # Verify task creation
        task_name = create_task.verify_task_name()
        print(task_name)
        # assert task_name == "Test Task 101", f"Expected task name 'Test Task 101' but got '{task_name}'"

        if task_name == "Test Task 101":
            self.logger.info("Task name verification passed.")
            allure.attach(self.driver.get_screenshot_as_png(), name='test_create_task_name_verification_passed')
        else:
            self.logger.error(f"Task name verification failed. Expected: 'Test Task 101', but got: '{task_name}'")
            capture_screenshot(self.driver, "test_create_task_name_verification_failed")
            assert False, f"Expected task name 'Test Task 101' but got '{task_name}'"





