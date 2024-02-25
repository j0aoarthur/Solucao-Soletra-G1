from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def pegar_palavras(driver):
    wait = WebDriverWait(driver, 10)

    try:

        elemento_pai = wait.until(
            EC.presence_of_element_located((By.XPATH, "/html/body/main/astro-island/section/div/div/div[2]/div/div[2]/div[2]"))
        )

        elementos_filhos = elemento_pai.find_elements(By.XPATH, "./div")

        lista_palavras = []

        for filho in elementos_filhos:
            if "found" in filho.get_attribute("class"):
                lista_palavras.append(filho.text)

        return lista_palavras

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return []


