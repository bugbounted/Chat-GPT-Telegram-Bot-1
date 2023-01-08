FROM python:3.11.1

ENV OPENAI_APIKEY=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
ENV TELEGRAM_BOT_APIKEY=5307238740:AAEgfisv4kC_z5ns_bL8k34ZzeLm6b6eAPk

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./chatgpt.py" ]
