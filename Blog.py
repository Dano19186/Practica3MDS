from selenium import webdriver
import re


def enlacesRec(original):
    cuerpo = descargarHTML(original)
    inicial = re.findall(regex, cuerpo)
    for i in inicial:
        enlace = (raiz + "notice/" + i[1])
        if enlace not in enlaces:
            enlaces.add(enlace)
            enlacesRec(enlace)


def descargarHTML(link):
    driver.get(link)
    body = driver.execute_script("return document.body.innerHTML")
    fichero.write(body)
    return body


def buscar(body):
    unis = re.findall(URJC, body)
    return len(unis)


regex = r'(<a href=\"\/notice\/|<a href=\")([^\";#]{1,})\"'

URJC = r'\bURJC\b'
driver = webdriver.Chrome()
raiz = "https://r2-ctf-vulnerable.numa.host/"
fichero = open("cuerpos.txt", 'a')

enlaces = set()

enlacesRec(raiz)
fichero.close()
leer = open("cuerpos.txt", "r")
num = re.findall(URJC, leer.read())
print(len(num))
