#link da video aula 


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

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
driver.find_element(By.TAG_NAME,'a')

# Encontrando elemento via 'title'  

