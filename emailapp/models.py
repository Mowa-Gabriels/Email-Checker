from statistics import mode
from django.db import models


# Create your models here.

class EmailLog(models.Model):
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(unique=True, max_length=40)

    

    class Meta:
        verbose_name = ("Email Log")
        verbose_name_plural = ("Email Logs")

    def __str__(self):
        return self.name

    

