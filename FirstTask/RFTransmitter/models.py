# RFTransmitter/models.py

from django.db import models

class User(models.Model):
    TYPE_CHOICES = (
        ('Type 1', 'Type 1'),
        ('Type 2', 'Type 2'),
        ('Type 3', 'Type 3'),
    )
    FREQUENCY_CHOICES = (
        ('Frequency 1', 'Frequency 1'),
        ('Frequency 2', 'Frequency 2'),
        ('Frequency 3', 'Frequency 3'),
    )

    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    frequency = models.CharField(max_length=50, choices=FREQUENCY_CHOICES)
    prf = models.CharField(max_length=100)
    pw_usec = models.IntegerField()

    def __str__(self):
        return f"{self.type} - {self.frequency}"
