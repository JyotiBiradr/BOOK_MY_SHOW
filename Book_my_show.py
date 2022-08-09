from selenium.webdriver import Chrome
from time import sleep
driver=Chrome("./chromedriver.exe")
driver.get("https://in.bookmyshow.com/")
driver.maximize_window()
sleep(4)
driver.find_element_by_xpath("//span[text()='Bengaluru']").click()
sleep(2)
driver.find_element_by_xpath("//div[text()='Sign in']").click()
sleep(2)
driver.find_element_by_xpath("//div[@class='sc-kfGgVZ ffEUhO']").click()
driver.close()
