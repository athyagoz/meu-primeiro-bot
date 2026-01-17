from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. Configuração: Abre o navegador
driver = webdriver.Chrome()
driver.get("https://analista-teste.seatecnologia.com.br")

try:
    # 2. Ação: Clica no botão de adicionar
    print("Tentando clicar em + Adicionar Funcionário...")
    botao_adicionar = driver.find_element(By.XPATH, "//button[contains(text(), 'Adicionar')]")
    botao_adicionar.click()
    
    # 3. Ação: Preenche os campos
    driver.find_element(By.ID, "nome").send_keys("Robô de Teste")
    driver.find_element(By.ID, "cpf").send_keys("12345678901")
    
    # 4. Ação: Tenta salvar
    driver.find_element(By.ID, "salvar").click()
    print("Comando de salvar enviado.")
    
    time.sleep(3) # Espera para ver o resultado

finally:
    driver.quit()
