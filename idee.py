from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('./chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get("http://localhost/Projet_TDW/public/idee_recette/afficher_form_page")  
elements = driver.find_element("id","send")
ingre = ["sel","huile","Farine","lait","levure chimique","Citronnade","Nectarines","Eau froide","Champignons","Cheddar","Une sauce tomate","Pâte feuilletée express","Thon","Olives noires","beurre","biscuit haché","chocolat noir","Boudoirs"]
but = driver.find_element("id","add")
for i in range(len(ingre)):
    driver.find_element("id","send").send_keys(ingre[i])
    driver.find_element("id","ingr").submit() 
time.sleep(500)

