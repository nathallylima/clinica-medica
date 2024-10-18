from .cadastrar import usuarios

def login():
    usuario = input('\nUsuário: ').lower()
    senha = input('Senha: ')

    if usuario in usuarios:
        if usuarios[usuario] == senha:
            print('Entrada bem-sucedida\n')
            from menu.menu_principal import gerenciar_menu
            gerenciar_menu()
        else:
            print('Senha incorreta, tente novamente.')
    else:
        print('Usuário não encontrado, tente novamente.')

            
        