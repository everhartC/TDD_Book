from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
new_binary = FirefoxBinary(R"C:\Program Files\Firefox Developer Edition\firefox.exe")


browser = webdriver.Firefox(firefox_binary=new_binary)
browser.get('http://localhost:8000')

assert 'Django' in browser.title