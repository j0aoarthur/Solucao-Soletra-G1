from datetime import date

from busca import buscar_palavras, criar_arquivo, printar_palavras_por_tamanho
from enviar_palavras import enviar_palavras

letra_obrigatoria = input("Digite a letra obrigatória em todas as palavras: ")
letras_acompanhantes = input("Digite em sequência todas as letras que podem ou não estar na palavra (Ex: abcdef): ") + letra_obrigatoria
minimo_tamanho = int(input("Qual o tamanho mínimo de letras: "))
maximo_tamanho = int(input("Qual o tamanho máximo de letras: "))

file1 = open("dicionario_soletra.txt", "r")
palavras_arquivo1 = file1.readlines()

palavras_encontradas = buscar_palavras(palavras_arquivo1, letras_acompanhantes, letra_obrigatoria, minimo_tamanho, maximo_tamanho)

printar_palavras_por_tamanho(palavras_encontradas)

escolha = input("Deseja tentar todas essas palavras no jogo? (S/N) ").lower()

if escolha == 's':
    resultado_final = enviar_palavras(palavras_encontradas)
    criar_arquivo(f"resultado_soletra_{date.today()}.txt", resultado_final)
elif escolha == 'n':
    exit()