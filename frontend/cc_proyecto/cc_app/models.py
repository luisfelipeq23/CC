from django.db import models

class Repo(models.Model):
    nombre_repo = models.CharField(max_length=255)
    url_repo = models.URLField()
    estados = [("Pendiente", "En espera", "En Proceso", "Terminado")]
    estado = models.CharField(choices=estados)

    class Meta:
        app_label = 'cc_app'