usuarios = {'admin': 'admin123'}


def cadastrar_usuario():
    while True:
        usuario = input('\nDigite o nome de usuário que deseja cadastrar (ou "sair" para cancelar): ').lower()
        if usuario.lower() == 'sair':  
            print('Cadastro cancelado.')
            break
        
        senha = input('Digite a senha (ou "sair" para cancelar): ')
        if senha.lower() == 'sair': 
            print('Cadastro cancelado.')
            break


        if usuario in usuarios:
            print(f'Nome de usuário "{usuario}" já está cadastrado. Tente novamente ou faça o login.\n')
        else:
            usuarios[usuario] = senha
            print(f'Usuário "{usuario}" cadastrado com sucesso.\n')
            break 
