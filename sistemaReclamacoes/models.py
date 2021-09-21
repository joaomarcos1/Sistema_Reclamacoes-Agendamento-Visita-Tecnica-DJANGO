from django.db import models
from django.contrib import auth
import re
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core import validators

# Create your models here.
class Tecnico_Campo(models.Model):
    id = models.TextField()
    nome = models.TextField()
    telefone = models.TextField()

    def setId(self, ident):
        self.id = ident

    def getId(self, ident):
        return self.id

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setTelefone(self,telefone):
        self.telefone = telefone

    def getTelefone(self):
        return self.telefone





