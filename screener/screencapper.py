from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from pathlib import Path
import sys

def crear_driver():
    #establecer opciones
    opciones = Options()
    opciones.add_argument("--headless")
    ubicacion_gecko = "/snap/bin/firefox.geckodriver" 
    servicio = Service(ubicacion_gecko)
    navegador =  webdriver.Firefox(options = opciones, service = servicio)
    return navegador

def abrir_pagina(navegador, pagina):
    navegador.get(pagina)

def ajustar_ancho_y_alto(navegador):
    altura = navegador.execute_script('return document.documentElement.scrollHeight')
    anchura = navegador.execute_script('return document.documentElement.scrollWidth')
    navegador.set_window_size(anchura, altura)
    return navegador

def tomar_captura(navegador):
    navegador.save_screenshot("captura.png")

def recibir_sitio():
    """Funcion que extrae un sitio web de un archivo txt"""
    with open(sys.argv[1], 'r') as archivo:
        lineas = archivo.readlines()
        return lineas[0]
def recibir_titulo():
    """Funcion que aserta el titulo en la pagina a abrir"""
    with open(sys.argv[1], 'r') as archivo:
        lineas = archivo.readlines()
        return lineas[1]

def main():
    navegador = crear_driver()
    pagina = recibir_sitio()
    abrir_pagina(navegador = navegador, pagina = pagina)
    navegador = ajustar_ancho_y_alto(navegador)
    tomar_captura(navegador = navegador)
    navegador.close()

if __name__ == "__main__":
    main()
