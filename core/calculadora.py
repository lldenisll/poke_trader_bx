import json, requests

def calcula_pontos(lista):
    
    pontuacao_final=0
    for i in range(len(lista)):
        flat_list = [item for sublist in lista for item in sublist]
        nome_pokemon        = flat_list[i]
        url_valores         = 'http://pokeapi.co/api/v2/pokemon/'+nome_pokemon+'/'
        url_boleanos        = 'https://pokeapi.co/api/v2/pokemon-species/'+nome_pokemon+ '/'
        response_valores    = requests.get(url_valores)
        data_valores        = json.loads(response_valores.text)
        response_boleanos   = requests.get(url_boleanos)
        data_boleanos       = json.loads(response_boleanos.text)
        base_experience     = data_valores['base_experience']
        ataque              = data_valores['stats'][1]['base_stat']
        ataque_especial     = data_valores['stats'][3]['base_stat']
        lendario            = data_boleanos['is_legendary']
        mitico              = data_boleanos['is_mythical']
        if lendario or mitico:
            pontuacao       = (base_experience*2 + ataque + ataque_especial)*10
        else:
            pontuacao       = (base_experience*2 + ataque + ataque_especial)
        pontuacao_final+=pontuacao
    return pontuacao_final