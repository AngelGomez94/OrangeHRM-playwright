import pytest
from playwright.sync_api import expect # Importamos las validaciones (Asserts) nativas

def test_login_playwright(page):
    # 1. Navegar (Igual que driver.get)
    page.goto(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", 
        wait_until="commit", # <--- EL TRUCO: Solo espera a que el servidor responda "Ok", no a que cargue la vista.
        timeout=60000        # <--- Y por si las dudas, le damos 60 segundos de paciencia extra.
    )

    # 2. Llenar campos
    # get_by_placeholder busca exactamente el texto gris que está de fondo en la caja de texto
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")

    # 3. Hacer click
    # get_by_role busca elementos por su tipo y su texto visible
    page.get_by_role("button", name="Login").click()

    # 4. Asserts Nativos (Playwright se queda esperando automáticamente hasta que esto sea verdad)
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    
    # Validamos que el título Dashboard sea visible en la pantalla
    titulo = page.get_by_role("heading", name="Dashboard")
    expect(titulo).to_be_visible()