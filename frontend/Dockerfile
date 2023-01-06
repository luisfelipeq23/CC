FROM python3
WORKDIR /CC
COPY . /CC
RUN pip install --no-cache-dir -r frontend/cc_proyecto/requirements.txt
ENV PORT=8000
EXPOSE 8000
RUN python ~/CC/frontend/manage.py makemigrations
RUN python ~/CC/frontend/manage.py runserver