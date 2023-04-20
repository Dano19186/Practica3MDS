from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
driver = webdriver.Chrome()

driver.get("https://r2-ctf-vulnerable.numa.host/")

h = driver.execute_script("return document.body.innerHTML;")
print(h)
driver.close()
#print(requests.get(url='https://r2-ctf-vulnerable.numa.host/').text)

