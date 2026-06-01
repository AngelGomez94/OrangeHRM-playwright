import random
import os 
from faker import Faker
class BasePage:
    faker = Faker()
    def __init__(self, page):
     self.page = page
     

    def abrir_url(self,url):
        self.page.goto(url,wait_until="commit", timeout=60000)

    def escribir_texto(self,locator,texto):
        locator.fill(texto) # Limpiar el campo antes de escribir
    
    def hacer_click(self,locator): 
        locator.click()

    def obtener_texto(self,locator):
       return locator.inner_text()# Te devuelve exactamente lo que un humano puede ver en la pantalla en ese momento.
    
    def llenar_dropdown(self, dropdown_selector,opcion_locator):
        dropdown_selector.click()
        opcion_locator.click()
    def seleccionar_radiobutton(self, *locators):
        locator_seleccionado = random.choice(locators)
        locator_seleccionado.click()

    def subir_archivo(self,ruta_archivo, locator):
        #Subir la foto del empleado
        ruta_foto = os.path.abspath(ruta_archivo)
        locator.set_input_files(ruta_foto)
    def generar_correo_aleatorio(self,locator):
         correo_principal = self.faker.email() 
         locator.fill(correo_principal)


       

        
        
           
    