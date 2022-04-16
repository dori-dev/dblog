FROM python:3.8
LABEL MAINTAINER="Mohammad Dori | https://github.com/dori-dev"

ENV PYTHONUNBUFFERED 1

RUN mkdir /dblog
WORKDIR /dblog
COPY . /dblog

ADD requirements.txt /dblog
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --no-input

CMD [ "gunicorn", "--chdir", "dblog", "--bind", ":8000", "dblog.wsgi:application" ]