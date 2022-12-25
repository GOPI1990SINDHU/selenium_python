from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By


service_obj = Service("C:\\Users\\CHUKKAPALLI GOPI\\Documents\\Python Scripts\\SeleniumChromedriver\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options,service=service_obj)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
radio_buttons = driver.find_elements(By.XPATH,"//input[@type='radio']")

for radio_button in radio_buttons:
    if radio_button.get_attribute("value") == "radio2":
        radio_button.click()
        assert radio_button.is_selected()
        break