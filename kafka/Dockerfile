FROM bitnami/kafka:latest
COPY kafka.properties /opt/bitnami/kafka/config/server.properties
EXPOSE 9092
CMD ["/opt/bitnami/kafka/bin/kafka-server-start.sh", "/opt/bitnami/kafka/config/server.properties"]
