import unittest
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class test1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        driver = self.driver
        driver.wait = WebDriverWait(driver,10)
        driver.maximize_window()
        driver.get("http://www.demo.guru99.com/V4/")

        #Assert Title
        try:
            assert "Guru99" in driver.title
        except:
            print " Sorry name is not present in title"
        #break


        #for i in range(0,20):
        userId = driver.find_element_by_xpath('/html/body/form/table/tbody/tr[1]/td[2]/input')

        userId.clear()
        userId.send_keys('mngr43201')


        password = self.driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[2]/input')
        password.clear()
        password.send_keys('ybEvEha')


        #Check Login Button
        driver.find_element_by_xpath('/html/body/form/table/tbody/tr[3]/td[2]/input[1]').click()


        driver.execute_script("window.history.go(-1)")

        #Check Reset button
        driver.find_element_by_xpath('/html/body/form/table/tbody/tr[3]/td[2]/input[2]').click()


    #driver.close()


if __name__ == '__main__':
    print " "
    unittest.main()

#Performance not good for multiple login - Database
'''
Test Cases:

1. Make sure site opens
2. Check title assertion
3. Username textbox
4. Password textbox
5. Password should be encrypted
6. Check if Login button works
7. Check if reset button works

'''
