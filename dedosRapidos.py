import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('C:/Users/Sergio Vegue/Desktop/URJC/4/2o cuatri/MDS/index.html')
time.sleep(5)

frase = ""
for i in range(1, 21):
    palabra = driver.find_element(By.ID, "word_"+str(i)).text
    frase += palabra+" "
escribir = driver.find_element(By.XPATH, '//*[@id="textInput"]')
escribir.send_keys(frase)
time.sleep(10)



