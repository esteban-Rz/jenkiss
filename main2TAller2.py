from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Inicializar navegador
driver = webdriver.Chrome()
driver.maximize_window()

# --- Parte 1: Login Portal ---
driver.get("https://webdriveruniversity.com/Login-Portal/index.html")

# Probar usuario/contraseña
driver.find_element(By.ID, "text").send_keys("usuario")
driver.find_element(By.ID, "password").send_keys("password123")
driver.find_element(By.ID, "login-button").click()

# Validar alerta
alert = driver.switch_to.alert
print("Texto del alert:", alert.text)
alert.accept()

# --- Parte 2: To Do List ---
driver.get("https://webdriveruniversity.com/To-Do-List/index.html")

# Agregar tarea
driver.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys("Nueva tarea")
driver.find_element(By.CSS_SELECTOR, "button").click()

# Marcar como completada
driver.find_element(By.XPATH, "//li[contains(text(),'Nueva tarea')]").click()

# Eliminar tarea
driver.find_element(By.XPATH, "//li[contains(text(),'Nueva tarea')]/span").click()

# Validar estado de la lista
tasks = driver.find_elements(By.TAG_NAME, "li")
print("Número de tareas actuales:", len(tasks))

# --- Parte 3: Dropdown ---
driver.get("https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")

dropdown = Select(driver.find_element(By.ID, "dropdowm-menu-1"))
dropdown.select_by_visible_text("Python")   # por texto
time.sleep(1)
dropdown.select_by_value("c#")              # por valor
time.sleep(1)
dropdown.select_by_index(2)                 # por índice

# --- Parte 4: Iframes + Popups ---
driver.get("https://webdriveruniversity.com/IFrame/index.html")

# Cambiar al iframe
driver.switch_to.frame("frame")

# Hacer clic dentro del iframe
driver.find_element(By.LINK_TEXT, "Our Products").click()

# Volver al DOM principal
driver.switch_to.default_content()

# Ir a Popup & Alerts
driver.get("https://webdriveruniversity.com/Popup-Alerts/index.html")

# Manejar Alert
driver.find_element(By.ID, "button1").click()
simple_alert = driver.switch_to.alert
print("Alert:", simple_alert.text)
simple_alert.accept()

# Manejar Confirm
driver.find_element(By.ID, "button4").click()
confirm_alert = driver.switch_to.alert
print("Confirm:", confirm_alert.text)
confirm_alert.dismiss()  # o .accept()

# Manejar Prompt
driver.find_element(By.ID, "button2").click()
prompt_alert = driver.switch_to.alert
prompt_alert.send_keys("Texto en prompt")
print("Prompt:", prompt_alert.text)
prompt_alert.accept()

driver.quit()
