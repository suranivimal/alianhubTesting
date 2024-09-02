import time
import uuid
import allure
import pytest
from pageObjects.CreateProject import CreateProject
from pageObjects.LoginPage import LoginPage
from utilities.readProperities import ReadConfig
from utilities.customlogger import LogGen
from utilities.commom_utils import capture_screenshot


def generate_project_name(base_name="Project"):
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
    def test_create_project_with_required_field(self, setup):
        self.logger.info("***** Testing Create Project with required fields only*****")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        login_page = LoginPage(self.driver)
        login_page.setUserName(self.username)
        login_page.setPassword(self.password)
        login_page.clickOnLogin()
        login_page.wait_for_home_page()
        create_project = CreateProject(self.driver)
        create_project.clickOnMenuLink()
        create_project.wait_for_projects_element()
        create_project.clickOnNewProject()
        create_project.clickOnBlankProject()
        self.projectname = generate_project_name()
        self.logger.info("Step-1 : Project Type - Blank Project or Use a Template")
        create_project.setProjectName(self.projectname)
        create_project.clickOnCategory()
        create_project.selectCategory()
        create_project.clickOnNextButton()
        self.logger.info("Step-2 : Project Detail")
        create_project.clickOnNextButton()
        self.logger.info("Step-3 : Project Avatar or Project Color")
        create_project.clickOnNextButton()
        self.logger.info("Step-4 : Project Type - Public Project or Private Project")
        create_project.clickOnNextButton()
        self.logger.info("Step-5 : Task Type - Add the type of tasks you need")
        create_project.clickOnNextButton()
        self.logger.info("Step-6 : Project Status - Add the statuses for the project")
        create_project.clickOnNextButton()
        self.logger.info("Step-7 : Task Status - Set up the statuses for tasks")
        create_project.clickOnNextButton()
        self.logger.info("Step-8 : Enable Apps - Priority,Multiple Assignees,Time Estimate,Milestones,Tags,Custom Fields,Time Tracking And AI")
        create_project.clickOnNextButton()
        self.logger.info("Step-9 : Enable views - List,Board,Project Details,Comments,Calendar,Activity,Workload And Table")
        time.sleep(20)
        create_project.clickOnCreateProject()
        self.logger.info("Step-10 : Project Summary - Details of the Project set up")
        create_project.verify_project_toast_message()
        time.sleep(60)

        # Verify the project name
        created_project_name = create_project.get_created_project_name()
        print(created_project_name)
        if created_project_name.__eq__(self.projectname):
            self.logger.info("Project name verification testcase passed")
            allure.attach(self.driver.get_screenshot_as_png(), name='test_create_project_name_verification_passed')
            assert True
        else:
            self.logger.error(
                f"Project name verification testcase failed. Expected: {self.projectname}, Found: {created_project_name}")
            capture_screenshot(self.driver, "test_create_project_name_verification_failed")
            assert False
