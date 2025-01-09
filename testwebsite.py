import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

class GoogleTest(unittest.TestCase):
    def test_search(self):
        s = Service('C:\\webdriver\\chromedriver-win64\\chromedriver.exe')
        driver = webdriver.Chrome(service=s)

        # เปิดเว็บไซต์ Google
        driver.get("https://www.google.com/")
        driver.set_window_size(1072, 816)

        # พิมพ์คำค้นหา "ไทยรัฐ" ลงในช่องค้นหา
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("ไทยรัฐ")
        search_box.send_keys(Keys.RETURN)  
        # รอให้ผลลัพธ์การค้นหาโหลดเสร็จ
        time.sleep(5)

        # ตรวจสอบว่าผลลัพธ์แรกมีคำว่า "ไทยรัฐ" และพิมพ์ชื่อเว็บไซต์ไทยรัฐในผลลัพธ์แรก
        first_result = driver.find_element(By.CSS_SELECTOR, "h3")
        self.assertIn("ไทยรัฐ", first_result.text)
        print("ผลลัพธ์แรก: " + first_result.text)

        # คลิกที่ลิงก์เว็บไซต์ไทยรัฐ
        driver.find_element(By.PARTIAL_LINK_TEXT, "ไทยรัฐ").click()

        # รอให้หน้าไทยรัฐโหลดเสร็จ
        time.sleep(5)

        # คลิกที่เมนู hamburger เพื่อเลือกเมนูค้นหา
        hamburger_menu = driver.find_element(By.ID, "hamburger")  # ปรับ ID ให้ตรงกับเว็บไซต์จริง
        hamburger_menu.click()
        time.sleep(2)  # รอเมนูแสดงผล

        # ค้นหาช่องค้นหาในเมนูที่แสดงขึ้นมา
        thairath_search_box = driver.find_element(By.NAME, "txt-search")  # ตรวจสอบว่าชื่อช่องค้นหาในเมนูเหมือนเดิมหรือเปลี่ยน
        thairath_search_box.send_keys("squid game")
        thairath_search_box.send_keys(Keys.RETURN)  

        # รอให้ผลลัพธ์การค้นหาในไทยรัฐโหลดเสร็จ
        time.sleep(5)

        # พิมพ์หัวข้อของหน้า
        print("Title ของหน้า: " + driver.title)

        # ปิดเบราว์เซอร์
        driver.quit()

if __name__ == '__main__':
    unittest.main()
