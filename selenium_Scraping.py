#link da video aula 


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import pandas as pd
# Serve parar iniciar uma instancia do Chomer WebDriver
Service = Service()

# Usado para definir a preferencia de para o browser Chome
options = webdriver.ChromeOptions()

#Inicia a instancia do Chrome WebDriver com as definidas 'opitions' e 'service'
driver = webdriver.Chrome(service=Service,options=options)

#link de exemplo, para entrar na tela
url = 'https://books.toscrape.com/'
driver.get(url)

#Encontrando elementos via 'tag name' HTML, a parti do primeiro elemento
 

# Encontrando elemento via 'title'  
driver.find_element(By.TAG_NAME,'a').get_attribute('title')

# Pegando todos os titulos da lista de dois em dois
titleelements = driver.find_elements(By.TAG_NAME,'a')[54:94:2]

#clicando no primeiro  nome
titleelements[0].click()

#Voltando
driver.back()

# Pegando os dados de uma 'class' e depois tirando os dandos que não precisam 
int(driver.find_element(By.CLASS_NAME,'instock').text.replace('In stock (','').replace(' available)',''))


# Iniciando um desafio para pegar o titulo e a quantidade em estoque
lis = []
titleelements = driver.find_elements(By.TAG_NAME,'a')[54:94:2]
tierList = [i.get_attribute('title') for i in titleelements]
for i in titleelements:
    i.click()
    estoq = int(driver.find_element(By.CLASS_NAME,'instock').text.replace('In stock (','').replace(' available)',''))
    lis.append(estoq)
    driver.back()

dicDf = {'title':tierList,
         'stock':estoq}

pd.DataFrame(dicDf)
