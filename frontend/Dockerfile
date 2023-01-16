FROM python:3
# Python no verifica actualizaciones de PIP
ENV PIP_DISABLE_PIP_VERSION_CHECK 1

# Python no (sobre)escribe archivos pyc
ENV PYTHONDONTWRITEBYTECODE 1

# Docker no maneja la salida de Python
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /CC/CC/frontend/

COPY . /CC/CC/frontend/
WORKDIR /CC/CC/frontend/
RUN pip install -r ./cc_proyecto/requirements.txt --no-cache-dir --root-user-action=ignore
RUN bash -c "source cc/bin/activate"
EXPOSE 8000:8000
WORKDIR /CC/CC/frontend/cc_proyecto/