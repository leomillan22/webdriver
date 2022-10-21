from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Chrome()

#Entrar no navegador.
navegador.get("https://www.madeiramadeira.com.br/")

#Clicar no campo para pesquisar.
campo = navegador.find_element("xpath", '//*[@id="searchAutoComplete"]')

#Digitar o que eu quero e dar enter.
## Tentar pegaro imput do usuario para saber o produto que ele quer.
campo.send_keys('cama')
campo.send_keys(Keys.ENTER)