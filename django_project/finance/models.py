from django.db import models
from django.utils import timezone

class Company(models.Model):
    Name = models.CharField(primary_key=True, max_length=50, default='Undefined')


class Historical_data(models.Model):
    Date = models.DateField(primary_key=True, default=timezone.now)
    Open = models.FloatField()
    High = models.FloatField()
    Low = models.FloatField()
    Close = models.FloatField()
    Volume = models.IntegerField()
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, null=False)

