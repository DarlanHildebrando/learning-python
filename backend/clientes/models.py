from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)

    def str(self):
        return self.user.username
