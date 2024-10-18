usuarios = {'admin': 'admin123'}


def cadastrar_usuario():
    while True:
        usuario = input('\nDigite o nome de usuário que deseja cadastrar (ou "sair" para cancelar): ').lower()
        if usuario.lower() == 'sair':  # Opção para sair do loop
            print('Cadastro cancelado.')
            break
        
        senha = input('Digite a senha (ou "sair" para cancelar): ')
        if senha.lower() == 'sair':  # Opção para sair do loop
            print('Cadastro cancelado.')
            break


        if usuario in usuarios:
            print(f'Nome de usuário "{usuario}" já está cadastrado. Tente novamente ou faça o login.\n')
        else:
            usuarios[usuario] = senha
            print(f'Usuário "{usuario}" cadastrado com sucesso.\n')
            print(usuarios)
            break  # Cadastro feito, sair do loop


def login():
    usuario = input('\nUsuário: ').lower()
    senha = input('Senha: ')

    if usuario in usuarios:
        if usuarios[usuario] == senha:
            print('Entrada bem-sucedida\n')
            from menu.menu_principal import gerenciar_menu
            gerenciar_menu()
        else:
            print('Senha incorreta.')
    else:
        print('Login incorreto.')

            
        