from django.urls import path
from rest_framework import routers
from .views import PokemonsAnalisadosView, PokemonsTrocadosView
from .models import PokemonsAnalisados, PokemonsTrocados

router = routers.DefaultRouter()
router.register('pokemon-analise',PokemonsAnalisadosView,basename='PokemonsAnalisados')
router.register('pokemon-troca',PokemonsTrocadosView,basename='PokemonsTrocados')


urlpatterns=router.urls