# Web scraping (raspagem de dados)
Este projeto tem como objetivo demonstrar uma implementação simples de web scraping em Python, utilizando requisições HTTP para coletar dados públicos diretamente de uma página web.

## 🚀 Tecnologias Utilizadas

* Python 3

* Requests – para realizar requisições HTTP

* BeautifulSoup (bs4) – para fazer o parse do HTML e extrair os dados

* sqlite3

## 🎯 Objetivo do Projeto

* O script acessa a página:
https://www.idealsoftwares.com.br/indices/ipca_ibge.html
e realiza a coleta dos dados de uma tabela HTML e insere em um banco SQLlite.

## 🧠 Conceitos Abordados

* Requisições HTTP (GET)

* Estrutura básica de páginas HTML

* Seleção de elementos HTML

* Extração e tratamento inicial de dados

* Boas práticas em web scraping


## ⚙️ Como Executar o Projeto
Clone o repositório:

```
git clone https://github.com/mayacabral/Raspagem-de-dados.git raspagem_dados
```

Acesse a pasta do projeto:

```
cd raspagem_dados
```
Crie um ambiente virtual do Python e depois ative ele.

Encerre o terminal e abra um novo

Instale as dependências:

```
pip install -r requirements.txt
```

Execute o script:

```
python main.py
```
