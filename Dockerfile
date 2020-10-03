FROM python:3.8.6-buster

WORKDIR /var/www/

COPY . /var/www/
RUN pip install -r requirements.txt
RUN pip install gunicorn
RUN cat /var/www/wsgi.py


EXPOSE 5000

CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "wsgi"]