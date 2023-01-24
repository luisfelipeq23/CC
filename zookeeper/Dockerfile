FROM bitnami/zookeeper:latest
COPY zoo.cfg /opt/bitnami/zookeeper/conf/zoo.cfg
EXPOSE 2181 2888 3888
ENTRYPOINT ["zkServer.sh start"]
CMD ["/opt/bitnami/zookeeper/conf/zoo.cfg"]


# FROM zookeeper:latest
# COPY zoo.cfg /conf/zoo.cfg
# EXPOSE 2181
# CMD ["zkServer.sh", "start-foreground"]
