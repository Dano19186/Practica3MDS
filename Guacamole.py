from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('file:///C:/Users/Sergio%20Vegue/Desktop/URJC/4/2o%20cuatri/MDS/guacamole/index.html')

elemento = driver.find_elements(By.CLASS_NAME, 'hole')
while True:
    for i in elemento:
        i.click()