FROM python:3.10.13

ENV CRAWL_DOMAINS='tws.twcc.ai, twsc.twcc.ai'
ENV AFS_CLOUD_EMBEDDING=''
ENV API_KEY_EMBEDDING=''
ENV AFS_CLOUD_FFM=''
ENV API_KEY_FFM=''
ENV ENDPOINT_EMBEDDING=''
ENV ENDPOINT_FFM=''
RUN mkdir -p /home/ubuntu && apt-get update && apt-get install lsof -y
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh



EXPOSE 80

CMD ["sleep", "infinity"]
