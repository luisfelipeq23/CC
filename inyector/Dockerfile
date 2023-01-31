FROM python:3

# Python no verifica actualizaciones de PIP
ENV PIP_DISABLE_PIP_VERSION_CHECK 1

# Python no (sobre)escribe archivos pyc
ENV PYTHONDONTWRITEBYTECODE 1

# Docker no maneja la salida de Python
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /CC/CC/inyector/

#COPY . /CC/CC/inyector/

EXPOSE 8000:8000