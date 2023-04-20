from selenium import webdriver
from selenium.webdriver.common.by import By
import re


def enlacesRec(source, original):
    encontrados = re.findall(regex, source)
    if encontrados:
        for i in encontrados:
            if i not in enlaces:
                enlaces.add(i)
                cuerpo = descargarHTML(original + i)
                enlacesRec(cuerpo, original + i)
        return enlaces
    else:
        return False


def descargarHTML(link):
    driver.get(link)
    web = driver.execute_script("return document.body")
    source = web.get_attribute('innerHTML')
    fichero.write(source)
    return source


def buscar(body):
    unis = re.findall(URJC, body)
    return len(unis)


regex = r'<a href="(\S*)"'
URJC = r'\bURJC\b'
driver = webdriver.Chrome()
original = "https://r2-ctf-vulnerable.numa.host/"
fichero = open("cuerpos.txt", 'w')

enlaces = set()
cuerpo = descargarHTML(original)
validos = enlacesRec(cuerpo, original)
fichero.close()
leer = open("cuerpos.txt", "r")
num = re.findall(URJC, leer.read())
print(len(num))
print(validos)
