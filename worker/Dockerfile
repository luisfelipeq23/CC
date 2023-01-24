FROM python:3

RUN mkdir -p /cc/worker/

COPY . /cc/worker/
RUN pip install -r ./cc/requirements.txt --no-cache-dir --root-user-action=ignore
WORKDIR /cc/worker/
RUN bash -c "source volume/cc_worker/bin/activate"
EXPOSE 9000:9000
WORKDIR /cc/worker/