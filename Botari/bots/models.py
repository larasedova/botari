from django.db import models

# Create your models here.


class Bot(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class Scenario(models.Model):
    bot = models.ForeignKey(Bot, related_name='scenarios', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    data = models.JSONField()

class Step(models.Model):
    scenario = models.ForeignKey(Scenario, related_name='steps', on_delete=models.CASCADE)
    order = models.IntegerField()
    content = models.TextField()
