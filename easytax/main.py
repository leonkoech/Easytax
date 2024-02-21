'''
This is Automated for Chrome Users.. 
NOTE: Ids and Classes may be Changed in Future While Upgrading the Site..
Change Those Ids and Classess if any of them are Changed.. 
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import cv2
import pytesseract
import secrets


def openkra():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    # Getting the Url Fired..
    driver = webdriver.Chrome(options=options, executable_path='/usr/local/bin/chromedriver')
    driver.get('https://itax.kra.go.ke/')
    time.sleep(3)  # sleep for 3 seconds after page has loaded
    # Signing In to Your Account.. Do add your PINS and PASSWORDS in Secrets.py inorder to make the Code Work..
    inputpin = driver.find_element_by_xpath('//*[@id="logid"]')
    inputpin.send_keys(secrets.pin)
    time.sleep(3)  # sleep for 10 seconds to see input
    signinbtn = driver.find_element_by_xpath('//*[@id="normalDiv"]/table/tbody/tr[3]/td[2]/a')
    signinbtn.click()
    time.sleep(4)
    downloadimage(driver, '//*[@id="captcha_img"]')
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="captcahText"]').send_keys(readimage())
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="xxZTT9p2wQ"]').send_keys(secrets.password)
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="loginButton"]').click()
    time.sleep(8)
    action = ActionChains(driver)
    action.move_to_element(driver.find_element_by_xpath('//*[@id="ddtopmenubar"]/ul/li[3]/a')).perform()
    # move to file nil returns
    filenil = driver.find_element_by_xpath('//*[@id="Returns"]/li[4]/a')
    # hover over the item
    action.move_to_element(filenil).perform()
    # now click on the item
    filenil.click()
    time.sleep(3)
    # find the  options
    driver.find_element_by_xpath('//*[@id="regType"]').click()
    # and hover over resident
    # click on it
    driver.find_element_by_xpath('//*[@id="regType"]/option[2]').click()
    time.sleep(2)
    # click the next button
    driver.find_element_by_xpath('//*[@id="btnSubmit"]')
    time.sleep(10)

    # Closing the Driver after Completion of TASK 
    driver.quit()

# Function to Read and Write the Images
def downloadimage(driver, link):
    with open('filename.png', 'wb') as file:
        file.write(driver.find_element_by_xpath(link).screenshot_as_png)

# Reading the Images Using OpenCV Module and Converting the Text in the Image into a string Using Pytesseract Module .. 
def readimage():
    img = cv2.imread('filename.png')
    text = pytesseract.image_to_string(img)
    text = text[:-1]
    for t in text:
        if t == '+':
            text = text.replace(t, ' ')
            text = text.split()
            ans = int(text[0]) + int(text[1])
            return ans
        elif t == '-':
            text = text.replace(t, ' ')
            text = text.split()
            ans = int(text[0]) - int(text[1])
            return ans

# Running the Program If it is the Main Script ... 
if __name__ == '__main__':
    openkra()
