FROM python:3.12.5
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/
COPY .env /code/.env

RUN python manage.py migrate

ENV DJANGO_SETTINGS_MODULE=UpTree.settings

EXPOSE 8000

CMD ["/bin/bash", "-c", "python populate_db.py && python manage.py runserver 0.0.0.0:8000"]
