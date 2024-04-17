from controller import Cadastro, Login


while True:
    print('==========[MENU do usuário]==========')
    print('[1] Cadastro\n[2] Logar\n[3] Sair')
    escolha = input('Informe sua escolha: ').lower()
    
    if escolha == '1':
        nome = input('Informe seu nome: ')
        email = input('Informe seu email: ')
        senha = input('Informe sua senha: ')

        if nome and email and senha:
            resultado = Cadastro.cadastrar(nome, email, senha)
            if resultado == 1:
                print('Usuário cadastrado com sucesso...')
            elif resultado == 2:
                print('Nome deve ser menor...')
            elif resultado == 3:
                print('Email precisa ter entre 10 a 50 caracteres...')
            elif resultado == 4:
                print('Senha precisa ser de 6 a 50 caracteres...')
            elif resultado == 5:
                print('Usuário já possui cadastro...')
            else:
                print('Ocorreu um erro!')
        else:
            print('Preencha todos os campos corretamente...')
    elif escolha == '2':
        email = input('Informe seu email: ')
        senha = input('Informe sua senha: ')

        if email and senha:
            logar = Login.login(email, senha)
            if logar == False:
                print('Usuário ou senha inválidos...')
            else:
                print('Usuário logado com sucesso...')
        else:
            print('Preencha todos os campos para realizar o login...')
    elif escolha == '3':
        print('Obrigado por usar nosso sistema...')
        break
    
