from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Test_Homework:
    def test_username_password(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        # tam ekran yapar
        driver.maximize_window() 
        # ilgili adrese gider
        driver.get("https://www.saucedemo.com/")

        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(2)
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        sleep(2)
        loginbtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginbtn.click()
        sleep(5)

        errorMessage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")

        print(errorMessage.text == "Epic sadface: Username is required")
        sleep(200)

    def test_password(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        # tam ekran yapar
        driver.maximize_window() 
        # ilgili adrese gider
        driver.get("https://www.saucedemo.com/")

        passwordInput = driver.find_element(By.ID, "password")
        sleep(2)
        passwordInput.send_keys("")
        sleep(2)
        loginbtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginbtn.click()
        sleep(5)

        errorMessage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")

        print(errorMessage.text == "Epic sadface: Password is required")
        sleep(200)

    def test_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        # tam ekran yapar
        driver.maximize_window() 
        # ilgili adrese gider
        driver.get("https://www.saucedemo.com/")

        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(2)
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginbtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginbtn.click()
        sleep(5)

        errorMessage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")

        print(errorMessage.text == "Epic sadface: Sorry, this user has been locked out.")
        sleep(200)

    def error_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        # tam ekran yapar
        driver.maximize_window() 
        # ilgili adrese gider
        driver.get("https://www.saucedemo.com/")
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(2)
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        sleep(2)
        loginbtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginbtn.click()
        sleep(5)
        errorButton = driver.find_element(By.CLASS_NAME,"error-button")
        errorButton.click()

    def get_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        # tam ekran yapar
        driver.maximize_window() 
        # ilgili adrese gider
        driver.get("https://www.saucedemo.com/")

        usernameInput = driver.find_element(By.ID, "standard_user")
        passwordInput = driver.find_element(By.ID, "secret_sauce")
        sleep(2)
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        sleep(2)
        loginbtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginbtn.click()
        sleep(5)
        driver.get("https://www.saucedemo.com/inventory.html")

    def list_products(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        # tam ekran yapar
        driver.maximize_window() 
        # ilgili adrese gider
        driver.get("https://www.saucedemo.com/")

        usernameInput = driver.find_element(By.ID, "standard_user")
        passwordInput = driver.find_element(By.ID, "secret_sauce")
        sleep(2)
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        sleep(2)
        loginbtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginbtn.click()
        sleep(5)
        driver.get("https://www.saucedemo.com/inventory.html")

        productList = driver.find_elements(By.CLASS_NAME, "inventory_item")
        print(f"inventory sitesinde şu anda {len(productList)} adet ürün var")
        while True:
            continue
    
TestClass = Test_Homework()
TestClass.test_username_password()
TestClass.test_password()
TestClass.test_login()
TestClass.error_login()
TestClass.get_login()
TestClass.list_products()
