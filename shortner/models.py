from django.db import models

# Create your models here.
class urls(models.Model):
    short = models.CharField(max_length=60,verbose_name="Shorted link")
    actual = models.CharField(max_length=200,verbose_name="Actual url")
    def __str__(self):
        return self.short
