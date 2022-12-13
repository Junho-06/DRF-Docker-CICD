from django.db import models

class User(models.Model):

    name = models.CharField(max_length=10)
    idf = models.CharField(max_length=15)
    password = models.CharField(max_length=15)