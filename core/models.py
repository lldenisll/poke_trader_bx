from django.db import models
import requests, json
from django.contrib.postgres.fields import ArrayField
from .calculadora import calcula_pontos

class PokemonsTrocados(models.Model):
    pokemon_user            =   ArrayField(ArrayField(models.TextField(max_length=10, blank=True),size=1,),size=6,)
    pokemon_troca           =   ArrayField(ArrayField(models.TextField(max_length=10, blank=True),size=1,),size=6,)


class PokemonsAnalisados(models.Model):
    pokemon_user            =   ArrayField(ArrayField(models.TextField(max_length=10, blank=True),size=1,),size=6,)
    pokemon_troca           =   ArrayField(ArrayField(models.TextField(max_length=10, blank=True),size=1,),size=6,)
    veredito                =   models.BooleanField(editable=False)
  
    def calcula_veredito(self):
        pontos_user         = calcula_pontos(self.pokemon_user)
        pontos_troca        = calcula_pontos(self.pokemon_troca)
        diferenca           = max(pontos_user,pontos_troca)/min(pontos_troca,pontos_user)
        if diferenca < 1.1:
            return True 
        else:
            return False 
    def save(self, *args, **kwargs):
        self.veredito = self.calcula_veredito()
        super(PokemonsAnalisados, self).save(*args, **kwargs)
