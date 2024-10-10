# Use uma imagem base oficial do Python
FROM python:3.12

# Define o diretório de trabalho no container
WORKDIR /app

# Copia os arquivos de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto dos arquivos do projeto para o diretório de trabalho
COPY . .

# Especifica o comando para executar a aplicação
CMD ["python", "app.py"]