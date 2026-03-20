from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)
driver.maximize_window()

driver.get("https://www.saucedemo.com/")

wait = WebDriverWait(driver, 10)

username = wait.until(
    EC.visibility_of_element_located((By.ID, "user-name"))
)
username.send_keys("standard_user")


password = wait.until(
    EC.visibility_of_element_located((By.ID, "password"))
)
password.send_keys("secret_sauce")


login_btn = wait.until(
    EC.element_to_be_clickable((By.ID, "login-button"))
)
login_btn.click()

wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
)

driver.quit()