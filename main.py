import json

dict_boletim_alunos = {}
indice_alunos = 0

def imprimir_menu():
    print('\n----------------------------------------')
    print('         MENU - BOLETINS THD')
    print('----------------------------------------')
    print('1  • Visualizar boletins')
    print('2  • Visualizar boletim individual')
    print('3  • Cadastrar boletim')
    print('4  • Excluir boletim')
    print('5  • Importar boletins')
    print('6  • Exportar boletins')
    print('0  • Sair')
    print('----------------------------------------\n')

def imprimir_boletim(boletim):
    situacao = 'APROVADO' if boletim['is_aprovado'] else 'REPROVADO'
    status = 'MATRÍCULA ATIVA' if boletim['is_ativo'] else 'MATRÍCULA INATIVA'

    titulo_boletim = f"Boletim de {boletim['nome']}"
    print('\n' + titulo_boletim)
    print('-' * len(titulo_boletim) + '\n')

    print(
        f"ID: {boletim['id']}\n"
        f"Nome: {boletim['nome']}\n"
        f"Idade: {boletim['idade']}\n"
        f"Nota: {boletim['nota']}\n"
        f'Situação: {situacao}\n'
        f'Status: {status}'
    )

def solicitar_enter():
    input('\nAperte ENTER para continuar...')

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
    print(f"\n• O boletim de {obj_aluno['nome']} foi cadastrado com sucesso (ID: {obj_aluno['id']}) •")
    solicitar_enter()

    return novo_id_aluno

def excluir_boletim(id):
    boletim = dict_boletim_alunos.get(id)
    if (boletim):
        boletim['is_ativo'] = False
        print(f"\n• O boletim de {boletim['nome']} foi excluído com sucesso •")
    else:
        print('\n• Boletim não encontrado •')
    solicitar_enter()

def visualizar_boletim(id):
    boletim = dict_boletim_alunos.get(id)
    if (boletim):
        imprimir_boletim(boletim)
    else:
        print('\n• Boletim não encontrado •')
    solicitar_enter()

def visualizar_boletins():
    if not dict_boletim_alunos:
        print('• Nenhum boletim cadastrado no sistema •')
    else:
        nenhum_boletim_ativo = True 
        for id in dict_boletim_alunos:
            boletim = dict_boletim_alunos[id]
            if (boletim['is_ativo']):
                nenhum_boletim_ativo = False
                imprimir_boletim(boletim)
        if nenhum_boletim_ativo:
            print('• Nenhum boletim ativo no sistema •')

    solicitar_enter()

def exportar_boletins(nome_arq):
    if not dict_boletim_alunos:
        print(f'\n• Nenhum boletim cadastrado no sistema •')
    else:
        nome_arq_json = nome_arq + '.json'
        with open(nome_arq_json, 'w', encoding='utf-8') as f:
            json.dump(dict_boletim_alunos, f, ensure_ascii=False, indent=4)

        print(f'\n• {nome_arq_json} gerado com sucesso •')
    solicitar_enter()

def imprimir_aviso():
    print('\n• Funcionalidade ainda não implementada nessa versão •')
    solicitar_enter()

imprimir_menu()
opcao = int(input('Escolha uma opção: '))
while (opcao > 0):
    match opcao:
        case 1:
            print('\n=== Visualizar Boletins ===\n')
            visualizar_boletins()
        case 2:
            print('\n===  Visualizar Boletim ===\n')
            input_id = int(input('Digite o id do boletim: '))
            visualizar_boletim(input_id)
        case 3:
            print('\n===  Cadastrar Boletim ===\n')
            indice_alunos = cadastrar_boletim(indice_alunos)
        case 4:
            print('\n===  Excluir Boletim ===\n')
            input_id = int(input('Digite o id do boletim que será excluído: '))
            excluir_boletim(input_id)
        case 5:
            imprimir_aviso()
        case 6:
            print('\n===  Exportar Boletins ===\n')
            nome_arq = input('Nome do arquivo a ser criado: ')
            exportar_boletins(nome_arq)
        case _:
            print('\n• Opção inválida, tente novamente •')
            solicitar_enter()

    imprimir_menu()
    opcao = int(input('Escolha uma opção: '))

print('\n• Boletim de Alunos Colégio THD Encerrado •\n')