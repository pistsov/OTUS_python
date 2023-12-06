from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    weight_initial = models.PositiveIntegerField(null=False)
    weight_goal = models.PositiveIntegerField(null=False)
    daily_ccal = models.PositiveIntegerField(null=False)

    def __str__(self):
        return self.username


class Product(models.Model):
    name = models.CharField(max_length=32)
    ccal = models.PositiveIntegerField(null=False)

    def __str__(self):
        return self.name