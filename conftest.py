import pytest
import allure
from pages.login_page import LoginPage

# Creamos una fixture personalizada. Al llamarla, Playwright nos prestará su 'page'.
@pytest.fixture
def page_autenticada(page):
    #Hacemos el login:
    login = LoginPage(page)
    login.abrir_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login.ingresar_credenciales("Admin", "admin123")
    #Le prestramos pagina ya logueada al test que no los pida
    yield page
# --- EL PUENTE ENTRE PLAYWRIGHT Y ALLURE ---
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get('page') or item.funcargs.get('page_autenticada')
        
        if page:
            try:
                # 1. Le damos medio segundo para que termine cualquier animación de error
                page.wait_for_timeout(500) 
                
                # 2. Tomamos la foto normal (sin full_page)
                captura = page.screenshot() 
                
                # 3. La adjuntamos a Allure
                allure.attach(
                    captura,
                    name="Captura_del_Error",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                print(f"No se pudo tomar la captura de pantalla: {e}")