import pandas as pd
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Carregar os dados do CSV
df = pd.read_csv("silver_google_analytics.csv")

# Preparar os dados para análise
dados = df.to_string()

# Função para fazer uma pergunta à API da OpenAI
def fazer_pergunta(pergunta):
    resposta = client.chat.completions.create(model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Você é um analista de dados especializado em e-commerce."},
        {"role": "user", "content": f"Com base nos seguintes dados:\n\n{dados}\n\n{pergunta}"}
    ])
    return resposta.choices[0].message.content

# Lista de perguntas para análise
perguntas = [
    "Qual é o total de usuários únicos?",
    "Quais são as 5 cidades com mais sessões?",
    "Qual é a média de duração das sessões?",
    "Qual é a proporção de novos usuários em relação ao total de usuários?",
    "Quais são as principais fontes de tráfego?"
]

# Fazer as perguntas e imprimir as respostas
for i, pergunta in enumerate(perguntas, 1):
    print(f"\nAnálise {i}:")
    print(fazer_pergunta(pergunta))