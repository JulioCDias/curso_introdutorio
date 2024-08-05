from django.db import models

# Create your models here.


class Produto(models.Model):
    produto = models.CharField(max_length=100)
    preco = models.FloatField()
