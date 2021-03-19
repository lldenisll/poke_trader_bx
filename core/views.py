from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import PokemonsAnalisados, PokemonsTrocados
from rest_framework.viewsets import ModelViewSet
from .serializer import PokemonsAnalisadosSerializer, PokemonsTrocadosSerializer


class PokemonsAnalisadosView(ModelViewSet):
    queryset = PokemonsAnalisados.objects.all()          
    serializer_class = PokemonsAnalisadosSerializer

class PokemonsTrocadosView(ModelViewSet):
    queryset = PokemonsTrocados.objects.all()
    serializer_class = PokemonsTrocadosSerializer

