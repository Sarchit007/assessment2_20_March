from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from tornado.gen import sleep

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.maximize_window()
driver.get("https://www.shine.com/registration/")
sleep(3)
file_input= driver.find_element(By.XPATH, '//input[@type="file"]')
sleep(3)
file_input.send_keys(r"C:\Users\sarch\OneDrive\Desktop\week2\Archit Saxena Resume.pdf")
sleep(3)
driver.quit()