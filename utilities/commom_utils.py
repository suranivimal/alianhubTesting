import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def webdriver_wait(driver, element_tuple):
    WebDriverWait(driver=driver, timeout=25).until(
        EC.visibility_of_element_located(element_tuple))


def webdriver_wait(driver, element_tuple, timeout):
    WebDriverWait(driver=driver, timeout=timeout).until(
        EC.visibility_of_element_located(element_tuple))


def webdriver_wait(driver, element_title, timeout=50):
    WebDriverWait(driver, timeout).until(EC.title_contains(element_title))


def capture_screenshot(driver, screenshot_name):
    """Utility to capture and attach a screenshot."""
    screenshot_path = f"C:/Users/Alian Testing/PycharmProjects/alianhubTesting/Screenshots/{screenshot_name}.png"
    driver.save_screenshot(screenshot_path)
    allure.attach(driver.get_screenshot_as_png(), name=screenshot_name)
