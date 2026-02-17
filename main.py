from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

service = Service(executable_path="msedgedriver.exe")
driver = webdriver.Edge(service=service)

driver.get("https://www.saucedemo.com/")
 #time.sleep(2) 
WebDriverWait (driver,10).until(
    EC.presence_of_all_elements_located (By.XPATH,'//input[@placeholder="Username"]')
)
username_input = driver.find_elements(By.XPATH,'//input[@placeholder="Username"]')
username_input.send_keys("standar_user")
time.sleep(10)
passwork_input = driver.find_elements(By.XPATH,'//input[@name="password"]')
passwork_input.send_keys("standar_sauce")
boton_login = driver.find_elements(By.XPATH, '//input[contains(@value,"Login")]')
boton_login.click()
time.sleep(10)
# agragar el primer producto 
boton_compra = driver.find_element(By.XPATH, '//div [ contains(text(),"Backpack")]/../../..// button [contains (text(), "Add ") ]')
boton_compra.click ()
#agregar el segundo producto
boton_compra1 = driver.find_element(By.XPATH,'//div [ contains(text(),"Bike")]/../../..// button [contains (text(), "Add ") ]')
boton_compra1.click
#agregar el  tercero 
boton_compra2 = driver.find_element (By.XPATH, '//div [ contains(text(),"Bolt")]/../../..// button [contains (text(), "Add ") ]')
boton_compra2.click
time.sleep(5)
#click carrito de compras 
carrito_compras = driver.find_element (By.XPATH, '//a[@data-test="shopping-cart-link"]')
carrito_compras.click
time.sleep(10)
#click boton check
boton_check = driver.find_element (By.XPATH,' //button[ @name = "checkout" ]')
boton_check.click
