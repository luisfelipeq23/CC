FROM bitnami/kafka:latest
COPY server.properties /opt/bitnami/kafka/config/server.properties
EXPOSE 9092
ENTRYPOINT ["kafka-server-start.sh"]
CMD ["/opt/bitnami/kafka/config/server.properties"]
