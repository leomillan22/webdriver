from time import sleep
from urllib import response
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup




response = requests.get("https://www.madeiramadeira.com.br/")
print(response.text)







"""
navegador = webdriver.Chrome()

#Entrar no navegador.
navegador.get("https://www.madeiramadeira.com.br/")

#Clicar no campo para pesquisar.
campo = navegador.find_element("xpath", '//*[@id="searchAutoComplete"]')

#Digitar o que eu quero e dar enter.
## Tentar pegar o imput do usuario para saber o produto que ele quer.
campo.send_keys('cama')
sleep(1)
campo.send_keys(Keys.ENTER)

cards = navegador.find_elements('xpath', '//*[@id="control-box-content"]/div[4]/div/div/div/div[2]/div/div[1]/div[1]/div/article/a')

#lACO PARA PEGAR OS DADOS DO PRODUTO
for card in cards:
    nameHolder = card.find_element('xpath', '//*[@id="control-box-content"]/div[4]/div/div/div/div[2]/div/div[1]/div[1]/div/article/a/div[4]/div/h2')
    nome = nameHolder.get_attribute('innerHTML')
    print(nome)

# PEGAR O NOME, PRECO E LINK DE CADA PRODUTO COM O LACO FOR
# SALVAR EM UMA PLANILHA DO EXCEL
"""