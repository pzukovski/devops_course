
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

ser = Service("C:\\temp\\chromedriver.exe")
op = webdriver.ChromeOptions()
s = webdriver.Chrome(service=ser, options=op)
s.get('https://www.google.com')
s.find_element(By.NAME,'q').send_keys('Paul Zukovski LinkedIn',Keys.ENTER)

