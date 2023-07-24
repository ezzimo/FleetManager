FROM python:3.6-alpine

COPY requirements.txt /app/requirements.txt

# Configuring the server

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev \
    && pip install psycopg2

RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl 
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev
RUN apk add --no-cache geos gdal


RUN set -ex \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt

# Working directory 
WORKDIR /app

ADD . .

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "Manager.wsgi:application"]