FROM tiangolo/meinheld-gunicorn:python3.8-alpine3.11

RUN apk add --update git
RUN apk add --update libxml2-dev
RUN apk add --update libxslt-dev
#RUN apk add --update build-base
#RUN apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
RUN pip install gunicorn
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY ./Service /app
