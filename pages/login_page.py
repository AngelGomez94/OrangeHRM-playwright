from pages.base_page import BasePage
class LoginPage(BasePage):
    def __init__(self,page):
        super().__init__(page)

        self.txt_usuario = page.get_by_placeholder("Username")
        self.txt_contrasena = page.get_by_placeholder("Password")
        self.btn_iniciar_sesion = page.get_by_role("button", name="Login")
        self.titulo_pagina = page.get_by_role("heading", name="Dashboard")
    
    def ingresar_credenciales(self,usuario,password):
        self.escribir_texto(self.txt_usuario,usuario)
        self.escribir_texto(self.txt_contrasena,password)
        self.hacer_click(self.btn_iniciar_sesion)

    def obtener_titulo_pagina(self):
        # Retornamos el locator para hacer validaciones en el test
        return self.titulo_pagina