from django.db import models

# Create your models here.
class Stock_model(models.Model):
    capacity=models.IntegerField(max_length=15)
    number=models.IntegerField(max_length=15)
    open=models.IntegerField(max_length=15)
    high=models.IntegerField(max_length=15)
    low=models.IntegerField(max_length=15)
    close=models.IntegerField(max_length=15)
    change=models.IntegerField(max_length=15)
    transaction=models.IntegerField(max_length=15)
    def __str__(self) -> str:
        return self.name