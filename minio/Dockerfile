FROM minio/minio
EXPOSE 9000
EXPOSE 9090
ENV MINIO_ROOT_USER=cc_minio_user
ENV MINIO_ROOT_PASSWORD=cc_m1n10_p455
ENV MINIO_STORAGE_USE_HTTPS=False
RUN curl https://dl.min.io/client/mc/release/linux-amd64/mc --create-dirs -o $HOME/minio-binaries/mc
RUN chmod +x $HOME/minio-binaries/mc
ENV PATH=$PATH:$HOME/minio-binaries/
CMD ["minio", "server", "/cc/minio/volume/"]
