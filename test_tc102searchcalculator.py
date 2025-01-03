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

class TestTc102searchcalculator():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tc102searchcalculator(self):
    self.driver.get("https://www.google.com/")
    self.driver.set_window_size(1050, 840)
    self.driver.find_element(By.ID, "APjFqb").send_keys("1+3")
    self.driver.find_element(By.CSS_SELECTOR, "center:nth-child(1) > .gNO89b").click()
    assert self.driver.find_element(By.ID, "cwos").text == "4"
    self.driver.close()
  
