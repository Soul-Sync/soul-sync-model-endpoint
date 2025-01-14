FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -U pip

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:8080"]
