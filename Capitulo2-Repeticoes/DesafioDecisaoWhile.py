resposta="SIM"
while resposta=="SIM":
    nivel=input("Digite o seu nivel de acesso: ").upper()
    if nivel=="ADM" or nivel=="USR":
        genero=input("Digite o seu genero: ").upper()
        if nivel=="ADM":
            if genero=="FEMININO":
                print("Olá administradora!")
            else:
                print("Olá administrador!")
        else:
            if genero=="FEMININO":
                print("Olá usuária!")
            else:
                print("Olá usuário!")
    elif nivel=="GUEST":
        print("Ola visitante!")
    else:
        print("Olá desconhecido(a)!")
    resposta=input("Digite SIM para continuar: ").upper()
