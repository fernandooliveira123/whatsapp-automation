import pandas as pd
import urllib.parse
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Lê os contatos da planilha
contatos_df = pd.read_excel("clientes_ateJunho_2025.xlsx")
print("\n👉 Primeiras linhas da planilha:")
print(contatos_df.head())

# Inicia o navegador e abre o WhatsApp Web
navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com")

# Aguarda o login manual com o QR Code
input("⚠️ Escaneie o QR Code e pressione Enter para continuar...")

# Garante que a interface do WhatsApp foi carregada
while len(navegador.find_elements(By.ID, "side")) == 0:
    time.sleep(1)

# Fecha o pop-up "WhatsApp Web está de cara nova", se aparecer
try:
    time.sleep(2)  # Pequena espera extra para o pop-up surgir
    popup_botao = navegador.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[2]/div/button')
    popup_botao.click()
    print("🧹 Pop-up fechado automaticamente.")
except:
    print("ℹ️ Nenhum pop-up encontrado, continuando...")

# Envia mensagem para cada contato
for i, mensagem in enumerate(contatos_df['mensagem_enviar']):
    pessoa = contatos_df.loc[i, 'primeiro_nome']
    numero = contatos_df.loc[i, 'telefone_formato_completo']
    
    texto = urllib.parse.quote(f"📣 Fale Personal {pessoa}, {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    
    navegador.get(link)

    # Espera o chat carregar
    while len(navegador.find_elements(By.ID, "side")) == 0:
        time.sleep(1)

    # Aguarda a área de mensagem carregar
    time.sleep(3)

    try:
        campo_mensagem = navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div/div[3]/div/p')
        campo_mensagem.send_keys(Keys.ENTER)
        print(f"✅ Mensagem enviada para {pessoa}")
    except Exception as e:
        print(f"❌ Erro ao enviar mensagem para {pessoa}: {e}")
    
    time.sleep(10)

# Finaliza
navegador.quit()
