from django.db import models

class Calamity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=255)

class MitigationStrategy(models.Model):
    calamity = models.ForeignKey(Calamity, on_delete=models.CASCADE)
    strategy = models.TextField()
