from django.db import models

class Repo(models.Model):
    nombre_repo = models.CharField(max_length=255)
    url_repo = models.URLField()

    class Meta:
        app_label = 'cc_proyecto'
        db_table = 'cc_cloud_repos'