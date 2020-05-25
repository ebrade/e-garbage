from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class Register(models.Model):
    choices = (
        ('Laptop', 'Laptop'),
        ('Computer', 'Computer'),
        ('Phone', 'Phone'),
        ('Radio', 'Radio'),
        ('Charger', 'Charger'),
        ('Speaker','Speaker'),
        ('Printer', 'Printer'),
        ('Headphone', 'Headphone'),
        ('Cables', 'Cables')
    )
    name = models.CharField(max_length=30)
    province = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    sector = models.CharField(max_length=30)
    cell = models.CharField(max_length=30)
    village = models.CharField(max_length=30)
    street = models.CharField(max_length=50)
    e_waste_type = models.CharField(max_length=30, choices=choices)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    timestamp = models.DateTimeField(auto_now_add=True)


