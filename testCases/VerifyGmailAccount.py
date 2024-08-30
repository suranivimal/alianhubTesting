from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

import time

from selenium.webdriver.support.wait import WebDriverWait

# Set up WebDriver options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Optional: Maximize the browser window

# Path to the WebDriver executable
driver_path = '/path/to/chromedriver'  # Replace with the path to your WebDriver executable
driver = webdriver.Chrome(options=options)

try:
    # Navigate to Gmail login page
    driver.get("https://mail.google.com/")
    time.sleep(2)  # Allow the page to load

    # Enter email
    email_input = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
    email_input.send_keys('vimalpatel888999@gmail.com')  # Replace with your email
    email_input.send_keys(Keys.ENTER)
    time.sleep(2)  # Allow page to load

    # Enter password
    password_input = driver.find_element(By.XPATH, '//*[@name="Passwd"]')
    password_input.send_keys('Abc@223133')  # Replace with your password
    password_input.send_keys(Keys.ENTER)
    time.sleep(5)  # Allow page to load after login

    # Search for specific email based on subject
    subject_to_find = "Fwd: You are shortlisted Vims"  # Replace with the subject of the email you want to find
    search_box = driver.find_element(By.XPATH, '//*[@name="q"]')
    search_box.send_keys(subject_to_find)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)  # Allow search results to load

    # Click on the specific email based on the subject
    email_link_xpath = "//*[@id=':60']/span"
    email_link = WebDriverWait(driver, .30).until(
        EC.visibility_of_element_located((By.XPATH, email_link_xpath))
    )
    email_link.click()
    time.sleep(5)  # Wait for the email page to load

    driver.find_element(By.XPATH,"//*[@id=':5f']/div[1]/div[1]/div[2]/div/table[1]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/p[5]/a/b/u'").click()

    # Perform actions within the email if needed
    # e.g., driver.find_element(By.XPATH, '...').click() or driver.find_element(By.XPATH, '...').send_keys(...)

finally:
    # Close the browser window after done
    driver.quit()