nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença ifecto-contagiosa? ").upper()
if idade>=65:
    print("O paciente COM prioridade ")
    if doenca_infectocontagiosa=="SIM":
        print("Encaminhe o paciente para a sala AMARELA")
    elif doenca_infectocontagiosa=="NAO":
        print("Encaminhe o paciente para a sala BRANCA")
    else:
        print("Responda a suspeita de doença infecto-contagiosa com SIM OU NAO")
else:
    print("Paciente SEM prioridade")
    if doenca_infectocontagiosa=="SIM":
        print("Encaminhe o paciente para a sala AMARELA")
    elif doenca_infectocontagiosa=="NAO":
        print("Encaminhe o paciente para a sala BRANCA")
    else:
        print(" Responda a suspeita de doença infecto-contagiosa com SIM OU NAO")
