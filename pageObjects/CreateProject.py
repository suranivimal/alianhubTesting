from selenium.webdriver.common.by import By
from utilities.commom_utils import *


class CreateProject:
    link_menu_tab_projects = "//a[normalize-space()='Projects']"
    button_newproject = "(//button[normalize-space()='+ New Project'])[1]"
    button_blank_project = "//div[@id='createblankproject_driver']//button[@type='button']"
    textbox_project_name = "//input[@placeholder='Enter Project Name']"
    dropdown_category = "//div[@id='createprojectcategory_driver']//input[@id='inputId']"
    dropdown_value_hourly_price = "//span[normalize-space()='Hourly Price']"
    button_next = "//button[normalize-space()='Next']"
    button_create_project = "//button[@id='createprojectbtn_driver']"
    projects_element = "//div/span[@class='project-list-title']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnMenuLink(self):
        locator = (By.XPATH, self.link_menu_tab_projects)
        webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=locator, timeout=60)
        self.driver.find_element(*locator).click()

    def wait_for_projects_element(self):
        locator = (By.XPATH, self.projects_element)
        webdriver_wait_for_text_in_element(driver=self.driver, locator=locator, text="Projects", timeout=60)

    def get_error_message(self):
        webdriver_wait_for_visibility_of_element_located(driver=self.driver, element_tuple=self.link_menu_tab_projects)
        return self.driver.find_element(*CreateProject.error_message)

    def clickOnNewProject(self):
        self.driver.find_element(By.XPATH, self.button_newproject).click()

    def clickOnBlankProject(self):
        locator = (By.CSS_SELECTOR, ".font-size-18.font-weight-700.blue")
        webdriver_wait_for_text_in_element(driver=self.driver, locator=locator, text="Create Project", timeout=60)
        self.driver.find_element(By.XPATH, self.button_blank_project).click()

    def setProjectName(self, projectname):
        self.driver.find_element(By.XPATH, self.textbox_project_name).clear()
        self.driver.find_element(By.XPATH, self.textbox_project_name).send_keys(projectname)

    def clickOnCategory(self):
        locator = (By.XPATH, "//div[@id='createprojectcategory_driver']//input[@id='inputId']")
        webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=locator, timeout=60)
        self.driver.find_element(*locator).click()

    def selectCategory(self):
        locator = (By.XPATH,
                   "//div[@class='assignee-headtitle d-block text-ellipsis text-nowrap'][normalize-space()='Category List']")
        webdriver_wait_for_text_in_element(driver=self.driver, locator=locator, text="Category List", timeout=60)
        self.driver.find_element(By.XPATH, self.dropdown_value_hourly_price).click()

    def clickOnNextButton(self):
        locator = (By.XPATH, '//button[text()="Next"]')
        webdriver_wait_for_text_in_element(driver=self.driver, locator=locator, text="Next", timeout=60)
        self.driver.find_element(*locator).click()

    def clickOnCreateProject(self):
        # locator = (By.XPATH,"(//button[normalize-space()='Create Project'])[1]")
        # webdriver_wait_for_visibility_of_element_located(driver=self.driver,element_tuple=locator,timeout=60)
        # self.driver.find_element(*locator).click()
        self.driver.find_element(By.XPATH, self.button_create_project).click()

    def verify_project_toast_message(self):
        toast_locator = (
            By.XPATH, "//div[contains(@class, 'v-toast__item') and contains(@class, 'v-toast__item--success')]")
        webdriver_wait_for_visibility_of_element_located(driver=self.driver, element_tuple=toast_locator, timeout=80)
        toast_element = self.driver.find_element(*toast_locator)
        return toast_element.text

    def get_created_project_name(self):
        project_name_locator = (By.XPATH,
                                "//span[@class='text-ellipsis project-sb-ptitle font-size-13 font-weight-500 mw-80']")  # Replace with the actual locator
        webdriver_wait_for_visibility_of_element_located(driver=self.driver, element_tuple=project_name_locator,
                                                         timeout=60)
        project_name_element = self.driver.find_element(*project_name_locator)
        return project_name_element.text

    def select_created_project(self):
        locator = (By.XPATH, "//span[@class='text-ellipsis project-sb-ptitle font-size-13 font-weight-500 mw-80']")
        webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=locator, timeout=60)
        project_element = self.driver.find_element(*locator)
        project_element.click()
