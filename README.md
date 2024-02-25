# Solução do jogo Soletra G1 - Globo.com

Este é um script Python para jogar automaticamente o Soletra, um jogo desenvolvido pelo G1, parte da Globo.com, onde o jogador precisa formar palavras com um conjunto de letras fornecido.

## Funcionalidades

- **Geração Automática de Palavras**: O script utiliza um arquivo de texto contendo todas as palavras do dicionário português brasileiro para gerar as palavras possíveis com base nas letras fornecidas.
- **Personalização de Parâmetros**: O usuário pode definir as letras obrigatórias, letras acompanhantes, tamanho mínimo e máximo das palavras diretamente no arquivo `main.py`.
- **Exportação de Resultados**: Ao final do programa, é gerado um arquivo de texto contendo as palavras encontradas durante o jogo. O arquivo é nomeado como `resultado_soletra{data-do-dia}.txt`, onde a data do dia é adicionada ao nome do arquivo para garantir unicidade.


## Desafios durante a Criação

Durante o desenvolvimento deste script, enfrentei alguns desafios significativos que vale a pena mencionar:

- **Obtenção de um Dicionário Adequado**: Inicialmente, busquei um dicionário de palavras em português brasileiro que pudesse usar para criar o script de busca. No entanto, não foi possível encontrar um dicionário abrangente que atendesse às necessidades do jogo Soletra. Como solução, optei por reunir vários dicionários incompletos, alguns com palavras acentuadas e outros sem, e formatei-os para atender às necessidades do jogo.

- **Aprendizado do Selenium**: Este projeto foi uma das minhas primeiras experiências com o uso da biblioteca Selenium em Python. Foi necessário aprender sobre a sua utilização e explorar as funcionalidades oferecidas para automatizar as interações com o jogo de forma eficiente.

Esses desafios foram oportunidades de aprendizado e crescimento, contribuindo para o aprimoramento das minhas habilidades de desenvolvimento em Python e automação web.



## Requisitos

Para executar este script, é necessário ter instaladas as seguintes bibliotecas Python, que podem ser instaladas usando o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```
## Execução

Para jogar Soletra, basta executar o arquivo `main.py`. Certifique-se de ter configurado as variáveis necessárias no arquivo `main.py` de acordo com suas preferências ou pode deixar como está atualmente e digitar no terminal:

<!-- Coloque a imagem aqui -->

Após configurar as variáveis, execute o script:

```bash
python main.py
```

## Notas

Este script foi desenvolvido independentemente, de forma educacional e não possui afiliação oficial com o G1, Globo.com ou o jogo Soletra.

Divirta-se desvendando o jogo Soletra! 🎉

