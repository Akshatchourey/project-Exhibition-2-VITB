FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .

ENV PYTHONDONTWRITECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
