from django.db import models


SUPER_POWER = (
    ('FLY', 'FLY'),
    ('RUN FAST', 'RUN FAST'),
    ('SHOOTING WEB', 'SHOOTING WEB'),
    ('STRONG', 'STRONG'),
)

class Hero(models.Model):
    name = models.CharField(max_length=20)
    alias = models.CharField(max_length=100)
    super_power = models.CharField(choices=SUPER_POWER, max_length=50)

    def __str__(self):
        return self.name, self.alias, self.super_power


class Villian(models.Model):
    name = models.CharField(max_length=20)
    alias = models.CharField(max_length=100)
    super_power = models.CharField(choices=SUPER_POWER, max_length=50)
    against = models.CharField(max_length=50)

    def __str__(self):
        return self.name, self.alias, self.super_power, self.against