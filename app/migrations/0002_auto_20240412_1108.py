# Generated by Django 2.2.6 on 2024-04-12 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camerastatuslog',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
