from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path
from datetime import date
import pytest
import time

class Test_Sauce():

    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok = True)

    def teardown_method(self):
        self.driver.quit()

    def wait_for_element_visible(self,locator):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located(locator))

    
    # Başarısız giriş
    @pytest.mark.parametrize("username,password",[("1","1"),("rachell","green"),("kodlamaio","password12")])
    def test_invalid_login(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput, username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()

        errorMesage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{password}.png") 
        assert errorMesage.text == 'Epic sadface: Username and password do not match any user in this service'

     # Başarılı giriş
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_get_login(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()      
        self.driver.save_screenshot(f"{self.folderPath}/test-get-login-{username}-{password}.png")

    # Şifre boş giriş
    @pytest.mark.parametrize("username,password",[("rachell","")])
    def test_empty_password(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-empty-password-login-{username}-{password}.png")
        assert errorMessage.text == 'Epic sadface: Password is required'

    # Boş giriş
    @pytest.mark.parametrize("username,password",[("", "")])
    def test_empty_login(self,username,password):
        self.wait_for_element_visible((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        
        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID, "password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-empty-login-{username}-{password}.png")
        assert errorMessage.text == 'Epic sadface: Username is required'      


    # Locked out
    @pytest.mark.parametrize("username,password",[("locked_out_user","secret_sauce")])
    def test_locked_out(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-locked-out-login-{username}-{password}.png")
        assert errorMessage.text == 'Epic sadface: Sorry, this user has been locked out.'

    # Çıkış yap
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_log_out(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()
        
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()

        menuBtn = self.driver.find_element(By.ID,"react-burger-menu-btn")
        menuBtn.click()
        time.sleep(2)

        logoutBtn = self.driver.find_element(By.XPATH,"//*[@id='logout_sidebar_link']")
        self.driver.save_screenshot(f"{self.folderPath}/test-log-out-{username}-{password}.png")
        logoutBtn.click()
    
    #Ürün ekle
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_add_product(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()

        add_button = self.driver.find_element(By.XPATH,"//*[@id='add-to-cart-sauce-labs-bike-light']")
        add_button.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-add-cart-{username}-{password}.png")

        products_button = self.driver.find_element(By.XPATH,"//*[@id='shopping_cart_container']/a")
        products_button.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-add-cart-{username}-{password}.png")

    # Ürün listesi
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_inventory(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()
        
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        self.driver.get("https://www.saucedemo.com/inventory.html")
        self.driver.save_screenshot(f"{self.folderPath}/test-product-list-{username}-{password}.png")
   
   #Ürün sayısı
    @pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
    def test_item_number(self, username, password):
        self.wait_for_element_visible((By.ID, "user-name"))
        userNameInput = self.driver.find_element(By.ID, "user-name")
       
        self.wait_for_element_visible((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(userNameInput, username)
        action.send_keys_to_element(passwordInput, password)
        action.perform()
       
        logIn = self.driver.find_element(By.ID, "login-button")
        logIn.click()
       
        itemNumber = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        self.driver.save_screenshot(f"{self.folderPath}/test-item-number-{username}-{password}.png")
        assert len(itemNumber) == 6


    # about
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_about(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()

        menuBtn = self.driver.find_element(By.ID,"react-burger-menu-btn")
        menuBtn.click()
    
        time.sleep(1)
        aboutBtn = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/nav/a[2]")
        aboutBtn.click()
        time.sleep(8)
        self.driver.save_screenshot(f"{self.folderPath}/test-about-{username}-{password}.png")

    # İcon testi
    @pytest.mark.parametrize("username,password",[("rachell","green")])
    def test_x_icon(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        self.driver.save_screenshot(f"{self.folderPath}/test-icon-{username}-{password}.png")

        xBtn = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3/button")
        xBtn.click()
