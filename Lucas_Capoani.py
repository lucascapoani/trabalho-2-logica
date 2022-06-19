# Avaliação 02 individual
# Autor: Lucas Holanda Capoani

# Quando finalizar a tarefa, salve o arquivo com o seu nome_completo

# Esta avaliação deverá ser individual.
# Competências observadas:
#   - Saber interpretar o que foi solicitado;
#   - Conhecer os comando básicos da linguagem python;
#   - Saber utilizar a estrutura de lista da linguagem;
#   - Desenvolver uma solução viável para o problema proposto


'''
Faça um algoritmo que implemente o menu abaixo.

MENU
1- Cadastrar Login e Senha
2- Aumento de 10%
3- Relatório
4- Cadastrar Funcionário
Escolha:

Para implementar seu código você deverá utilizar
as seguintes listas:
login = []
senha = []
funcionarios = ['Pedro' , 'Ana'   , 'Carlos', 'Maria Clara', 'João Antonio']
salarios     = [ 3470.00,  2200.00,  3970.34,  7450.23     ,  5677.33 ]


Descrição:
Na opção 1 - Você deverá cadastrar login e senha nas listas correspondentes.
             Critério: login não poderá se repetir. Verificar se nome consta
             na lista de funcionarios.

Para executar as opções 2 e 3, você deverá validar seu login e senha

Na opção 2 - Após validar login e senha, seu código deverá aumentar
             o salário dos funcionários em 10%. Mas somente
             se o funcionário ganhar abaixo da média em relação
             a lista de salarios.

Na opção 3 - Após confirmar login e senha, você deverá fazer um
             relatório mostrando o nome e o salario, conforme exemplo:

                 Maria Clara  - 7450.23
                 João Antonio - 5677.33
                 Carlos       - 3970.34
                 Pedro        - 3470.00
                 Ana          - 2200.00

Na opção 4 - Você deverá cadastrar o nome e o salário de um
             novo funcionário.

'''

i = 0
login = []
senha = []
funcionarios = ['Pedro' , 'Ana'   , 'Carlos', 'Maria Clara', 'João Antonio']
salarios     = [ 3470.00,  2200.00,  3970.34,  7450.23     ,  5677.33 ]

while True:
    escolha = input(
    '''
    
    MENU
    1- Cadastrar Login e Senha
    2- Aumento de 10%
    3- Relatório
    4- Cadastrar Funcionário
    Escolha: '''
    )

    if escolha == '1':
        nome = input("Digite seu nome de login: ")
        while True:
            if nome in login:
                nome = input("Login em uso. Digite outro: ")
            else:
                break
                
        if nome not in login:
            if nome in funcionarios:
                senha.append(input("Login de Funcionário. Digite a senha: "))
            else:
                senha.append(input("Não é funcionário. Cadastre a senha: "))

        login.append(nome)
        print(f"Seja bem vindo, {nome}. Usuário liberado.")



    if escolha == '2':
        print("Para acessar esta seção, você deve validar seu login e senha. ")
        nome = input("Digite seu login: ")
        num = input("Digite sua senha: ")
        if nome not in login:
            print("Você precisa retornar à opção 1 e criar seu login. ")
        elif num not in senha:
            print("Você precisa retornar à opção 1 e criar sua senha. ")
        else:
            media = sum(salarios)/len(salarios)
            for p in range(len(salarios)):
                if salarios[p] < media:
                    salarios[p] = salarios[p] + (salarios[p]*0.1)
                    print(salarios[p])
                else:
                    print(salarios[p])



    if escolha == '3':
        print("Para acessar esta seção, você deve validar seu login e senha. ")
        nome = input("Digite seu login: ")
        num = input("Digite sua senha: ")
        if nome not in login:
            print("Você precisa retornar à opção 1 e criar seu login. ")
        elif num not in senha:
            print("Você precisa retornar à opção 1 e criar sua senha. ")
        else:
            indices = list(range(len(salarios)))
            indices.sort(key=lambda i: salarios[i])
            ordem_salarios = [salarios[i] for i in indices]
            ordem_funcionarios = [funcionarios[i] for i in indices]
            
            x = len(funcionarios)
            
            for i in range(x-1,-1,-1):
                print((ordem_funcionarios[i])," - ",(ordem_salarios[i]))



    if escolha == '4':
        funcionarios.append(input("Digite o nome de um novo funcionário: "))
        salarios.append(float(input("Digite o salário do funcionário: ")))
        print(funcionarios)
        print(salarios)
