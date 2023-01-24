FROM python:3

RUN bash -c "source volume/cc_worker/bin/activate"

RUN mkdir -p /cc/worker/volume

COPY . /cc//worker/

RUN pip install -r ./cc/requirements.txt --no-cache-dir --root-user-action=ignore

WORKDIR /cc/worker/

EXPOSE 9000:9000

WORKDIR /cc/worker/