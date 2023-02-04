from django.db import models

class Repo(models.Model):
    url_repo = models.URLField()
    status = models.CharField(max_length=100, default = "")
    creation_timestamp = models.CharField(max_length=100, null=True, blank=True, default = "")
    worker_start_timestamp = models.CharField(max_length=100, null=True, blank=True, default = "")
    worker_finishing_timestamp = models.CharField(max_length=100, null=True, blank=True, default = "")
    inyector_timestamp = models.CharField(max_length=100, null=True, blank=True, default = "")

    class Meta:
        app_label = 'cc_proyecto'
        db_table = 'cc_cloud_repos'