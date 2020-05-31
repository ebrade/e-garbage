from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.

class Province(models.Model):
    province = models.CharField(max_length=10)

    def __str__(self):
        return self.province


class District(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    district = models.CharField(max_length=30)

    def __str__(self):
        return self.district


class Sector(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    sector = models.CharField(max_length=30)

    def __str__(self):
        return self.sector


class Cell(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    cell = models.CharField(max_length=30)

    def __str__(self):
        return self.cell


class Village(models.Model):
    cell = models.ForeignKey(Cell, on_delete=models.CASCADE)
    village = models.CharField(max_length=30)

    def __str__(self):
        return self.village


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

    name = models.ForeignKey(User, on_delete=models.CASCADE)
    e_waste_type = models.CharField(max_length=30, choices=choices)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True, related_name='provinces')
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, related_name='districts')
    sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True, related_name='sectors')
    cell = models.ForeignKey(Cell, on_delete=models.SET_NULL, null=True, related_name='cells')
    village = models.ForeignKey(Village, on_delete=models.CASCADE, null=True)
    street = models.CharField(max_length=50)
    collected = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'E-Waste'
        verbose_name_plural = 'E-Waste'


class Contact(models.Model):
    names = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=600)

    class Meta:
        verbose_name = "Received messages"
