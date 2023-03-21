from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
# tam ekran yapar
driver.maximize_window() 

# ilgili adrese gider
driver.get("https://www.google.com/")

# input alanının namei q
input = driver.find_element(By.NAME, 'q')

# input alanına kodlama io yazar
input.send_keys("kodlama.io")
sleep(5)
# namei btnk olan butona tıklar
buttonSearch = driver.find_element(By.NAME, 'btnK')
sleep(5)
buttonSearch.click()
sleep(5)
firstResult = driver.find_element(By.XPATH, '/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a')
sleep(5)
firstResult.click()
sleep(2)
# web scraping de yapılabilir. 7 tane kurs var
listofCourse = driver.find_elements(By.CLASSNAME, 'course-listing')
len(listofCourse)
while True:
    continue