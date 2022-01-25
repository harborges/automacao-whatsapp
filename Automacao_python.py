#!/usr/bin/env python
# coding: utf-8

# Automação de envio de mensagens no WhatsApp
# WhatsApp automation of sending messages
# 
#     Descrição: Código para extração de dados em uma lista de contatos e envio de mensagens automatizadas.
#     Description: Code for extracting data from a contact list and sending automated messages.

# In[4]:


#Você precisa instalar a biblioteca Pandas
#You must install Pandas

#Importando pandas/Importing pandas

import pandas as pd


# In[5]:


#Abrindo planilha/Opening spreadsheet

contatos_df=pd.read_excel('Planilha de Telefones.xlsx')
display(contatos_df)


# In[6]:


#Controlando o navegador/controlling the navigator
#You must install Selenium and Urllib

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib

navegador = webdriver.Chrome()

navegador.get("https://web.whatsapp.com/")

#Esperando o login via QR code/waiting login by QR code

while len(navegador.find_elements(By.ID,'side')) < 1:
    time.sleep(1)
    
#Estamos logados no WhatsApp Web/We are logged in

for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i, "Nome"]
    numero = contatos_df.loc[i,"Telefone"]
    texto = urrlib.parse.quote(f"Oi, {pessoa}! Esse é seu código de cupom {texto}. Obrigado pela preferência")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements(By.ID,'side')) < 1:
            time.sleep(5)
    navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').sendKeys(Keys.ENTER)
    time.sleep(15)
    
navegador.quit()
print('Success!')


# In[ ]:




