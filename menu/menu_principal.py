from gerenciadores.gerenciador_funcionario import menu_funcionario
from gerenciadores.gerenciador_medico import menu_medico
from gerenciadores.gerenciador_paciente import menu_paciente
from gerenciadores.gerenciador_consulta import menu_consulta
from main import menu_login

print('GERENCIADOR CLÍNICA MÉDICA')

def gerenciar_menu():
    while True:
        try:
            print('\n --- Menu Principal ---')
            print('[1] Gerenciar Funcionários')
            print('[2] Gerenciar Médicos')
            print('[3] Gerenciar Pacientes')
            print('[4] Gerenciar Consultas')
            print('[5] Voltar ao menu de login')
            print('[6] Sair')

            opc = int(input('Digite o número referente à opção desejada: '))

            if opc == 1:
                menu_funcionario()
            elif opc == 2:
                menu_medico() 
            elif opc == 3:
                menu_paciente()
            elif opc == 4:
                menu_consulta()
            elif opc == 5:
                menu_login()
            elif opc == 6:
                print('Encerrando o programa...')
                exit()
            else:
                print('Digite uma opção válida.')

        except ValueError:
            print('Digite uma opção válida.')

gerenciar_menu()
