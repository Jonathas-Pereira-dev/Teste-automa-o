import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage

# Define um fixture do pytest que configura o navegador antes dos testes e fecha após
@pytest.fixture
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
    
# Teste para verificar se o login com dados válidos funciona corretamente
def test_login_com_sucesso(driver):
    login_page = LoginPage(driver)
    login_page.acessar_pagina("https://exemplo.com/login")
    login_page.preencher_usuario("usuario_valido")
    login_page.preencher_senha("senha_valida")
    login_page.clicar_login()

    assert "dashboard" in driver.current_url

def test_login_com_erro(driver):
    login_page = LoginPage(driver)
    login_page.acessar_pagina("https://exemplo.com/login")
    login_page.preencher_usuario("usuario_invalido")
    login_page.preencher_senha("senha_errada")
    login_page.clicar_login()

    assert "erro" in driver.page_source.lower()
