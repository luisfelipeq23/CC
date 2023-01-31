FROM python:3

# Python no verifica actualizaciones de PIP
ENV PIP_DISABLE_PIP_VERSION_CHECK 1

# Python no (sobre)escribe archivos pyc
ENV PYTHONDONTWRITEBYTECODE 1

# Docker no maneja la salida de Python
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /CC/CC/kafka_client/volume

WORKDIR /CC/CC/kafka_client

RUN python3 -m venv cc_venv_kafkaclient
RUN . cc_venv_kafkaclient/bin/activate

COPY requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir --root-user-action=ignore

WORKDIR /CC/CC/kafka_client/
