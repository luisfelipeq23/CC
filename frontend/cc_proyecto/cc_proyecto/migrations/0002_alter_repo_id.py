# Generated by Django 4.1.5 on 2023-01-16 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cc_proyecto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
