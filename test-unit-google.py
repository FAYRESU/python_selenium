import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

class GoogleTest(unittest.TestCase):
   
  def setUp(self):
    s = Service('D:\chromdriver\chromedriver.exe')
    self.driver = webdriver.Chrome(service=s)
    self.driver.get("https://www.google.com/")
    self.driver.set_window_size(1072, 816)

  def tearDown(self):
    self.driver.quit()
   
  def test_search_calculator_add(self):
    self.driver.find_element(By.ID, "APjFqb").send_keys("5+5")
    self.driver.find_element(By.NAME, "q").send_keys(Keys.RETURN)
    assert self.driver.find_element(By.ID, "cwos").text == "10"
    assert self.driver.title == "5+5 - ค้นหาด้วย Google"

    # Wait for the search results to load
    time.sleep(5)

  def test_search_calculator_multiply(self):
    self.driver.find_element(By.ID, "APjFqb").send_keys("5*5")
    self.driver.find_element(By.CSS_SELECTOR, "center:nth-child(1) > .gNO89b").click()
    assert self.driver.find_element(By.ID, "cwos").text == "25"
    assert self.driver.title == "5*5 - ค้นหาด้วย Google"

    # Wait for the search results to load
    time.sleep(5)

 
if __name__ == '__main__':
  unittest.main()