FROM mysql:latest
COPY my.cnf /etc/mysql/conf.d/my.cnf
EXPOSE 3306
ENTRYPOINT ["mysqld"]
#RUN echo "CREATE DATABASE mydatabase; GRANT ALL PRIVILEGES ON mydatabase.* TO 'cc_user'@'%'; FLUSH PRIVILEGES;" | mysql -uroot -prootpassword
CMD ["--defaults-file=/etc/mysql/conf.d/my.cnf"]


# FROM postgres:12
# ENV POSTGRES_HOST_AUTH_METHOD false
# RUN pg_createcluster -p 5432 -u postgres 12 cc_cluster
# RUN pg_ctlcluster 12 cc_cluster start
# Contraseña para el ususario 'postgres'
# ENV POSTGRES_PASSWORD cc_pass
# p0576r35ql

# Se crea la base de datos
# ENV POSTGRES_DB cc_db

# Se crean el usuario y contraseña para dicha BD
# ENV POSTGRES_USER cc_user
# ENV POSTGRES_PASSWORD cc_pass

# Exposición del puerto por defecto
# EXPOSE 5432

# CMD service postgresql start

#CMD ["/bin/bash", "-c", "docker run --name cc_db --network cc_network -e POSTGRES_PASSWORD='' -e POSTGRES_PASSWORD='' -d cc_db"]

#FROM ubuntu

#ENV TZ=Europe/Madrid

# Instalar postgresql
#RUN apt-get update && apt-get install -y postgresql postgresql-contrib

# Create DB y usuario
#RUN service postgresql start && su postgres -c "createuser -s cc_user" && su postgres -c "createdb cc_db"

#EXPOSE 5432

# Iniciar PostgreSQL cuando se ejecuta el contenedor
#CMD service postgresql start
