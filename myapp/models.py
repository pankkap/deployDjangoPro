from msilib import Table
from django.db import models

# Create your models here.

# It is equalant to Table. Table contains field


class Students(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

    def __str__(self):
        return format(self.firstname)
