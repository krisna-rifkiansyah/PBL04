from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.model}) - {self.brand}"
