import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.parse

# Lendo a planilha de contatos
contatos_df = pd.read_excel("enviar.xlsx")

# Configuração do Selenium
navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

# Esperar o QR Code ser escaneado
while len(navegador.find_elements(By.ID, "side")) < 1:
    time.sleep(1)

# Para cada linha da planilha
for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i, "Pessoa"]
    numero = contatos_df.loc[i, "Número"]
    texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    
    navegador.get(link)
    
    # Esperar a página carregar
    while len(navegador.find_elements(By.ID, "side")) < 1:
        time.sleep(1)
    
    # Enviar a mensagem
    time.sleep(5)  # Espera um pouco mais para garantir que carregou
    navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
    time.sleep(10)  # Espera entre mensagens para evitar bloqueio

navegador.quit()
