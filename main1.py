import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ContactUsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.webdriveruniversity.com/Contact-Us/contactus.html")
        self.driver.maximize_window()

    def test_formulario_correcto(self):
        driver = self.driver

        # Llenar formulario
        driver.find_element(By.NAME, "first_name").send_keys("Nick")
        driver.find_element(By.NAME, "last_name").send_keys("Hurtado")
        driver.find_element(By.NAME, "email").send_keys("nick@example.com")
        driver.find_element(By.NAME, "message").send_keys("Prueba positiva")

        # Enviar formulario
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        time.sleep(2)

        # Verificar mensaje
        texto = driver.find_element(By.TAG_NAME, "body").text
        self.assertIn("Thank You for your Message!", texto)

    def test_formulario_email_invalido(self):
        driver = self.driver

        # Llenar formulario con email incorrecto
        driver.find_element(By.NAME, "first_name").send_keys("Ana")
        driver.find_element(By.NAME, "last_name").send_keys("Rodriguez")
        driver.find_element(By.NAME, "email").send_keys("ana@invalido")
        driver.find_element(By.NAME, "message").send_keys("Prueba negativa")

        # Enviar formulario
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        time.sleep(2)

        # Verificar mensaje de error
        texto = driver.find_element(By.TAG_NAME, "body").text
        self.assertIn("Error: Invalid email address", texto)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

