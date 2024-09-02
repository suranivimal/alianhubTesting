import time

import allure
import pytest
from pageObjects.CreateProject import CreateProject
from pageObjects.CreateTask import CreateTask
from pageObjects.LoginPage import LoginPage
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
        self.login_page.wait_for_home_page()

        self.create_project = CreateProject(self.driver)
        self.create_project.clickOnMenuLink()
        self.create_project.wait_for_projects_element()

        self.create_project.select_created_project()
        # self.login_page.wait_for_home_page()
        # assert self.driver.title == "Alian Hub | Home"

        create_project = CreateProject(self.driver)
        create_project.clickOnMenuLink()
        assert self.driver.title == "Alian Hub | Projects"

        create_task = CreateTask(self.driver)
        create_task.clickOnTask()
        # time.sleep(25)
        create_task.setTaskName("Test Task 101")
        # time.sleep(25)
        create_task.clickOnSave()
        create_task.verify_task_toast_message()
        self.driver.refresh()

        # Verify task creation
        task_name = create_task.verify_task_name()
        print(task_name)
        assert task_name == "Test Task 101", f"Expected task name 'Test Task 101' but got '{task_name}'"

        # Select the task and change status
        # create_task.click_task_name()
        # time.sleep(15)
        # create_task.change_task_status()
        # time.sleep(15)
