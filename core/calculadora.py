import json, requests

def calcula_pontos(lista):
    
    pontuacao_final=0
    for i in range(len(lista)):
        nome_pokemon        = lista[i]
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

def coleta_base_experience(lista):
    lista_base = []
    for i in range(len(lista)):
        nome_pokemon        = lista[i]
        url                 = 'http://pokeapi.co/api/v2/pokemon/'+nome_pokemon+'/'
        response            = requests.get(url)
        data                = json.loads(response.text)
        lista_base.append(data['base_experience'])
    return lista_base

def coleta_img(lista):
    lista_img = []
    for i in range(len(lista)):
        nome_pokemon        = lista[i]
        url                 = 'http://pokeapi.co/api/v2/pokemon/'+nome_pokemon+'/'
        response            = requests.get(url)
        data                = json.loads(response.text)
        lista_img.append(data['sprites']['front_default'])
    return lista_img

