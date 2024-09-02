import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def webdriver_wait_for_title_is(driver, element_title, timeout=60):
    WebDriverWait(driver, timeout).until(EC.title_is(element_title))


def webdriver_wait_for_title_contains(driver, element_title, timeout=50):
    WebDriverWait(driver, timeout=timeout).until(EC.title_contains(element_title))


def webdriver_for_presence_of_element_located(driver, locator, timeout=60):
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))


def webdriver_wait_for_visibility_of_element_located(driver, element_tuple, timeout=50):
    WebDriverWait(driver, timeout=timeout).until(EC.visibility_of_element_located(element_tuple))


def webdriver_wait_for_visibility_of(driver, element, timeout=60):
    WebDriverWait(driver, timeout).until(EC.visibility_of(element))


def webdriver_wait_for_presence_of_all_elements_located(driver, locator, timeout=60):
    WebDriverWait(driver, timeout).until(EC.presence_of_all_elements_located(locator))


def webdriver_wait_for_text_in_element(driver, locator, text, timeout=60):
    WebDriverWait(driver, timeout).until(EC.text_to_be_present_in_element(locator, text))


def webdriver_wait_for_text_in_element_value(driver, locator, text, timeout=60):
    WebDriverWait(driver, timeout).until(EC.text_to_be_present_in_element_value(locator, text))


def webdriver_wait_for_frame_and_switch(driver, locator, timeout=60):
    WebDriverWait(driver, timeout).until(EC.frame_to_be_available_and_switch_to_it(locator))


def webdriver_wait_for_invisibility_of_element_located(driver, locator, timeout=60):
    WebDriverWait(driver, timeout).until(EC.invisibility_of_element_located(locator))


def webdriver_wait_for_element_to_be_clickable(driver, locator, timeout=60):
    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))


def webdriver_wait_for_staleness_of(driver, element, timeout=60):
    WebDriverWait(driver, timeout).until(EC.staleness_of(element))


def webdriver_wait_for_element_to_be_selected(driver, element, timeout=60):
    WebDriverWait(driver, timeout).until(EC.element_to_be_selected(element))


def webdriver_wait_for_element_selection_state_to_be(driver, element, state, timeout=60):
    WebDriverWait(driver, timeout).until(EC.element_selection_state_to_be(element, state))


def webdriver_wait_for_element_located_selection_state_to_be(driver, locator, state, timeout=60):
    WebDriverWait(driver, timeout).until(EC.element_located_selection_state_to_be(locator, state))


def webdriver_wait_for_alert_is_present(driver, timeout=60):
    WebDriverWait(driver, timeout).until(EC.alert_is_present())


def capture_screenshot(driver, screenshot_name):
    screenshot_path = f"C:/Users/Alian Testing/PycharmProjects/alianhubTesting/Screenshots/{screenshot_name}.png"
    driver.save_screenshot(screenshot_path)
    allure.attach(driver.get_screenshot_as_png(), name=screenshot_name)
