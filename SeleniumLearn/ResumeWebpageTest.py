from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import urllib


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.cis.umassd.edu/~mkavatkar/")

#btn btn-success resume
#
#driver.find_element_by_css_selector("btn btn-success resume").click()

#Open linkedIn, Github page on new tabs
icons = driver.find_elements_by_xpath('//*[@id="icons"]')

#print icons
for i in range(0,3):
    xpath = '//*[@id="icons"]/div['+str(i+1)+']'
    driver.find_element_by_xpath(xpath).click()
    driver.execute_script("window.history.go(-1)")
#//*[@id="icons"]/div[2]
#linkedIn.send_keys(Keys.COMMAND + 't')
#Download Resume
driver.find_element_by_xpath('/html/body/div[3]/p/a[2]').click()

#Download image
img = driver.find_element_by_xpath('//*[@id="subheading"]/img')
src = img.get_attribute('src')
urllib.urlretrieve(src,"/home/pragnya/Downloads/IMG_8790.jpg")

#Retrieve email
email = (driver.find_element_by_id('htem')).text


driver.close()
