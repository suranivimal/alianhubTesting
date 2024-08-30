import time
import uuid
import allure
import pytest
from pageObjects.CreateProject import CreateProject
from pageObjects.LoginPage import LoginPage
from utilities.readProperities import ReadConfig
from utilities.customlogger import LogGen
from utilities.commom_utils import capture_screenshot


def generate_project_name(base_name="Test Project"):
    unique_id = uuid.uuid4().hex[:8]  # Generate a unique identifier
    return f"{base_name} {unique_id}"


class Test_CreateProject:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    projectname = ReadConfig.getProjectName()
    logger = LogGen.loggen()

    @allure.epic("Alian Hub Create Project Test")
    @allure.feature("TC#01 - Alian Hub Positive Test")
    @pytest.mark.positive
    def test_CreateProject(self, setup):
        self.logger.info("***** Testing Create Project *****")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.login_page.setUserName(self.username)
        self.login_page.setPassword(self.password)
        self.login_page.clickOnLogin()
        time.sleep(20)
        self.projectname = generate_project_name()
        self.create_project = CreateProject(self.driver)
        self.create_project.clickOnMenuLink()
        time.sleep(50)
        self.create_project.clickOnNewProject()
        time.sleep(20)
        self.create_project.clickOnBlankProject()
        time.sleep(20)
        print("**************** Step 1 Project Type Blank or Use a Template ****************")
        self.create_project.setProjectName(self.projectname)
        time.sleep(20)
        self.create_project.clickOnCategory()
        time.sleep(20)
        self.create_project.selectCategory()
        time.sleep(20)
        self.create_project.clickOnNextButton()
        time.sleep(20)
        print("**************** Step 2 Project Detail ****************")
        self.create_project.clickOnNextButton()
        time.sleep(20)
        print("**************** Step 3 Project Avatar OR Color ****************")
        self.create_project.clickOnNextButton()
        time.sleep(20)
        print("**************** Step 4 Project Type Public or Private ****************")
        self.create_project.clickOnNextButton()
        time.sleep(20)
        print("**************** Step 5 Task Type ****************")
        self.create_project.clickOnNextButton()
        time.sleep(20)
        print("**************** Step 6 Project Status ****************")
        self.create_project.clickOnNextButton()
        time.sleep(20)
        print("**************** Step 7 Task Status ****************")
        self.create_project.clickOnNextButton()
        time.sleep(20)
        print("**************** Step 8 Alian App ****************")
        self.create_project.clickOnNextButton()
        time.sleep(20)
        print("**************** Step 9 View ****************")
        self.create_project.clickOnCreateProject()
        self.driver.refresh()
        print("Step 10: Create Project Completed")
        time.sleep(50)

        # Verify the project name
        created_project_name = self.create_project.get_created_project_name()
        print(created_project_name)
        if created_project_name.__eq__(self.projectname):
            self.logger.info("Project name verification passed.")
            allure.attach(self.driver.get_screenshot_as_png(), name='project_creation_pass')
            assert True
        else:
            self.logger.error(
                f"Project name verification failed. Expected: {self.projectname}, Found: {created_project_name}")
            allure.attach(self.driver.get_screenshot_as_png(), name='project_creation_Fail')
            capture_screenshot(self.driver, "test_create_project_name_verification")
            assert False
