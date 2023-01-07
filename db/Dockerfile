FROM postgres
ENV POSTGRES_HOST_AUTH_METHOD false

# Contraseña para el ususario 'postgres'
ENV POSTGRES_PASSWORD ""
#p0576r35ql

# Se crea la base de datos
ENV POSTGRES_DB cc_db

# Se crean el usuario y contraseña para dicha BD
ENV POSTGRES_USER cc_user
ENV POSTGRES_PASSWORD ""
#cc_pr0y3c70

# Exposición del puerto por defecto
EXPOSE 5432

CMD service postgresql start

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
