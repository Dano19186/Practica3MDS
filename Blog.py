from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
"""driver = webdriver.Chrome()

driver.get("https://r2-ctf-vulnerable.numa.host/")"""

print(requests.get(url='https://r2-ctf-vulnerable.numa.host/').text)

