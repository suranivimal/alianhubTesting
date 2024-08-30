from selenium.webdriver.common.by import By

from utilities.commom_utils import webdriver_wait


class CreateProject:
    link_menu_tab_projects = "//a[normalize-space()='Projects']"
    button_newproject = "(//button[normalize-space()='+ New Project'])[1]"
    button_blank_project = "//div[@id='createblankproject_driver']//button[@type='button']"
    textbox_project_name = "//input[@placeholder='Enter Project Name']"
    dropdown_category = "//div[@id='createprojectcategory_driver']//input[@id='inputId']"
    dropdown_value_hourly_price = "//span[normalize-space()='Hourly Price']"
    button_next = "//button[normalize-space()='Next']"
    button_create_project = "//button[@id='createprojectbtn_driver']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnMenuLink(self):
        self.driver.find_element(By.XPATH, self.link_menu_tab_projects).click()

    def get_error_message(self):
        webdriver_wait(driver=self.driver, element_tuple=self.link_menu_tab_projects)
        return self.driver.find_element(*CreateProject.error_message)

    def clickOnNewProject(self):
        self.driver.find_element(By.XPATH, self.button_newproject).click()

    def clickOnBlankProject(self):
        self.driver.find_element(By.XPATH, self.button_blank_project).click()

    def setProjectName(self, projectname):
        self.driver.find_element(By.XPATH, self.textbox_project_name).clear()
        self.driver.find_element(By.XPATH, self.textbox_project_name).send_keys(projectname)

    def clickOnCategory(self):
        self.driver.find_element(By.XPATH, self.dropdown_category).click()

    def selectCategory(self):
        self.driver.find_element(By.XPATH, self.dropdown_value_hourly_price).click()

    def clickOnNextButton(self):
        self.driver.find_element(By.XPATH, self.button_next).click()

    def clickOnCreateProject(self):
        self.driver.find_element(By.XPATH, self.button_create_project).click()

    project_name_locator = (By.XPATH,
                            "//span[@class='text-ellipsis project-sb-ptitle font-size-13 font-weight-500 mw-80']")  # Replace with the actual locator

    def get_created_project_name(self):
        project_name_element = self.driver.find_element(*self.project_name_locator)
        return project_name_element.text

    def select_created_project(self, project_name):
        project_element = self.driver.find_element(*self.project_name_locator)
        project_element.click()
