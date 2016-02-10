FROM ubuntu:14.04
MAINTAINER P-A Söderqvist <pa.soderqvist@gmail.com>

RUN apt-get update -y
RUN apt-get install -y git python python-pip python-virtualenv gunicorn supervisor

# Setup supervisord
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN git clone https://github.com/McLoone/recipes.git /var/www/app
RUN pip install -r /var/www/app/requirements.txt

CMD ["/usr/bin/supervisord"]
