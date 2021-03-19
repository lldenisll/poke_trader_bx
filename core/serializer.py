from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import PokemonsAnalisados, PokemonsTrocados

class PokemonsAnalisadosSerializer(ModelSerializer):
    class Meta:
        model = PokemonsAnalisados
        fields = ('__all__')
class PokemonsTrocadosSerializer(ModelSerializer):
    class Meta:
        model = PokemonsTrocados
        fields = ('__all__')