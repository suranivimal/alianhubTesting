import time

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from utilities.common_utils import *
import pyautogui


class CreateProject:
    """
    Page Object Model for the Create Project page in the application.
    Contains locators and methods to interact with the Create Project page.
    """

    # Locators
    btn_new_project = "(//button[normalize-space()='+ New Project'])[1]"
    # Step 1
    btn_blank_project = "//div[@id='createblankproject_driver']//button[@type='button']"
    btn_use_a_template = "(//button[@type='button'])[2]"
    # Step 2
    txt_project_name = "//input[@placeholder='Enter Project Name']"
    txt_project_key = "//div[@id='createprojectkey_driver']//input[@id='inputId']"
    dropdown_category = "//div[@id='createprojectcategory_driver']//input[@id='inputId']"
    dropdown_title_category_list = "//div[@class='assignee-headtitle d-block text-ellipsis text-nowrap'][normalize-space()='Category List']"
    option_hourly_price = "//span[normalize-space()='Hourly Price']"
    date_picker_due_date = "// input[ @ placeholder = 'Select Project Due Date']"
    lead_button = "//ul[@class='d-flex']"
    dropdown_option = "//span[normalize-space()='Member One']"
    dropdown_close_btn = "//img[@alt='closeButton']"
    # Step 3
    upload_btn = "//label[normalize-space()='Upload']"
    # Step 4
    project_type_private = "//p[text()='Private']"
    # Step 5
    task_type_plus_icon = "//img[@id='createprojecttasktype_driver']"
    task_type_template_name = "//input[@placeholder='Enter Template']"
    task_type_template_save_icon = "//span[@class='position-ab edit-rightinput save__closeimg-wrapper']//img[@class='cursor-pointer']"
    task_type_template_add_btn = "//button[@id='createprojecttasktypenew_driver']"
    task_type_template_bug = "//span[normalize-space()='Bug']"
    task_type_template_subtask = "//span[normalize-space()='Sub Task']"
    task_type_template_close_icon = "//div[@class='cursor-pointer d-flex align-items-center']//img"

    btn_next = "//button[normalize-space()='Next']"
    toggle_view_project_details = "//div[@id='my-sidebar']//div[3]//div[2]//div[2]"
    btn_create_project = "(//button[normalize-space()='Create Project'])[1]"
    project_list_title = "//div/span[@class='project-list-title']"
    project_list_fav = "//img[@id='projestleftlistfilter_driver']"
    project_name = "//span[@class='text-ellipsis project-sb-ptitle font-size-13 font-weight-500 mw-80']"
    option_template = "//div[@class='template_project_img']//img[@class='cursor-pointer']"
    btn_use_template = "//button[normalize-space()='Use Template']"
    toast_message_project = "//div[contains(@class, 'v-toast__item') and contains(@class, 'v-toast__item--success')]"

    def __init__(self, driver):
        """
        Initializes the CreateProject page object.

        :param driver: WebDriver instance to interact with the browser.
        """
        self.driver = driver

    def wait_for_project_list_title(self):
        """
        Waits for the 'Projects' title to be visible on the project list sidebar.
        """
        locator = (By.XPATH, self.project_list_title)
        try:
            webdriver_wait_for_text_in_element_value(driver=self.driver, locator=locator, text="Projects", timeout=60)
        except TimeoutException as e:
            print(f"Timeout waiting for 'Projects' title: {e}")

    def wait_for_project_list_fav(self):
        """
        Waits for the 'fav.' icon to be visible on the project list sidebar.
        """
        locator = (By.XPATH, self.project_list_fav)
        try:
            webdriver_for_presence_of_element_located(driver=self.driver, locator=locator, timeout=60)
        except TimeoutException as e:
            print(f"Timeout waiting for 'Projects' title: {e}")

    def click_on_new_project_button(self):
        """
        Clicks on the 'New Project' button to start creating a new project.
        """
        try:
            self.driver.find_element(By.XPATH, self.btn_new_project).click()
        except NoSuchElementException as e:
            print(f"Error clicking on 'New Project' button: {e}")

    def click_on_blank_project_button(self):
        """
        Clicks on the 'Blank Project' button to create a new project from scratch.
        """
        locator = (By.XPATH, self.btn_blank_project)
        try:
            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=locator, timeout=60)
            self.driver.find_element(*locator).click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error clicking on 'Blank Project' button: {e}")

    def click_on_use_a_template_button(self):
        """
        Clicks on the 'Use a Template' button to use a predefined template for the project.
        """
        locator = (By.XPATH, self.btn_use_a_template)
        try:
            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=locator, timeout=60)
            self.driver.find_element(*locator).click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error clicking on 'Use a Template' button: {e}")

    def set_project_name(self, project_name):
        """
        Sets the name of the project in the project name input field.

        :param project_name: The name to be entered into the project name field.
        """
        try:
            element = self.driver.find_element(By.XPATH, self.txt_project_name)
            element.clear()
            element.send_keys(project_name)
        except NoSuchElementException as e:
            print(f"Error setting project name: {e}")

    def set_project_key(self, project_key):
        """
        Sets the project key in the project key input field.

        :param project_key: The key to be entered into the project key field.
        """
        locator = (By.XPATH, self.txt_project_key)
        try:
            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=locator, timeout=60)
            element = self.driver.find_element(*locator)
            element.clear()
            element.send_keys(project_key)
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error setting project key: {e}")

    def click_on_category(self):
        """
        Clicks on the category dropdown to select a category for the project.
        """
        locator = (By.XPATH, self.dropdown_category)
        try:
            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=locator, timeout=60)
            self.driver.find_element(*locator).click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error clicking on category dropdown: {e}")

    def select_category(self):
        """
        Selects a category from the category dropdown.
        """
        locator = (By.XPATH, self.dropdown_title_category_list)
        try:
            webdriver_wait_for_text_in_element(driver=self.driver, locator=locator, text="Category List", timeout=60)
            self.driver.find_element(By.XPATH, self.option_hourly_price).click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error selecting category: {e}")

    def click_on_lead_dropdown(self):
        """
        Clicks on the 'Next' button to proceed to the next step in the project creation process.
        """
        locator = (By.XPATH, self.lead_button)
        try:
            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=locator, timeout=60)
            self.driver.find_element(*locator).click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error clicking on 'lead assignee' button: {e}")

    def select_assignee(self):

        locator = (By.XPATH, self.dropdown_option)
        try:
            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=locator, timeout=60)
            self.driver.find_element(*locator).click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error selecting assignee: {e}")

    def close_assignee_sidebar(self):
        locator = (By.XPATH, self.dropdown_close_btn)
        try:
            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=locator, timeout=60)
            self.driver.find_element(*locator).click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error clicking on  close button: {e}")

    def project_image_upload(self):

        upload_button = self.driver.find_element(By.XPATH, self.upload_btn)  # Adjust XPath
        upload_button.click()

        # Wait for the file picker to open
        time.sleep(2)

        # Automate the file picker using PyAutoGUI
        file_path = "C:\\Users\\Alian Testing\\Downloads\\test.png"  # Replace with the correct file path
        pyautogui.write(file_path)  # Type the file path
        pyautogui.press('enter')

    def select_project_type(self):

        locator = (By.XPATH, self.project_type_private)
        try:
            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=locator, timeout=60)
            self.driver.find_element(*locator).click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error clicking on 'project type': {e}")

    def select_task_type_template(self):

        plus_locator = (By.XPATH, self.task_type_plus_icon)
        template_name_locator = (By.XPATH, self.task_type_template_name)
        template_save_locator = (By.XPATH, self.task_type_template_save_icon)
        template_add_locator = (By.XPATH, self.task_type_template_add_btn)
        template_bug_locator = (By.XPATH, self.task_type_template_bug)
        template_subtask_locator = (By.XPATH, self.task_type_template_subtask)
        template_close_locator = (By.XPATH, self.task_type_template_close_icon)

        try:
            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=plus_locator, timeout=60)
            self.driver.find_element(*plus_locator).click()

            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=template_name_locator, timeout=60)
            self.driver.find_element(*template_name_locator).send_keys("QA")

            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=template_save_locator, timeout=60)
            self.driver.find_element(*template_save_locator).click()

            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=template_add_locator, timeout=60)
            self.driver.find_element(*template_add_locator).click()

            time.sleep(20)

            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=template_bug_locator, timeout=60)
            self.driver.find_element(*template_bug_locator).click()

            time.sleep(20)

            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=template_subtask_locator, timeout=60)
            self.driver.find_element(*template_subtask_locator).click()

            time.sleep(20)

            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=template_close_locator, timeout=60)
            self.driver.find_element(*template_close_locator).click()

            time.sleep(20)

        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error clicking on 'project type': {e}")

    def click_on_next_button(self):
        """
        Clicks on the 'Next' button to proceed to the next step in the project creation process.
        """
        locator = (By.XPATH, self.btn_next)
        try:
            webdriver_wait_for_text_in_element(driver=self.driver, locator=locator, text="Next", timeout=60)
            self.driver.find_element(*locator).click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error clicking on 'Next' button: {e}")

    def click_on_view_radio_button(self):
        """
        Clicks on the 'View' radio button in the project details section.
        """
        locator = (By.XPATH, self.toggle_view_project_details)
        try:
            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=locator, timeout=60)
            self.driver.find_element(*locator).click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error clicking on 'View' radio button: {e}")

    def select_templates(self):
        """
        Selects a template from the available templates.
        """
        locator = (By.XPATH, self.option_template)
        webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=locator, timeout=60)
        self.driver.find_element(*locator).click()

    def click_on_use_template_button(self):
        """
        Clicks on the 'Use Template' button to proceed to the next step in the project creation process.
        """
        locator = (By.XPATH, self.btn_use_template)
        try:
            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=locator, timeout=60)
            self.driver.find_element(*locator).click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error clicking on 'Use Template' button: {e}")

    def click_on_create_project(self):
        """
        Clicks on the 'Create Project' button to finalize and create the new project.
        """
        locator = (By.XPATH, self.btn_create_project)
        try:
            webdriver_wait_for_visibility_of_element_located(driver=self.driver, element_tuple=locator, timeout=60)
            self.driver.find_element(*locator).click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error clicking on 'Create Project' button: {e}")

    def verify_project_toast_message(self):
        """
        Verifies that the success toast message is displayed after project creation.

        :return: The text of the toast message.
        """
        toast_locator = (By.XPATH, self.toast_message_project)
        try:
            webdriver_wait_for_visibility_of_element_located(driver=self.driver, element_tuple=toast_locator,
                                                             timeout=80)
            toast_element = self.driver.find_element(*toast_locator)
            return toast_element.text
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error verifying project toast message: {e}")
            return None

    def get_created_project_name(self):
        """
        Retrieves the name of the newly created project from the project list.

        :return: The name of the created project.
        """
        project_name_locator = (By.XPATH, self.project_name)
        try:
            webdriver_wait_for_visibility_of_element_located(driver=self.driver, element_tuple=project_name_locator,
                                                             timeout=60)
            project_name_element = self.driver.find_element(*project_name_locator)
            return project_name_element.text
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error getting created project name: {e}")
            return None

    def select_created_project(self):
        """
        Clicks on the created project from the project list to open it.

        :return: The WebElement of the created project.
        """
        locator = (By.XPATH, self.project_name)
        try:
            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=locator, timeout=60)
            project_element = self.driver.find_element(*locator)
            project_element.click()
            return project_element
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error selecting created project: {e}")
            return None

    def click_on_due_date(self):
        locator = (By.XPATH, self.date_picker_due_date)
        try:
            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=locator, timeout=60)
            self.driver.find_element(*locator).click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error clicking on 'Use Template' button: {e}")

    def calendar_component(self):

        locator = (By.XPATH, self.date_picker_due_date)
        webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=locator, timeout=60)
        self.driver.find_element(*locator).click()

        cel_locator = (By.CLASS_NAME, "dp__instance_calendar")
        webdriver_wait_for_visibility_of_element_located(driver=self.driver, element_tuple=cel_locator, timeout=60)

        # Interact with the calendar

        next_button = self.driver.find_element(By.XPATH, "//button[@aria-label='Next month']")
        next_button.click()

        # Example: Select a specific date (30th)
        date_button = self.driver.find_element(By.XPATH,
                                               "//div[contains(@class, 'dp__calendar_item') and .//div[text()='30']]")
        date_button.click()
