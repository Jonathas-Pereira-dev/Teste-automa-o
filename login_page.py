# Importa o seletor 'By', usado para localizar elementos na página
from selenium.webdriver.common.by import By

# Classe que representa a página de login do sistema
class LoginPage:
# Construtor da classe, recebe o 'driver'

    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login")
# Método que acessa a URL da página de login
    def acessar_pagina(self, url):
        self.driver.get(url)
    def preencher_usuario(self, usuario):
        self.driver.find_element(*self.username_input).send_keys(usuario)

    def preencher_senha(self, senha):
        self.driver.find_element(*self.password_input).send_keys(senha)

    def clicar_login(self):
        self.driver.find_element(*self.login_button).click()
