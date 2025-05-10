from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import sys
import datetime

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
def determinar_nombre_archivo():
    directorio = sys.argv[2]
    timestamp = str(datetime.datetime.now())
    nombre_archivo = f"{directorio}/captura-{timestamp}.png"
    return nombre_archivo

def tomar_captura(navegador, nombre_archivo):
    navegador.save_screenshot(nombre_archivo)

def recibir_sitio():
    """Funcion que extrae un sitio web de un archivo txt"""
    with open(sys.argv[1], 'r') as archivo:
        lineas = archivo.readlines()
        return lineas[0]

def main():
    navegador = crear_driver()
    pagina = recibir_sitio()
    abrir_pagina(navegador = navegador, pagina = pagina)
    navegador = ajustar_ancho_y_alto(navegador)
    nombre_archivo = determinar_nombre_archivo()
    tomar_captura(navegador = navegador, nombre_archivo = nombre_archivo)
    navegador.close()

if __name__ == "__main__":
    main()
