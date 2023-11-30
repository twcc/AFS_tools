FROM python:3.10.13

ENV CRAWL_DOMAINS=''
ENV CRAWL_START_URL=''
ENV AFS_CLOUD_EMBEDDING=''
ENV API_KEY_EMBEDDING=''
ENV AFS_CLOUD_FFM=''
ENV API_KEY_FFM=''
ENV ENDPOINT_EMBEDDING=''
ENV ENDPOINT_FFM=''
ENV FFM_MODEL_NAME=''
RUN mkdir -p /home/ubuntu && apt-get update && apt-get install lsof -y
COPY docker-entrypoint.sh /docker-entrypoint.sh
COPY requirements.txt /tmp/requirements.txt
RUN python -m pip install -U pip
RUN python -m pip install -r /tmp/requirements.txt
RUN ln -s /home/ubuntu/AFS_tools/use_cases/webcrawler_chatbot/commands /commands
RUN chmod +x /docker-entrypoint.sh
RUN apt-get clean autoclean; apt-get autoremove --yes; rm -rf /var/lib/{apt,dpkg,cache,log}/

EXPOSE 80
HEALTHCHECK CMD curl --fail http://localhost/_stcore/health

CMD ["sleep", "infinity"]
