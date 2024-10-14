from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import re

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)



# driver.maximize_window()    
driver.get("https://veterinariasperu.net/trujillo/")
time.sleep(2)

vets_xpath = '//div/div/div/div/div/div/h3'
WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, vets_xpath)))
vets = driver.find_elements(By.XPATH, vets_xpath)
for v in vets:
    print(v.text)

urls_xpath = '//iframe'
WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, urls_xpath)))
iframes = driver.find_elements(By.XPATH, urls_xpath)
for iframe in iframes:
    src = iframe.get_attribute("src")
    if  src.startswith("https://www.google.com/maps/"):
        url = src
        # Expresiones regulares para capturar los valores de 2d (longitud) y 3d (latitud)
        longitud = re.search(r"2d(-?\d+\.\d+)", url)
        latitud = re.search(r"3d(-?\d+\.\d+)", url)
        if longitud and latitud:
            print("Latitud (3d):", latitud.group(1),"---","Longitud (2d):", longitud.group(1))
        else:
            print("No se encontraron las coordenadas 2d o 3d.")

uls_xpath = '//div/div/div/div/div/div/div/ul'
WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, uls_xpath)))
uls = driver.find_elements(By.XPATH, uls_xpath)
for ul in uls:
    if not ul.text.startswith("Veterinaria"): 
        print(ul.text)
