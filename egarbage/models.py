from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
from egarbage.regions import RwandaRegions


class Register(models.Model):
    choices = (
        ('Laptop', 'Laptop'),
        ('Computer', 'Computer'),
        ('Phone', 'Phone'),
        ('Radio', 'Radio'),
        ('Charger', 'Charger'),
        ('Speaker', 'Speaker'),
        ('Printer', 'Printer'),
        ('Headphone', 'Headphone'),
        ('Cables', 'Cables')
    )

    name = models.CharField(max_length=30)
    e_waste_type = models.CharField(max_length=30, choices=choices)
    province = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    sector = models.CharField(max_length=30)
    cell = models.CharField(max_length=30)
    village = models.CharField(max_length=30)
    street = models.CharField(max_length=50)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    collected = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Submitted'
        verbose_name_plural = 'Submitted'
