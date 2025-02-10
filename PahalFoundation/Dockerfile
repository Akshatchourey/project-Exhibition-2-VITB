FROM python:3.12
WORKDIR /app
COPY requirements.txt .

ENV PYTHONDONTWRITECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8001

CMD ["python2", "manage.py", "runserver", "0.0.0.0:8001"]
