from login.autenticar import login
from login.cadastrar import cadastrar_usuario

print('\n Bem-vindo ao Sistema da Clínica Médica \n')

def menu_login():
    while True:
        try:
            print('\n [1] Cadastrar usuário')
            print(' [2] Login')
            print(' [3] Sair')  

            opc = int(input('Digite o número referente à opção desejada: '))

            if opc == 1:
                cadastrar_usuario()
            elif opc == 2:
                login()
            elif opc == 3:
                print('Encerrando o sistema...')
                exit()
            else:
                print('Digite uma opção válida.\n')

        except ValueError:
            print('Digite uma opção válida.\n')        

menu_login()