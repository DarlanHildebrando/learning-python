from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    cpf = models.CharField(unique=True, max_length=14)

    def str(self):
        return self.user.username