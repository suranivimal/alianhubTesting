import time
import uuid

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

        try:

            # Login
            self.login_page = LoginPage(self.driver)
            self.login_page.setUserName(self.username)
            self.login_page.setPassword(self.password)
            self.login_page.clickOnLogin()
            self.login_page.wait_for_home_page()
            self.logger.info("Logged in successfully.")

            # Navigate to Project and Task sections
            self.create_project = CreateProject(self.driver)
            self.create_project.clickOnMenuLink()
            self.create_project.wait_for_projects_element()
            self.logger.info("Navigated to the Projects section.")


            self.create_project.select_created_project()
            self.logger.info(f"Selected project: {self.projectname}")

            # self.login_page.wait_for_home_page()
            # assert self.driver.title == "Alian Hub | Home"

            # Verify navigation
            create_project = CreateProject(self.driver)
            create_project.clickOnMenuLink()
            assert self.driver.title == "Alian Hub | Projects", f"Unexpected title: {self.driver.title}"
            self.logger.info("Project page title verified.")

            create_task = CreateTask(self.driver)
            create_task.clickOnTask()

            task_name = f"Task_{uuid.uuid4().hex[:6]}"  # Dynamic task name
            create_task.setTaskName(task_name)

            create_task.clickOnSave()
            create_task.verify_task_toast_message()
            self.logger.info(f"Task '{task_name}' created successfully.")

            self.driver.refresh()

            # Verify task creation
            verified_task_name = create_task.verify_task_name(task_name)
            self.logger.info(f"Verified task name: {verified_task_name}")
            assert verified_task_name == task_name, f"Expected task name '{task_name}' but got '{verified_task_name}'"

        except Exception as e:
            self.logger.error(f"Test failed: {str(e)}")
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot",attachment_type=allure.attachment_type.PNG)
            raise e

        # Select the task and change status
        # create_task.click_task_name()
        # time.sleep(15)
        # create_task.change_task_status()
        # time.sleep(15)
