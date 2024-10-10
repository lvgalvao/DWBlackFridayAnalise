import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém a URL do banco de dados e o nome da tabela das variáveis de ambiente
db_url = os.getenv('DATABASE_URL')
tabela = os.getenv('NOME_TABELA')

# Cria uma conexão com o banco de dados
engine = create_engine(db_url)

# Executa uma consulta SQL e carrega os resultados em um DataFrame
query = f"SELECT * FROM {tabela}"
df = pd.read_sql_query(query, engine)

# Salva o DataFrame como um arquivo CSV
df.to_csv(f'{tabela}.csv', index=False)

print("CSV criado com sucesso!")