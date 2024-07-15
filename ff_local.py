from time import sleep
import unittest
from selenium import webdriver
#from selenium.webdriver.common import desired_capabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element(By.NAME, "q").send_keys("pycon").send_keys(Keys.RETURN)
#        elem.send_keys("pycon")
#        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found", driver.page_source)
        sleep(2)
        driver.find_element(By.CSS_SELECTOR, "#downloads > a:nth-child(1)").click()
        sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/header/div/div[2]/div/div[2]/p/a").click()
        sleep(2)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()