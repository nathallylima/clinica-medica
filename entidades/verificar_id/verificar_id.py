def verificar_id(lista, id_procurado, tipo):
    for item in lista:
        if item['id'] == id_procurado:
            return True
    print(f'{tipo.capitalize()} com ID {id_procurado} não encontrado.')
    return False
