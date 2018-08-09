import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromeDriverPath = 'D:/_devTool/selenium_driver_chrome/chromedriver'
driver = webdriver.Chrome(chromeDriverPath)
driver.get("http://www.dianping.com/")

loginBtn = driver.find_element_by_css_selector('.login-container.J-login-container a[data-click-name="login"]')
if not loginBtn:
    print 'has logged in'
else:
    print 'has not logged in'

loginBtn.click()

time.sleep(3)

driver.switch_to.frame(0)

pcBtn = driver.find_element_by_css_selector('.icon-pc')
pcBtn.click()

phoneInput = driver.find_element_by_css_selector('#mobile-number-textbox')
phoneInput.send_keys('13701740453')

sendVerifyCodeBtn = driver.find_element_by_css_selector('#send-number-button')
sendVerifyCodeBtn.click()

verifyCode = raw_input('please input verify code:')
verifyCodeInput = driver.find_element_by_css_selector('#number-textbox')
verifyCodeInput.send_keys(verifyCode)

loginBtn = driver.find_element_by_css_selector('#login-button-mobile')
loginBtn.click()


time.sleep(3)

#driver.close()