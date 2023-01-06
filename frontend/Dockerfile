FROM python3
ENV TAG=template
RUN apt-get update -y
RUN apt-get install -y python3 pip
RUN mkdir ~/CC/
RUN cd ~/CC/
# WORKDIR ~/CC/CC/
RUN pip install virtualenv
COPY /home/cloudcomputing-/CC/ ~/CC/
# RUN cd /home/$USER/CC/CC
# RUN source ./fronent/cc/bin/activate
# RUN pip install django djangorestframework psycopg2-binary django-keycloak-auth oic
# RUN python3 ./frontend/manage.py runserver

