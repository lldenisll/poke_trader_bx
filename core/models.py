from django.db import models
import requests, json
from django.contrib.postgres.fields import ArrayField
from .calculadora import calcula_pontos, coleta_img, coleta_base_experience

class PokemonsTrocados(models.Model):
    pokemon_user            =   ArrayField(models.TextField(max_length=30, blank=True),size=6,)
    pokemon_troca           =   ArrayField(models.TextField(max_length=30, blank=True),size=6,)
    pokemon_img_user        =   ArrayField(models.TextField(max_length=30,blank=True),size=6, blank=True,editable=False)
    pokemon_base_user       =   ArrayField(models.TextField(max_length=30,blank=True),size=6,blank=True,editable=False)
    pokemon_img_troca       =   ArrayField(models.TextField(max_length=30,blank=True),size=6,blank=True,editable=False)
    pokemon_base_troca      =   ArrayField(models.TextField(max_length=30,blank=True),size=6,blank=True,editable=False)

    def save(self, *args, **kwargs):
        self.pokemon_img_user = coleta_img(self.pokemon_user)
        self.pokemon_base_user = coleta_base_experience(self.pokemon_user)
        self.pokemon_img_troca = coleta_img(self.pokemon_troca)
        self.pokemon_base_troca = coleta_base_experience(self.pokemon_troca)
        super(PokemonsTrocados, self).save(*args, **kwargs)

class PokemonsAnalisados(models.Model):
    pokemon_user            =   ArrayField(models.TextField(max_length=30, blank=True),size=6,)
    pokemon_troca           =   ArrayField(models.TextField(max_length=30, blank=True),size=6,)
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
        
