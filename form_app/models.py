from django.db import models

class Formular(models.Model):
    jmeno = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    ico = models.CharField(max_length=8)
    class Meta:
        verbose_name_plural = 'formular'


