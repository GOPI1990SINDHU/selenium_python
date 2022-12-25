from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By


service_obj = Service("C:\\Users\\CHUKKAPALLI GOPI\\Documents\\Python Scripts\\SeleniumChromedriver\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options,service=service_obj)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
check_boxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")

for checkbox in check_boxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        break