import re


def criar_dict(lista_de_palavras: list):
    lista_final = {}

    for palavra in lista_de_palavras:
        tamanho = len(palavra)
        if tamanho not in lista_final:
            lista_final[tamanho] = []
        lista_final[tamanho].append(palavra)
        lista_final[tamanho].sort()

    return dict(sorted(lista_final.items()))

def criar_arquivo(nome_arquivo, lista: list):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_saida:
        arquivo_saida.write('\n'.join(lista))

def buscar_palavras(dicionario: list, letras_acompanhantes: str, letra_obrigatoria: str, tamanho_min: int, tamanho_max: int):
    regex = fr"\b(?<!-)(?:[{letras_acompanhantes}]*{letra_obrigatoria}[{letras_acompanhantes}]*)\b(?!.*-)"
    lista = []
    for palavra in dicionario:
        palavra = palavra.lower()

        palavra_busca = re.findall(regex, palavra, re.IGNORECASE)

        if palavra_busca is not None and palavra_busca not in lista and verificar_tamanho(palavra_busca, tamanho_min, tamanho_max):
            lista += palavra_busca

    lista.sort()
    return lista

def verificar_tamanho(palavra_busca: list, tamanho_min: int, tamanho_max: int):
    for palavra in palavra_busca:
        tamanho = len(palavra)
        if tamanho < tamanho_min or tamanho > tamanho_max:
            return False
    return True

def printar_palavras_por_tamanho(lista_palavras: list):
    palavras = criar_dict(lista_palavras)

    for tamanho, palavras_lista in palavras.items():
        print(f"\nPalavras com {tamanho} letras:")
        for i, palavra in enumerate(palavras_lista):
            print(f"{i+1}º - {palavra}")