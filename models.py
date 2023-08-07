from django.db import models

# makemigrations -create changes and store in file
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class contact(models.Model):
    email = models.CharField(max_length=122)
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)

def __str__(self):
    self.name
