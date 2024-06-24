FROM rasa/rasa:latest

WORKDIR /app

COPY . /app

EXPOSE 5005

CMD ["rasa", "run", "-m", "models", "--enable-api", "--cors", "*"]
