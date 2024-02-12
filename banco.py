menu =   '''
[d] - depositar.
[s] - sacar.
[e] - extrato.
[q] - sair.

=> '''

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao.lower() == 'd':
        valor_deposito = float(input('Informe o valor do deposito: '))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f'Deposito: R${valor_deposito:.2f}\n'
        else:
            print('Valor inválido')  

    elif opcao.lower() == 's':
        valor_saque = float(input('Informe o valor do Saque: '))


        exedeu_saldo = valor_saque > saldo

        exedeu_limite = valor_saque > limite

        exedeu_saque = numero_de_saques >= LIMITE_SAQUE


        if exedeu_saldo:
            print('O valor do saque é maior que o valor disponovel na conta.')

        elif exedeu_limite:
            print('Operação falhou! O valor de saque excede o limite')   

        elif exedeu_saque:
            print('O numero de saques deve ser de 3 ao dia')

        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f'Saque: R${valor_saque}\n'
            numero_de_saques += 1
            print(f'Saque realizado. saldo atual: {saldo}')

        else:
            print('Valor inválido')    

    elif opcao.lower() == 'e':
        print('\n#==========Extrato==========#')
        print('Não foram realizada operações' if not extrato else extrato)
        print(f'\nSaldo: R${saldo:.2f}')
        print('#=============================#')

    elif opcao.lower() == 'q':
        print('Você saiu!')
        break    

    else:
        print('Opção inválida!')    
