lista_funcionarios = []

def cadastrar_funcionario():
    while True:
        id = len(lista_funcionarios)  
        nome = input("Digite o nome do funcionário: ")
        cargo = input("Digite o cargo do funcionário: ")

        try:
            telefone = int(input("Digite o telefone do funcionário: "))
            salario = float(input("Digite o salário do funcionário: "))
        except ValueError:
            print('Erro: Digite apenas números para Telefone e Salário.')
            continue

        escolaridade = input("Digite a escolaridade do funcionário: ")

        funcionario = {
            "id": id,  
            "nome": nome,
            "cargo": cargo,
            "telefone": telefone,
            "salário": salario,
            "escolaridade": escolaridade
        }

        lista_funcionarios.append(funcionario)
        print(f"{nome} cadastrado com sucesso!") 

        while True:
            opcao = input("Deseja adicionar outro funcionário? (Sim/Não) \n").lower()

            if opcao == 'sim':
                break
            elif opcao == 'não':
                return
            else:
                print('Opção inválida.  Responda com "Sim" ou "Não".')


def listar_funcionario():
    print()
    print('=== Funcionários Cadastrados === \n')
    
    if not lista_funcionarios:
        print("Nenhum funcionário cadastrado.\n")
    else:
        for i in lista_funcionarios: 
            print(f'ID: {i["id"]}') 
            print(f'Nome: {i["nome"]}') 
            print(f'Cargo: {i["cargo"]}') 
            print(f'Telefone: {i["telefone"]}') 
            print(f'Salário: {i["salário"]}') 
            print(f'Escolaridade: {i["escolaridade"]}') 
            print('--------------------------') 


def editar_funcionario():
    listar_funcionario()

    if not lista_funcionarios:
        return
    try:
        id_editar = int(input('\nDigite o ID do funcionário que deseja editar: '))
    except ValueError:
        print('Insira um ID válido.')
        return
    
    for funcionario in lista_funcionarios:
        if funcionario['id'] == id_editar:  
            print(f"Funcionário encontrado: ID: {funcionario['id']}, Nome: {funcionario['nome']}")
            
            opcoes = ['nome', 'cargo', 'telefone', 'salário', 'escolaridade']

            while True:
                opcao = input('Informe o que você deseja editar: '
                              '(nome, cargo, telefone, salário, escolaridade)\n').lower()
                
                if opcao in opcoes:
                    if opcao in ['telefone', 'salário']:
                        try:
                            alteracao = int(input(f"Digite o novo {opcao}: "))
                        except ValueError:
                            print(f"O valor para {opcao} deve ser numérico.")
                            continue
                        funcionario[opcao] = alteracao
                    else:
                        alteracao = input(f"Digite o novo {opcao}: ")
                        funcionario[opcao] = alteracao
                    print(f"{opcao.capitalize()} atualizado com sucesso!")
                    return 
                else:
                    print('Informe uma opção válida.')
                    continue 
                
    print(f'Funcionário com ID {id_editar} não encontrado.')


def excluir_funcionario():
    listar_funcionario()

    if not lista_funcionarios:
        return
    
    try:
        id_excluir = int(input("Digite o ID do funcionário que deseja excluir: "))
        
        for funcionario in lista_funcionarios:
            if funcionario['id'] == id_excluir:
                lista_funcionarios.remove(funcionario)
                print(f'Funcionário com ID {id_excluir} foi removido.')
                break
        else:
            print(f'Funcionário com ID {id_excluir} não encontrado.')

    except ValueError:
        print('Digite um número válido para o ID.')

