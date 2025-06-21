import urllib.parse
import pandas as pd
contatos_df = pd.read_excel("teste_envio.xlsx")
print("\n👉 Primeiras linhas da planilha:")
print(contatos_df.head())

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# #definindo navegador
navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com")

# #matendo o navegador aberto por tempo indeterminado
input("Pressione Enter para fechar o navegador...")


#id WhatsApp carregado
import time
import urllib
while len(navegador.find_elements(by.id,"side"))==0: 
    time.sleep(1)
#conectado

for i, mensagem in enumerate(contatos_df['mensagem_enviar']):
    pessoa = contatos_df.loc[i,'primeiro_nome']
    numero = contatos_df.loc[i,'telefone_formato_completo']
    texto = urllib.parse.quote((f"📣 Fale Personal {pessoa}, {mensagem}"))
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    
    navegador.get(link)

    while len(navegador.find_elements(By.ID,"side")) ==0: 
        time.sleep(1)

# Aguarda os campos de mensagem ficarem disponíveis sugestão Gpt
    time.sleep(3)


     # Envia a mensagem sugestão Gpt
    campo_mensagem = navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div/div[3]/div/p')
    campo_mensagem.send_keys(Keys.ENTER)

    # Aguarda antes de ir para o próximo
    time.sleep(10)

    #montado por eu mesmo
    # navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div/div[3]/div/p/span').send_keys(keys.ENTER)
    # time.sleep(10)
    

# #fechando o navegador
navegador.quit()





# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import urllib.parse

# Lendo a planilha de contatos
# contatos_df = pd.read_excel("enviar.xlsx")

# # Configuração do Selenium
# navegador = webdriver.Chrome()
# navegador.get("https://web.whatsapp.com/")

# # Esperar o QR Code ser escaneado
# while len(navegador.find_elements(By.ID, "side")) < 1:
#     time.sleep(1)

# # Para cada linha da planilha
# for i, mensagem in enumerate(contatos_df['Mensagem']):
#     pessoa = contatos_df.loc[i, "Pessoa"]
#     numero = contatos_df.loc[i, "Número"]
#     texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
#     link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    
#     navegador.get(link)
    
#     # Esperar a página carregar
#     while len(navegador.find_elements(By.ID, "side")) < 1:
#         time.sleep(1)
    
#     # Enviar a mensagem
#     time.sleep(5)  # Espera um pouco mais para garantir que carregou
#     navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
#     time.sleep(10)  # Espera entre mensagens para evitar bloqueio

# navegador.quit()
