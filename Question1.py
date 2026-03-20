from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)

driver.get("https://www.prokabaddi.com/")

driver.maximize_window()

driver.implicitly_wait(10)

driver.find_element(By.XPATH,"//a[@href='https://www.prokabaddi.com/standings']").click()

MatchPlay = driver.find_element(By.XPATH,'//p[contains(text(),"Jaipur Pink Panthers")]/../../../..//div[@class="table-data matches-play"]//p').text
print("Matches Played : ", MatchPlay)

MatchWon = driver.find_element(By.XPATH,'//p[contains(text(),"Jaipur Pink Panthers")]/../../../..//div[@class="table-data matches-won"]//p').text
print("Matches Won : ", MatchWon)

MatchLoss = driver.find_element(By.XPATH,'//p[contains(text(),"Jaipur Pink Panthers")]/../../../..//div[@class="table-data matches-lost"]//p').text
print("Matches Lost : ", MatchLoss)

MatchDiff = driver.find_element(By.XPATH,'//p[contains(text(),"Jaipur Pink Panthers")]/../../../..//div[@class="table-data score-diff"]//p').text
print("Score Diff : ", MatchDiff)

points = driver.find_element(By.XPATH,'//p[contains(text(),"Jaipur Pink Panthers")]/../../../..//div[@class="table-data points"]//p').text
print("Table Points : ", points)

driver.quit()