# Generated by Django 4.1.4 on 2022-12-13 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('idf', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
    ]