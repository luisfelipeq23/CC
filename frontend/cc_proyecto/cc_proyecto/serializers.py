from rest_framework import serializers
from cc_app import models

class RepoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Repo
        fields = '__all__'