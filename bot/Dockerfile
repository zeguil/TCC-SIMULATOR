FROM python:3.11-slim

WORKDIR /app

COPY bot.py .

COPY requirements.txt .

# Instale as dependências
RUN pip install -r requirements.txt

# Comando para iniciar o aplicativo
CMD ["python", "bot.py"]
