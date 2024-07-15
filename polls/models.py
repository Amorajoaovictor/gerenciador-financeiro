from django.db import models


# Create your models here.
MONTH_CHOICES = (
    ("JANUARY", "January"),
    ("FEBRUARY", "February"),
    ("MARCH", "March"),
    ("DECEMBER", "December"),
)

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200,)
    month = models.CharField(max_length=9,
    choices=MONTH_CHOICES,
    default="JANUARY")
    def __str__(self):
        return self.username
    
class Contribuinte(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    rendaBruta = models.IntegerField()
    contribuicao_previdenciaria = models.IntegerField()
    despesas_medicas = models.IntegerField()
    numero_dependentes = models.IntegerField()
    def __str__(self):
        return self.nome