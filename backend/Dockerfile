FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8000
CMD ["python", "/crawling_parking_toilet.py"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]