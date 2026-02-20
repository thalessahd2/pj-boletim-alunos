dict_boletim_alunos = {}
indice_alunos = 0

def imprimir_menu():
    print('****** Boletim de Alunos Colégio THD ******')
    print('1 - Visualizar boletins')
    print('2 - Visualizar boletim individual')
    print('3 - Cadastrar boletim')
    print('4 - Excluir boletim')
    print('5 - Importar boletim')
    print('6 - Exportar boletim')
    print('0 - Sair')

def imprimir_boletim(boletim):
    situacao = 'APROVADO' if boletim['is_aprovado'] else 'REPROVADO'
    status = 'MATRÍCULA ATIVA' if boletim['is_ativo'] else 'MATRÍCULA INATIVA'

    print(
        f'ID: {boletim['id']}\n'
        f'Nome: {boletim['nome']}\n'
        f'Idade: {boletim['idade']}\n'
        f'Nota: {boletim['nota']}\n'
        f'Situação: {situacao}\n'
        f'Status: {status}\n'
    )

def solicitar_enter():
    enter = input('Precione ENTER para continuar...')
    print('')
    return enter

def cadastrar_boletim(id_atual):
    nome_aluno = input('Nome do aluno: ')
    idade_aluno = int(input('Idade do aluno: '))
    nota_aluno = float(input('Nota do aluno: '))

    novo_id_aluno = id_atual + 1
    obj_aluno = {
        'id': novo_id_aluno,
        'nome': nome_aluno,
        'idade': idade_aluno,
        'nota': nota_aluno,
        'is_aprovado': nota_aluno > 6.0,
        'is_ativo': True
    }

    dict_boletim_alunos[obj_aluno['id']] = obj_aluno
    print(f'>> O boletim de {obj_aluno['nome']} foi cadastrado com sucesso com id = {obj_aluno['id']} <<')
    solicitar_enter()

    return novo_id_aluno

def visualizar_boletim(id):
    boletim = dict_boletim_alunos.get(id)
    if (boletim):
        print(f'****** Boletim de {boletim['nome']} ******')
        imprimir_boletim(boletim)
    else:
        print('>> Boletim não encontrado <<')
    solicitar_enter()

def visualizar_boletins():
    if not dict_boletim_alunos:
        print('>> Nenhum boletim cadastrado no sistema <<')
    else: 
        for id in dict_boletim_alunos:
            boletim = dict_boletim_alunos[id]
            imprimir_boletim(boletim)

    solicitar_enter()

def imprimir_aviso():
    print('>> Funcionalidade ainda não implementada nessa versão <<')
    solicitar_enter()

imprimir_menu()
opcao = int(input('Escolha uma opção: '))
while (opcao > 0):
    match opcao:
        case 1:
            print('****** Visualizar boletins ******')
            visualizar_boletins()
        case 2:
            print('****** Visualizar boletim ******')
            input_id = int(input('Digite o id do boletim: '))
            visualizar_boletim(input_id)
        case 3:
            print('****** Cadastrar boletim ******')
            indice_alunos = cadastrar_boletim(indice_alunos)
        case 4:
            imprimir_aviso()
        case 5:
            imprimir_aviso()
        case 6:
            imprimir_aviso()
        case _:
            print('Opção inválida, tente novamente')
            solicitar_enter()

    imprimir_menu()
    opcao = int(input('Escolha uma opção: '))

print('>> Boletim de Alunos Colégio THD Encerrado <<')