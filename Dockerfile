FROM python:3.13.3-alpine

ENV PYTHONDONTWRITBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apk update && apk add --no-cache build-base postgresql-dev && rm -rf /var/cache/apk/*
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . . 

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "project.wsgi:application"]