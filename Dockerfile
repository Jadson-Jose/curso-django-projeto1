FROM python:3.12.7-slim

ENV PYTHONDONTWRITBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends build-essential libpq-dev && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . . 

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "projeto.wsgi:application"]