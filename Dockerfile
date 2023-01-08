ARG CACHEBUST=1

FROM python:3.11.0

ENV OPENAI_APIKEY=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
ENV TELEGRAM_BOT_APIKEY=5890958473:AAHnszudZBU2w0G7t-KhNjINxc-MRkEWQC4

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD [ "python", "./chatgpt.py" ]
