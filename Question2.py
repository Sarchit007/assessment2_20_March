from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.maximize_window()

driver.get("https://www.saucedemo.com/")

wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="user-name"]'))).send_keys("standard_user")
wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="login-button"]'))).click()

Page_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'title')))
print("Title is ",Page_title.text)

products_Name = driver.find_elements(By.XPATH, '//div[@class="inventory_list"]//div[@class="inventory_item"]//div[@class="inventory_item_description"]//div[@class="inventory_item_label"]//a//div[@class="inventory_item_name "]')
products_Price = driver.find_elements(By.XPATH, '//div[@class="inventory_list"]//div[@class="inventory_item"]//div[@class="inventory_item_description"]//div[@class="pricebar"]//div[@class="inventory_item_price"]')

for i in range(len(products_Name)):
    print(f"{products_Name[i].text} - {products_Price[i].text}")


wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="inventory_item"][4]//div[@class="inventory_item_description"]//div[@class="pricebar"]//button[text()="Add to cart"]'))).click()
