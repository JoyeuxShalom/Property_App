from tkinter.constants import CASCADE

from django.db import models

class Property(models.Model):
    APARTMENT = 'Apartment'
    HOUSE = 'House'
    COMMERCIAL = 'Commercial'
    PROPERTY_TYPE_CHOICES = [
        (APARTMENT, 'Apartment'),
        (HOUSE, 'House'),
        (COMMERCIAL, 'Commercial'),
    ]
    name = models.CharField(max_length=500)
    address = models.TextField()
    property_type = models.CharField(max_length=500, choices=PROPERTY_TYPE_CHOICES)
    description = models.TextField()
    number_of_units = models.PositiveIntegerField()

    def _str_(self):
        return self.name

class Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    unit_number = models.CharField(max_length=100)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    rent = models.DecimalField(max_digits=50, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def _str_(self):
        return f'Unit {self.unit_number} - {self.property.name}'

class Tenant(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)

    def _str_(self):
        return self.name

class Lease(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    rent_amount = models.DecimalField(max_digits=50, decimal_places=2)

    def _str_(self):
        return f'{self.tenant.name} - {self.unit}'

