# coding: utf-8
from django.db import models


class Customer(models.Model):
    GENDER_CHOICES = [
        ('', 'Not specified'),
        ('female', 'Female'),
        ('male', 'Male'),
    ]
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=150)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    company = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    latitude = models.DecimalField(
        max_digits=22,
        decimal_places=16,
        null=True,
        blank=True
    )
    longitude = models.DecimalField(
        max_digits=22,
        decimal_places=16,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name_plural = "customers"

    def __str__(self):
        return u"{} {}".format(
            self.first_name,
            self.last_name
        )
