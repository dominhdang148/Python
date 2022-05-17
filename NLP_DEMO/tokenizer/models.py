from django.db import models
import numpy as np
import underthesea as uds
# class result(models.Model):
#     word=models.CharField(max_length=255)

class Sentece(models.Model):
    inputsent=models.CharField(max_length=255)
    