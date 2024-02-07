from django.db import models
from datetime import date, datetime


class Profile(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    weight_initial = models.PositiveIntegerField(null=False)
    weight_goal = models.PositiveIntegerField(null=False)
    daily_ccal = models.PositiveIntegerField(null=False)

    def __str__(self):
        return self.username

    def __repr__(self):
        return str(self)


class Product(models.Model):
    name = models.CharField(max_length=50)
    ccal = models.PositiveIntegerField(null=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)


class ProfilesProducts(models.Model):
    eat_date = models.DateField(blank=True)
    name = models.CharField(max_length=50)
    profile = models.ForeignKey(
        Profile,
        on_delete=models.PROTECT,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)
