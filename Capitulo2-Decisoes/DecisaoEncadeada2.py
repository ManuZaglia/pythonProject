nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença ifecto-contagiosa? ").upper()

#PRIMEIRO PROBLEMA A SER RESOLVIDO
if doenca_infectocontagiosa=="SIM":
        print("Encaminhe o paciente para a sala AMARELA")
elif doenca_infectocontagiosa=="NAO":
        print("Encaminhe o paciente para a sala BRANCA")
else:
        print("Responda a suspeita de doença infecto-contagiosa com SIM OU NAO")

#SEUNDO PROBLEMA A SER RESOLVIDO

if idade>=65:
    print("Paciente COM prioridade")
else:
    genero=input("Digite o genero do paciente: ").upper()
    if genero=="FEMININO" and idade>10:
        gravidez=input("A paciente está gravida? ").upper()
        if gravidez=="SIM":
            print("Paciente COM prioridade")
        else:
            print("PAciente SEM prioridade")
    else:
        print("Paciente SEM prioridade")