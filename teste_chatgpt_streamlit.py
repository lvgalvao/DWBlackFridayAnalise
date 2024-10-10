import pandas as pd
from openai import OpenAI
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Carregar os dados do CSV
df = pd.read_csv("silver_google_analytics.csv")

# Preparar os dados para análise
dados = df.to_string()

# Função para fazer uma pergunta à API da OpenAI
def fazer_pergunta(pergunta, dados):
    resposta = client.chat.completions.create(
        model="gpt-4-0125-preview",
        messages=[
            {"role": "system", "content": "Você é um analista de dados especializado em e-commerce me entregue a resposta em formato de texto como se fosse escrito por um humano especialista em ecommerces."},
            {"role": "user", "content": f"Com base nos seguintes dados:\n\n{dados}\n\n{pergunta}"}
        ]
    )
    return resposta.choices[0].message.content

# Interface Streamlit
st.title("Análise de Dados de E-commerce")

# Carregar os dados
@st.cache_data
def carregar_dados():
    return pd.read_csv("silver_google_analytics.csv")

df = carregar_dados()
dados = df.to_string()

# Lista de perguntas predefinidas
perguntas_predefinidas = [
    "Qual é o total de usuários únicos?",
    "Quais são as 5 cidades com mais sessões?",
    "Qual é a média de duração das sessões?",
    "Qual é a proporção de novos usuários em relação ao total de usuários?",
    "Quais são as principais fontes de tráfego?"
]

# Remova a parte de seleção de pergunta e substitua por:
st.subheader("Análises Predefinidas")

# Criar um elemento de expansão para cada pergunta
for pergunta in perguntas_predefinidas:
    with st.expander(pergunta):
        if st.button(f"Analisar: {pergunta}", key=pergunta):
            with st.spinner("Analisando..."):
                resposta = fazer_pergunta(pergunta, dados)
            st.write(resposta)

# Mantenha a seção de pergunta personalizada
st.subheader("Pergunta Personalizada")
pergunta_personalizada = st.text_input("Digite sua pergunta personalizada:")
if st.button("Analisar Pergunta Personalizada"):
    if pergunta_personalizada:
        with st.spinner("Analisando..."):
            resposta = fazer_pergunta(pergunta_personalizada, dados)
        st.write(resposta)
    else:
        st.warning("Por favor, digite uma pergunta personalizada.")

# Exibir os primeiros registros do DataFrame
st.subheader("Visualização dos Dados")
st.dataframe(df.head())  # Exibe as primeiras linhas do DataFrame