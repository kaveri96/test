from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\drivers1\chromedriver_win32\chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")

print("kaveri")
driver.maximize_window()

element = driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")

actions = ActionChains(driver)
print("kaveri")
actions.double_click(element).perform()
print("kaveri")
print("kaveri")
