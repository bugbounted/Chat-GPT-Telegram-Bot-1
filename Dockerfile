FROM python:3.11.0
USER root

ENV OPENAI_APIKEY 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
ENV TELEGRAM_BOT_APIKEY 5890958473:AAGJWMRp0ytbyHplRfgJoStvIM8qYbCci5U

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD [ "python", "./chatgpt.py" ]
