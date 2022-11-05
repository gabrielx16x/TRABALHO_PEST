from time import sleep
#As mudanças feitas nesse arquivo foram as seguintes: coloquei inputnum em vários locais e o  bendito else em vários locais, mas falta eu puxar outras coisas do trabalhodepest3.py
carros = list()
dados_car= dict()
dados_user = list()
usuarios = dict()
teste = dict()
teste['Login'] = 0

def menu_principal():
   
   print('-'*49) 
   print()
   print('---------- Bem vindo a concessionária! ----------')
   print()
   print('-'*49)
   while True:
    p = inputnum('1-Cadastrar usuário\n2-Login\nDigite 1 ou 2: ', erro='Erro!!!\n1-Cadastrar usuário\n2-Login\nDigite 1 ou 2: ')
  
    if p == 1:
        cadastrar_user()
    elif p == 2 and len(usuarios)>1:
        login()        
    elif p == 2:
        while len(usuarios) == 0:
            print("Erro!! Nenhum usuário cadastrado!!!")
            
            p = inputnum('1-Cadastrar usuário\n2-Login\nDigite 1 ou 2: ', erro='Erro!!!\n1-Cadastrar usuário\n2-Login\nDigite 1 ou 2: ')
            if p == 1:
                cadastrar_user()
            elif p == 2 and len(usuarios)>1:
                login()
            else:
                print("Função não encontrada!!!")
                sleep(2)
                menu_principal()
    else:
        print('Função não encontrada!!!')
        sleep(2)
        menu_principal()
        



def cadastrar_user():
    a = 1
    while a == 1:
        usuarios.clear() 
        nome_user = input('Digite o nome de usuário: ').title().strip().split()#nome completo
        while len(nome_user) < 2:
            print('Erro!! Adicione pelo menos nome e sobrenome')
            nome_user = input('Digite o nome de usuário: ').title().strip().split()
        nome_user = ' '.join(nome_user)
        usuarios['Usuário'] = nome_user
        print(usuarios['Usuário'])
        p = inputtexto('Digite C p/ comprador ou V p/ vendedor: ', erro='Erro!!! Digite C ou V\nDigite C p/ comprador ou V p/ vendedor: ')
        while p != "C" and p != "V":
            print('Função não encontrada')
            p = inputtexto('Digite C p/ comprador ou V p/ vendedor: ', erro='Erro!!! Digite C ou V\nDigite C p/ comprador ou V p/ vendedor: ')
        if p == "C":
            usuarios['Comp/Vend']= p
            perg = inputtexto('Digite P p/ PCD ou N p/ normal: ', erro='Erro!!! Digite P ou N\nDigite P p/ PCD ou N p/ normal: ')
            while perg != "P" and perg != "N":
                print('Função não encontrada')
                perg = inputtexto('Digite P p/ PCD ou N p/ normal: ', erro='Erro!!! Digite P ou N\nDigite P p/ PCD ou N p/ normal: ')
            if perg == "N":
                usuarios['Normal/PCD']= perg
            elif perg == "P":
                usuarios['Normal/PCD']= perg
            else:
                print('Função não encontrada')
                
        elif p == "V":
            usuarios['Comp/Vend']= p
            
        else:
            print("Função não encontrada!!!")
            
        while True:
            a,b,c,d = 0,0,0,0
            pass_user = str(input('Digite a sua senha: '))
            if (len(pass_user)>=8):
                for i in pass_user:
                    if (i.islower()):
                        a+=1
                    if (i.isupper()):
                        b+=1
                    if (i.isdigit()):
                        c+=1
                    if (i == '@' or i == '$' or i == '_' or i == '.' or i == '#'):
                        d+=1 

            if a >= 1 and b >=1 and c >= 1 and d >= 1 and a+b+c+d == len(pass_user):
                usuarios['Senha']= pass_user
                dados_user.append(usuarios.copy())
                print(dados_user)
                break
            
            else:
                print('Erro!!!!')

        pergunta=1 
        while pergunta == 1:
            pergunta = inputnum('Digite 1 p/ cadastrar outro usuário ou 2 p/ voltar ao menu principal: ', erro="Erro!!!\nDigite 1 p/ cadastrar outro usuário ou 2 p/ voltar ao menu principal: ")
                #while len(pergunta) == 0:
                    #print('Nada digitado!!')
                    #pergunta = input('Digite 1 p/ cadastrar outro usuário ou 2 p/ voltar ao menu principal: ').strip()
            if pergunta == 1:
                    cadastrar_user()
            elif pergunta == 2:
                    menu_principal()
            else:
                print('Função não encontrada!!!')
                
    
       
       
def login():
    while True:
        print(dados_user)
        nome_user = inputtexto('Digite o nome do usuário: ', erro='Erro!!!\nDigite o nome de usuário: ')
        for valor in dados_user:
            if nome_user == valor["Usuário"]:
                print('Ok')
                break
            else:
                print('Digite um usuário válido!!')
                '''if nome_user in usuarios['Usuário'] and nome_user in dados_user:#nome_user == usuarios['Usuário']
                print('Tudo certo')'''
            '''if nome_user not in usuarios['Usuário'] or nome_user != usuarios['Usuário']:
                print('Digite um usuário válido!')
                nome_user = inputtexto('Digite o nome do usuário: ', erro='Erro!!!\nDigite o nome de usuário: ')'''
            '''if nome_user in usuarios['Usuário'] or nome_user == usuarios['Usuário']:
                print('Tudo certo')'''
                
        while True:
            pass_user = inputtexto('Digite a senha do usuário: ', erro='Erro!!!\nDigite a senha do usuário: ')
            for valor in dados_user:
                if valor['Senha']== pass_user:
                    print('Login Ok!!')
                    z = 2
                    if nome_user == usuarios['Usuário'] and usuarios['Comp/Vend'] == 'V' :
                        menu_vendedor()
                    elif nome_user == usuarios['Usuário'] and usuarios['Comp/Vend'] == 'C':
                        menu_comprador()
                        teste['Login']=1
                else:
                    print('Digite uma senha válida.')
                    pass_user = inputtexto('Digite a senha do usuário: ', erro='Erro!!!\nDigite a senha do usuário: ')
        
        #como procurar se é comprador ou vendedor no dicionário de acordo com o usuário...
#criar uma chave, com dict teste e verificar se está logado(1) ou não (0).
      
        
def menu_comprador():
    print('-'*41)
    print()
    print('----------Bem vindo ao menu comprador----------')
    print()
    print('-'*41)
    p = 1
    while p == 1:
        perg = inputnum("Digite 1 p/ consultar e 2 p/ ir para o menu principal: ", erro="Erro!!!\nDigite 1 p/ consultar e 2 p/ ir para o menu principal: ")
      
        if perg == 1:
            consultar()
        elif perg == 2:
            menu_principal()
        else:
            print('Função não encontrada!!!')
            
        p = inputnum("Deseja continuar digite 1 p/ sim e 2 p/não: ", erro="Erro!!!\nDeseja continuar digite 1 p/ sim e 2 p/não: ")
        if p == 1:
            menu_comprador()
        elif p == 2:
            menu_principal()
        else:
            print('Função não encontrada!!!')
    
def menu_vendedor():
    print('-'*40 )
    print('----------Bem vindo ao menu vendedor----------')
    print('-'*40)
    
    p = 1
    while p == 1:
        perg = inputnum("Digite 1 p/ cadastrar um carro e 2 p/ editar: ", erro="Erro!!!\nDigite 1 p/ cadastrar um carro e 2 p/ editar: ")
        
            
        if perg == 1:
            cadastrar_carro()
            
        elif perg == 2:
            editar_carro()
        else:
            print('Função não encontrada!!!')
        p = inputnum("Deseja continuar? Digite 1 p/sim e 2 p/não: ", erro="Erro!!!\nDeseja continuar? Digite 1 p/sim e 2 p/não: ")
        if p == 1:
            menu_vendedor()
        elif p == 2:
            print('Tudo bem!!!')
            menu_principal()
        else:
            print('Função não encontrada!!!')
        
            
def cadastrar_carro():
    # Nome do carro(modelo), marca, (normal ou PCD),  preço, quantidade, ano
    # Se o ano for igual ao que estamos, criar chave com conteúdo "Novo", se não for igual será adicionado em "Usado" e aind criará a chave km rodados e pedirá ao usuário os km rodados que o carro tem)
    # Sempre tem que perguntar se quer continuar naquele mesmo tipo de escolha, talvez use o inputescolha
    p = 1
    while p == 1:
        dados_car.clear()
        pergunta = inputnum('Digite 1 se for PCD e se 2 não for: ', erro='Erro digite 1 ou 2!!\nDigite 1 se for PCD e 2 se não for: ')
        
        if pergunta == 1:
            mod_carro = inputtexto('Digite o nome do carro: ',erro='Erro!\nDigite o nome do carro: ')
           
            if mod_carro in carros:
                print('Já existe esse carro...')
            elif mod_carro not in carros:
                dados_car['Modelo PCD']= mod_carro
                
            marca_carro = inputtexto("Digite a marca do carro: ", erro="Erro!!!\nDigite a marca do carro: ")
            if marca_carro in carros:
                print('Essa marca já está cadastrada.')
            elif marca_carro not in carros:
                dados_car['Marca PCD'] = marca_carro
            
            preco_carro = inputfloat('Digite o preço do carro: ', erro='Erro!!!\nDigite o preço do carro: ')
            dados_car['Preço PCD']= preco_carro
            
            quant_carro = inputnum('Digite a quantidade de carros disponíveis: ',erro='Erro!!!\nDigite a quantidade de carros disponíveis: ')
            dados_car['Quantidade PCD']= quant_carro
            ano_carro()
            
            '''ano_car = inputnum('Digite o ano do carro: ',erro='Erro!!!\nDigite o ano do carro: ')
            if ano_car == 2022:
                dados_car['Ano PCD'] = 'Novo'
                
            elif ano_car < 2022:
                dados_car['Ano PCD'] = 'Usado'
                dados_car['Km rodados'] = inputfloat('Digite os Km rodados do carro: ', erro='Erro!!!\nDigite os Km rodados do carro: ')
            
            elif ano_car > 2022:
                print('Ano inválido')'''
        
                
        if pergunta == 2:
            mod_carro = inputtexto('Digite o nome do carro: ',erro="Erro\nDigite o nome do carro: ")#inputtexto tudo que tiver esse strip
         
            if mod_carro in carros:
                print('Esse modelo já está cadastrado...')
            if mod_carro not in carros:
                dados_car['Modelo não PCD'] = mod_carro
                
            marca_carro =inputtexto("Digite a marca do carro: ", erro="Erro\nDigite a marca do carro: ")
           
            if marca_carro in carros:
                print('Essa marca já está cadastrada...')
            if marca_carro not in carros:
                dados_car['Marca não PCD'] = marca_carro
            preco_carro = inputfloat('Digite o preço do carro: ', erro='Erro!!!\nDigite o preço do carro: ')
            dados_car['Preço não PCD']= preco_carro
            
            quant_carro = inputnum('Digite a quantidade de carros disponíveis: ',erro='Erro!!!\nDigite a quantidade de carros disponíveis: ')
            dados_car['Quantidade não PCD']= quant_carro
            ano_carro_no_pcd()  
            
            '''ano_car =inputnum('Digite o ano do carro: ', erro='Erro!!!\nDigite o ano do carro: ')
            if ano_car == 2022:
                dados_car['Ano não PCD'] = 'Novo'
            elif ano_car != 2022:
                dados_car['Ano não PCD'] = 'Usado'
                dados_car['Km rodados'] = inputfloat('Digite os Km rodados do carro: ', erro='Erro!!!\nDigite os Km rodados do carro: ')'''  
        else:
            print('Função não encontrada...')
        
        
        p = inputnum('Quer continuar?\n1-Sim\n2-Não\nResp: ',erro='Erro!!! Apenas 1 ou 2...\nQuer continuar?\n1-Sim\n2-Não\nResp: ')        
        if p == 1:
            cadastrar_carro()
        elif p == 2:
            carros.append(dados_car.copy())
            print(carros)
            menu_principal()
        else:
            print('Função não foi encontrada!!')
        
            
def editar_carro():
    carro_pcd = list()
    carro_no_pcd = list()
    for carro in carros:
        if carro['Para PCD'] == 'Sim':
            carro_pcd.append(carro)
        else:
            carro_no_pcd.append(carro)
    p = 1
    while p == 1:
        pergunta = inputnum('Digite 1 p/ editar o carro para PCD e 2 para editar se não for: ', erro='Erro!!!\nDigite 1 p/ editar o carro para PCD e 2 para editar se não for: ')
        if pergunta == 1:
            for i in carro_pcd:
                print(i)
                
    
def consultar():
    pass

def ano_carro():
    
    ano_car = inputnum('Digite o ano do carro: ',erro='Erro!!!\nDigite o ano do carro: ')

    if ano_car == 2022:
        dados_car['Ano PCD'] = 'Novo'
        
    elif ano_car < 2022:
        dados_car['Ano PCD'] = 'Usado'
        dados_car['Km rodados'] = inputfloat('Digite os Km rodados do carro: ', erro='Erro!!!\nDigite os Km rodados do carro: ')
    
    elif ano_car > 2022:
        print('Ano inválido')
        ano_carro()
        
def ano_carro_no_pcd():
    
    ano_car = inputnum('Digite o ano do carro: ',erro='Erro!!!\nDigite o ano do carro: ')

    if ano_car == 2022:
        dados_car['Ano não PCD'] = 'Novo'
        
    elif ano_car < 2022:
        dados_car['Ano não PCD'] = 'Usado'
        dados_car['Km rodados'] = inputfloat('Digite os Km rodados do carro: ', erro='Erro!!!\nDigite os Km rodados do carro: ')
    
    elif ano_car > 2022:
        print('Ano inválido')
        ano_carro_no_pcd()

#FUNÇÕES TRATAMENTO DE ERROS 

def pedir_texto(texto, escolhas, erro):
    resposta = str(input(texto)).title()
    while resposta != escolhas[0] and resposta != escolhas[1]:
        print(erro)
        resposta = str(input(texto)).title()
    return resposta
def espaco(texto):
    espacos = 0
    for i in range(0, len(texto)):
        if texto[i:i+1] == ' ':
            espacos += 1
    if espacos == len(texto):
       return True
    else:
       return False

def inputtexto(texto, erro):
    resposta = input(texto)
    while True:
        try:
            resposta = int(resposta)
            resposta = input(erro)
        except:
            if espaco(resposta):
                resposta = input(erro)
            else:
                return resposta
            
def inputnum(texto, erro):
    resposta = input(texto)
    while True:
        try:
            resposta = int(resposta)
            return resposta
        except:
            resposta = input(erro)
            
def temCaractere(texto):
    caracteres = [".", "'", '"', "!", "@", "#", "$", "%", "¨", "&", "*", "(", ")", "-", "_", "=", "+", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "´", "`", ".", ",", ";", ":", "[", "]", "{", "}", "/", ">", "<", "?", "§", "¢", "£", "¬", "^", "~"]
    for caractere in caracteres:
        if str(caractere) in texto:
            return True
    return False

def inputfloat(texto, erro):
    resposta = input(texto)
    while True:
        try:
            resposta = float(resposta)
            return resposta
        except:
            resposta = input(erro)
            
def clear():
    from os import system, name 
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def inputEscolha(texto, escolhas, erro):
    res = input(texto).title()
    if len(escolhas) == 2:
        while res != escolhas[0] and res != escolhas[1]:
            print(erro)
            res = input(texto).title()
        if res == escolhas[0]:
            return escolhas[0]
        else:
            return escolhas[1]

menu_principal()
