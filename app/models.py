from django.db import models

# Create your models here.
# Criação das variaveis a serem salvas no modelo
            #   <th scope="col">#</th>
            #   <th scope="col">Modelo</th>
            #   <th scope="col">Marca</th>
            #   <th scope="col">Cor</th>
            #   <th scope="col">Ano</th>
            #   <th scope="col">Serviço</th>
            #   <th scope="col">Entrada</th>
            #   <th scope="col">Pagamento</th>
class Carros(models.Model):
    modelo = models.CharField(max_length=150)
    marca = models.CharField(max_length=100)
    cor = models.CharField(max_length=100)
    ano = models.IntegerField()
    servico = models.IntegerField()
    entrada = models.CharField(max_length=100)
    pagamento = models.CharField(max_length=100)
    


