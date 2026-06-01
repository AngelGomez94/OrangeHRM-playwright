import pytest
from pages.login_page import LoginPage
from playwright.sync_api import expect

def test_login_exitoso(page):
    login = LoginPage(page)
    login.abrir_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login.ingresar_credenciales("Admin","admin123")
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    expect(login.obtener_titulo_pagina()).to_be_visible()