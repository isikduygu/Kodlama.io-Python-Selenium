# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager

class TestTestxicon():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testxicon(self):
    self.driver.get("https://www.saucedemo.com/")
    self.driver.maximize_window()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "user-name")))
    self.driver.find_element(By.ID, "user-name").click()
    self.driver.find_element(By.ID, "user-name").send_keys("1")
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "password")))
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("1")
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "login-button")))
    self.driver.find_element(By.ID, "login-button").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id=\'login_button_container\']/div/form/div[3]/h3")))
    self.driver.find_element(By.CSS_SELECTOR, ".fa-times > path").click()
    self.driver.close()
  
