from .funcionario import lista_funcionarios
from .medico import lista_medicos
from .paciente import lista_pacientes

lista_consultas = []

def verificar_id(lista, id_procurado, tipo):
    for item in lista:
        if item['id'] == id_procurado:
            return True
    print(f'{tipo.capitalize()} com ID {id_procurado} não encontrado.')
    return False

def cadastrar_consulta():
    while True:
        id_consulta = len(lista_consultas)

        try:
            id_funcionario = input('Informe ID do funcionário ou "sair" para voltar ao menu: ')
            if id_funcionario.lower() == 'sair':
                return
            id_funcionario = int(id_funcionario)
            if not verificar_id(lista_funcionarios, id_funcionario, "funcionário"):
                continue

            id_medico = input('Informe o ID do médico ou "sair" para voltar ao menu: ')
            if id_medico.lower() == 'sair':
                return
            id_medico = int(id_medico)
            if not verificar_id(lista_medicos, id_medico, "médico"):
                continue

            id_paciente = input('Informe o ID do paciente ou "sair" para voltar ao menu: ')
            if id_paciente.lower() == 'sair':
                return
            id_paciente = int(id_paciente)
            if not verificar_id(lista_pacientes, id_paciente, "paciente"):
                continue

            tipo = input('Digite o tipo da consulta: ')
            observacoes = input('Digite as observações da consulta: ')
            data = input('Digite a data da consulta (dd/mm/aaaa): ')
            
            consulta = {
                "id_consulta": id_consulta,
                "id_funcionario": id_funcionario,
                "id_medico": id_medico,
                "id_paciente": id_paciente,
                "tipo": tipo,
                "observações": observacoes,
                "data": data
            }

            lista_consultas.append(consulta)
            print(f'Consulta {id_consulta} cadastrada com sucesso!')

        except ValueError:
            print('Erro: Digite apenas números para IDs.')
            continue

        while True:
            opcao = input("Deseja adicionar outra consulta? (Sim/Não) \n").lower()
            if opcao == 'sim':
                break
            elif opcao == 'não':
                return
            else:
                print('Opção inválida. Responda com "Sim" ou "Não".')


def listar_consulta():
    print()
    print('Consultas cadastradas: ')

    if not lista_consultas:
        print('Nenhuma consulta cadastrada.')
    else:
        for i in lista_consultas:
            print(f"ID: {i['id_consulta']}") 
            print(f"ID funcionário: {i['id_funcionario']}") 
            print(f"ID médico: {i['id_medico']}") 
            print(f"ID paciente: {i['id_paciente']}")
            print(f"Tipo: {i['observações']}") 
            print(f"Data da consulta: {i['data']}")
            print()


def editar_consulta():
    listar_consulta()
    if not lista_consultas:
        return

    try:
        id_consulta = int(input('Digite o ID da consulta que deseja editar: '))
    except ValueError:
        print('Insira um ID válido.')
        return

    for consulta in lista_consultas:
        if consulta['id_consulta'] == id_consulta:
            print(f'Consulta encontrada ID: {consulta["id_consulta"]}')

            opcoes = ['tipo', 'observações', 'data']
            opcao = input('Informe o que você deseja editar: (tipo, observações ou data)\n').lower()

            if opcao in opcoes:
                alteracao = input(f'Digite o novo {opcao}: ')
                consulta[opcao] = alteracao
                print(f"{opcao.capitalize()} atualizado com sucesso!")
                return 

    print(f'Consulta com ID {id_consulta} não encontrada.')


def excluir_consulta():
    listar_consulta()
    if not lista_consultas:
        return
    
    try:
        id_consulta = int(input('Digite o ID da consulta que deseja excluir: '))

        for consulta in lista_consultas:
            if consulta['id_consulta'] == id_consulta:
                lista_consultas.remove(consulta)
                print(f'Consulta com ID {id_consulta} foi removida')
                break
        else:
            print(f'Consulta com ID {id_consulta} não encontrada')

    except ValueError:
        print('Digite um número válido para o ID.')

