
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from time import sleep
from pathlib import Path
import csv


fieldnames = ['Nome', 'Cod.Item', 'Preço','Detalhe do Produto']
data_pholder = Path('C:/Users/55199/Documents/')
file_to_open = data_pholder/"person.csv"

base_url = 'https://www.extra.com.br'


for item in range(1, 20):
    url_site = f'{base_url}/?Filtro=D37608&ordenacao=_maisvendidos&nid=201966&paginaAtual={item}'

    row = ''
    google_chrome_pet_shop = webdriver.Chrome()
    google_chrome_pet_shop.get(url_site)
    bs_obj = bs(google_chrome_pet_shop.page_source, 'html.parser')
    list = bs_obj.find_all('li', {'class': 'pet-shop'})

    for item in list:

        attrib_link = item.find('a')
        nome_produto = attrib_link.get('title')
        if item.find('span', {'class':'productDetails'}) is not None:
            preço_produto = item.find('span', {'class':'productDetails'}).text != None

        link_next_nivel = attrib_link.get('href')
        google_chrome_details = webdriver.Chrome()
        google_chrome_details.get(link_next_nivel)
        bs_obj_details = bs(google_chrome_details.page_source, 'html.parser')

        details_title = bs_obj_details.find('div', {'class': 'detalhesProduto'}).find('label').text
        details_product = bs_obj_details.find('div', {'id': 'descricao'}).text
        fieldnames.append([nome_produto, 1, preço_produto,details_product ])
    
        google_chrome_details.quit()
        csvData = fieldnames
        with open(file_to_open, 'w')as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            #writer.writerow({'Nome': 'Baked', 'Cod.Item': 'Beans', 'Preço':'sasa', 'Detalhe do Produto':'fsdfds' })
            writer.writerows(csvData)
        csvfile.close()


    google_chrome_pet_shop.quit()
