# Generated by Django 4.0.5 on 2022-07-02 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='position',
            field=models.CharField(max_length=100, null=True),
        ),
    ]