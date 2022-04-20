FROM python:3.8
LABEL MAINTAINER="Mohammad Dori | https://github.com/dori-dev"

ENV PYTHONUNBUFFERED 1

# Set working directory
RUN mkdir /dblog
WORKDIR /dblog
COPY . /dblog

# Installing requirements
ADD requirements.txt /dblog
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
# Static Files & Migrate & Super User
RUN python manage.py collectstatic --no-input
RUN python manage.py makemigrations blog --no-input
RUN python manage.py migrate --no-input

CMD ["gunicorn", "--chdir", "dblog", "--bind", ":8000", "dblog.wsgi:application"]
