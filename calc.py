import os

#Criar menu
def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('*'*13, 'Python Calculator', '*'*13)
    print('''
    1) Adição
    2) Subtração
    3) Multiplicação
    4) Divisão
    ''')

def escolherOpcao():
    opcao = 999
    while opcao > 5:
        opcao = int(input('Selecione uma operacao (1, 2, 3 ou 4) ou 5 para sair: '))
    
    if opcao == 5: 
        return
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))

    if opcao == 1: soma(n1, n2)
    elif opcao == 2: subtracao(n1, n2)
    elif opcao == 3: multiplicacao(n1, n2)
    elif opcao == 4: divisao(n1, n2)

def soma(a, b):
    print(f'{a} + {b} = {a+b}')

def subtracao(a, b): 
    print(f'{a} - {b} = {a-b}')

def multiplicacao(a, b): 
    print(f'{a} X {b} = {a*b}')

def divisao(a, b): 
    if b == 0: 
        print('Não pode dividir um número por 0.')
    else:
        print(f'{a} / {b} = {a/b}')


#funções de Adição, Subtração, Multiplicação e Divisão

if __name__ == '__main__':
    while(True):
        menu()
        escolherOpcao()
        continuar = ''
        while(continuar.upper() not in('S', 'N')):
            continuar = input('Deseja sair? (s/n): ')

        if continuar.upper() == 'S':
            break
        elif continuar.upper() != 'N':
            print('Digite uma opção válida!')
        else:
            continue
