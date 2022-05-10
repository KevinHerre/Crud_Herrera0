from django.db import models
from django.forms import CharField


class Usuario(models.Model) :
    name = models.CharField(max_length=100, blank = False , null = False)
    last_name = models.CharField(max_length=100, blank = False , null = False)
    age = models.CharField(max_length=100, blank = False , null = False)
    email = models.CharField(max_length=100, blank = False , null = False)

    def __str__(self) :
        return self.name   

