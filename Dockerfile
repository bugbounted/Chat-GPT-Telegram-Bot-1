FROM python:3.11.1

ENV OPENAI_APIKEY=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
ENV TELEGRAM_BOT_APIKEY=5914221224:AAH8Tlj1crkH7MaEAQrq_DAUEwugLfN0oJQ

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
