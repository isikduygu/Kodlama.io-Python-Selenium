from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Kodlamaio:
    def test_invalid_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        # tam ekran yapar
        driver.maximize_window() 
        # ilgili adrese gider
        driver.get("https://www.saucedemo.com/")

        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(2)
        usernameInput.send_keys("1")
        passwordInput.send_keys("2")
        sleep(2)
        loginbtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginbtn.click()
        sleep(5)

        errorMessage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")

        print(errorMessage.text == "Epic sadface: Username and password do not match any user in this service")
        sleep(200)

TestClass = Kodlamaio()
TestClass.test_invalid_login()
while True:
    continue