clientes = list()
pessoa = dict()
while True:
    print('-='*30)
    print('1 para cadastrar novo cliente\n2 para buscar dados do cliente\n3 para excluir cliente do sistema\n4 para encerrar operação')
    while True:
        op = int(input('Informe o numero referente a sua função: '))
        if op >= 1 and op <= 4:
            break
        else:
            print('ERRO! Digite um numero referente as operações')
    if op == 4:
        break
    elif op == 1:
        print('--'*20)
        print('Cadastrando cliente')
        pessoa['Nome'] = str(input('Nome: '))
        pessoa['Idade'] = int(input('Idade: '))
        pessoa['Contato'] = int(input('Telefone de contato: '))
        pessoa['Cpf'] = int(input('CPF: '))
        print('Cadastro finalizado!')
        clientes.append(pessoa.copy())
        pessoa.clear()
    elif op == 2:
        buscacpf = int(input('CPF: '))
        for i, v in enumerate(clientes):
            if clientes[i]['Cpf'] == buscacpf:
                print('Dados do cliente {}: '.format(clientes[i]['Nome']))
                print(clientes[i])
                break
            elif i == len(clientes)-1:
                print('CPF não cadastrado')
    elif op == 3:
        removecpf = int(input('Informe o cpf do cliente: '))
        for i,v in enumerate(clientes):
            if clientes[i]['Cpf'] == removecpf:
                print(clientes[i])
                while True:
                    resp = str(input('Deseja remover {} do sistema? [S/N]'.format(clientes[i]['Nome']))).upper().strip()[0]
                    if resp in 'SN':
                        break 
                    else:
                        print('ERRO! Digite um valor S ou N')
                if resp in 'S':
                    clientes.pop(i)
                    print('cliente removivo do sistema')
                    print(clientes)
            elif i == len(clientes)-1:
                print('Cliente não cadastrado')
print('Encerrado!')
print('Lista de clientes atual: ')
print(clientes)