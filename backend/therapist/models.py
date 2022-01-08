from django.db import models


class Therapist(models.Model):
    activity = models.IntegerField(default=0) # kiné:50, ...
    name = models.CharField(max_length=100)
    inami_nb = models.CharField(max_length=20)
    bank_account = models.CharField(max_length=20)
    bce = models.CharField(max_length=20)
    address = models.TextField()
    contracted = models.BooleanField(default=False) # conventionné

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
