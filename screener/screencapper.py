from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from pathlib import Path

def crear_driver():
    #establecer opciones
    opciones = Options()
    opciones.headless = True
    ubicacion_gecko = "/snap/bin/firefox.geckodriver" 
    servicio = Service(ubicacion_gecko)
    navegador =  webdriver.Firefox(options = opciones, service = servicio)
    return navegador
def asertar_titulo(navegador, pagina, titulo):
    navegador.get(pagina)
    assert titulo in navegador.title

def tomar_captura(navegador):
    navegador.save_screenshot("pain.png")

def main():
    navegador = crear_driver()
    asertar_titulo(navegador = navegador, pagina = "https://www.google.com/", titulo = "Google")
    tomar_captura(navegador = navegador)
    navegador.close()

if __name__ == "__main__":
    main()
