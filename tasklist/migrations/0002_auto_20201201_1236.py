# Generated by Django 3.1.3 on 2020-12-01 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasklist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefas',
            name='status',
            field=models.BooleanField(),
        ),
    ]