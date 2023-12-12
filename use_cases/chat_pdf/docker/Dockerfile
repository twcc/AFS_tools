FROM python:3.10.13-slim

ENV AFS_CLOUD_EMBEDDING=''
ENV API_KEY_EMBEDDING=''
ENV AFS_CLOUD_FFM=''
ENV API_KEY_FFM=''
ENV ENDPOINT_EMBEDDING=''
ENV ENDPOINT_FFM=''
ENV FFM_MODEL_NAME=''

RUN apt update -y; apt install -y build-essential gcc curl procps; rm -rf /var/lib/apt/lists/*
COPY requirements.txt /tmp/requirements.txt
RUN python -m pip install -U pip
RUN python -m pip install -r /tmp/requirements.txt

HEALTHCHECK --interval=5s --timeout=3s \
    CMD curl -fs http://localhost/ || exit 1
EXPOSE 80
CMD ["sleep", "infinity"]
