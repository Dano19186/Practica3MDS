import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('file:///C:/Users/Daniel/Documents/4_UNIVERSIDAD/MDS/10fastfingers-2023/index.html')
time.sleep(5)
#esperar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'word_1')))
frase = ""
for i in range(1, 21):
    palabra = driver.find_element(By.ID, "word_"+str(i)).text
    frase += palabra+" "
escribir = driver.find_element(By.XPATH, '//*[@id="textInput"]')
escribir.send_keys(frase)
time.sleep(10)
driver.close()
