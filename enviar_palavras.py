import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pegar_palavras import pegar_palavras


def enviar_palavras(palavras: list):
    palavras.sort()
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 4)

    driver.execute_script("window.open('about:blank', 'soletra_tab')")
    driver.switch_to.window("soletra_tab")

    url = "https://g1.globo.com/jogos/soletra/"

    driver.get(url)

    try:
        botao_alerta = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/astro-island/section/div/div/div/div/div/div/div[2]/button')))
        botao_alerta.click()
    except TimeoutException:
        pass

    botao_inciar = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/astro-island/section/div[1]/div/div[2]/div/button[1]')))
    botao_inciar.click()

    try:
        secao_instrucoes_fechar = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/astro-island/section/div[2]/div/div/div[1]/button')))
        secao_instrucoes_fechar.click()
    except TimeoutException:
        pass

    for palavra in palavras:

        if driver.find_elements(By.XPATH, '/html/body/main/astro-island/section/div[3]/div'):
            print("Jogo completado. Finalizando o loop.")
            break

        campo_input = wait.until(EC.presence_of_element_located((By.ID, "input")))

        if not campo_input.is_enabled():
            print("Campo de entrada não habilitado para digitação. Parando o loop.")
            break

        campo_input.send_keys(palavra + Keys.ENTER)
        
        time.sleep(0.5)

    input("Pressione Enter para fechar o navegador...")

    return pegar_palavras(driver)