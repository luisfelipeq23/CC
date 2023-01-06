FROM python:3
WORKDIR /CC/CC/frontend
COPY . /CC/CC/frontend/
RUN pip install -r ./cc_proyecto/requirements.txt --no-cache-dir --root-user-action=ignore
RUN bin/bash
RUN source cc/bin/activate 
#ENV PORT=8000
#EXPOSE 8000
#RUN python ~/frontend/cc_proyecto/manage.py makemigrations
#sRUN python ~/frontend/cc_proyecto/manage.py runserver