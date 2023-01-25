from django.db import models


class Transaction(models.Model):
    class Meta:
        ordering = ["id"]

    type = models.CharField(max_length=1)
    date = models.DateField()
    value = models.DecimalField(max_digits=8, decimal_places=2)
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.TimeField(auto_now=False, auto_now_add=False)
    store_owner = models.CharField(max_length=255)
    store_name = models.CharField(max_length=255)


# Create your models here.
