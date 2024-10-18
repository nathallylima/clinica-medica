from entidades.paciente import *

def menu_paciente():
    while True:
        try:
            print('\n --- Gerenciador de Pacientes ---')
            print('[1] Cadastrar')
            print('[2] Editar')
            print('[3] Excluir')
            print('[4] Exibir')
            print('[5] Voltar ao menu principal')
            print('[6] Sair')

            opc = int(input('Digite o número referente à opção desejada: '))

            if opc == 1:
                cadastrar_paciente()
            elif opc == 2:
                editar_paciente()
                input('Pressione Enter para voltar ao menu...')
            elif opc == 3:
                excluir_paciente()
                input('Pressione Enter para voltar ao menu...')
            elif opc == 4:
                listar_paciente()
                input('Pressione Enter para voltar ao menu...')
            elif opc == 5:
                return
            elif opc == 6:
                print('Encerrando o programa...')
                exit()
            else:
                print('Digite uma opção válida.')

        except ValueError:
            print('Digite uma opção válida.')