# Projeto de Análise de Dados com LangChain e SQL

## Descrição

Este projeto tem como objetivo realizar uma análise de dados utilizando Python e SQL, com a possibilidade de integração futura com a biblioteca LangChain. O foco inicial é extrair dados de um banco de dados SQL e salvá-los em um arquivo CSV para análises posteriores.

## Objetivos

- Conectar-se a um banco de dados SQL usando variáveis de ambiente
- Extrair dados de uma tabela específica
- Salvar os dados extraídos em um arquivo CSV
- Preparar o terreno para futuras análises com LangChain

## Tecnologias Utilizadas

- Python
- pandas
- SQLAlchemy
- python-dotenv
- SQL (para consultas ao banco de dados)

## Como Começar

1. Clone este repositório
2. Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
   ```
   DATABASE_URL=sua_url_do_banco_de_dados
   NOME_TABELA=nome_da_sua_tabela
   ```
3. Instale as dependências necessárias:
   ```
   pip install pandas sqlalchemy python-dotenv
   ```
4. Execute o script principal:
   ```
   python sql_to_csv.py
   ```

## Estrutura do Projeto

- `sql_to_csv.py`: Script principal que extrai dados do banco de dados e cria um arquivo CSV
- `README.md`: Este arquivo, contendo informações sobre o projeto
- `.env`: Arquivo de configuração com variáveis de ambiente (não incluído no repositório)

## Funcionamento do main.py

O script `sql_to_csv.py` realiza as seguintes operações:

1. Carrega as variáveis de ambiente do arquivo `.env`
2. Estabelece uma conexão com o banco de dados usando a URL fornecida
3. Executa uma consulta SQL para selecionar todos os dados da tabela especificada
4. Carrega os resultados da consulta em um DataFrame do pandas
5. Salva o DataFrame como um arquivo CSV com o nome da tabela

Este processo permite extrair facilmente os dados do banco de dados para análises futuras, possivelmente utilizando LangChain ou outras ferramentas de análise de dados.

## Próximos Passos

- Implementar análises de dados usando LangChain
- Criar visualizações dos dados extraídos
- Desenvolver insights baseados nos dados da camada gold da Jornada de Dados