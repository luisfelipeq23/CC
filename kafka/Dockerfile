FROM bitnami/kafka
COPY ./properties/server.properties /opt/bitnami/kafka/config/
COPY ./properties/producer.properties /opt/bitnami/kafka/config/
COPY ./properties/consumer.properties /opt/bitnami/kafka/config/

# Set environment variables
ENV KAFKA_HOME /opt/bitnami/kafka
ENV PATH $PATH:$KAFKA_HOME/bin
ENV ALLOW_PLAINTEXT_LISTENER=yes
ENV ALLOW_ANONYMUS_LOGIN=yes

WORKDIR $KAFKA_HOME/bin

ENTRYPOINT ["kafka-server-start.sh", "/opt/bitnami/kafka/config/server.properties"]
