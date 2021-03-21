from django.test import TestCase
from calculadora import calcula_pontos
import unittest

def verificar_troca(lista1, lista2):
    pontos_user         = calcula_pontos(lista1)
    pontos_troca        = calcula_pontos(lista2)
    diferenca           = max(pontos_user,pontos_troca)/min(pontos_troca,pontos_user)
    if diferenca < 1.1:
        return True 
    else:
        return False 

class TestPokemonTrade(unittest.TestCase):

    def test_troca_true(self):
#Uma troca entre 2 grupos de pokemons próximos, de acordo com o clustering feito no jupyter, tem que ser consideradas justas pelo algoritmo 
# Os 2 grupos abaixo, além de serem do mesmo cluster, tem uma distância muito pequena entre eles

        #Pokemons próximos no cluster 3, o mais poderoso de acordo com o algorítmo
        lista1_cluster_3 = ['mew','moltres','azelf'] 
        lista2_cluster_3 = ['mesprit','ho-oh','uxie']
        #Pokemons próximos no cluster 14, o menos poderoso de acordo com o algorítmo
        lista1_cluster_14 = ['pidgey','unfezant','pikipek']
        lista2_cluster_14 = ['spearow','staraptor','fletchling']
        #Esses pokemons são muito próximos, portanto a resposta deve ser true (troca justa)
        self.assertTrue(verificar_troca(lista1_cluster_3,lista2_cluster_3))
        self.assertTrue(verificar_troca(lista1_cluster_14,lista2_cluster_14))

    def test_troca_false(self):
        lista1_cluster_3 = ['mew','moltres','azelf'] 
        lista1_cluster_14 = ['pidgey','unfezant','pikipek']
        lista2_cluster_14 = ['spearow','staraptor','fletchling']
        # Agora estamos testando pokemons opostos, uma troca entre pokemons do cluster 3 com o cluster 14 não pode ser justa
        self.assertFalse(verificar_troca(lista1_cluster_3,lista1_cluster_14))
        self.assertFalse(verificar_troca(lista1_cluster_3,lista2_cluster_14))

if __name__ == '__main__':
    unittest.main()
