#Exibir título do programa para o usuário
print ("\nVOTAÇÃO DE MELHOR DIA PARA LIVE\n")

#Declarando variáveis dos dias
segunda_feira = 0
terca_feira = 0
quarta_feira = 0
quinta_feira = 0
sexta_feira = 0

#Solicitando número de colaboradores
n_colaboradores = int(input("Por favor, informe o número de colaboradores que vão participar da votação: "))

#Criando estrutura de repetição
for x in range (1, n_colaboradores + 1, 1):
    voto = int(input("\nColaborador {}, por favor, informe o número equivalente ao dia de sua preferência:\n1- Segunda-feira\n2- Terça-feira\n3- Quarta-feira\n4- Quinta-feira\n5- Sexta-feira\n\n".format(x)))

    # Criando condições dos votos
    if voto == 1:
        segunda_feira = segunda_feira + 1
    elif voto == 2:
        terca_feira = terca_feira + 1
    elif voto == 3:
        quarta_feira = quarta_feira + 1
    elif voto == 4:
        quinta_feira = quinta_feira + 1
    elif voto == 5:
        sexta_feira = sexta_feira + 1
    else:
        print("O colaborador {} digitou um número inválido e seu voto será desconsiderado. Caso queira votar novamente, por favor reinicie o programa.\n".format(x))

#Exibindo o resultado para os usuários
if segunda_feira > terca_feira and segunda_feira > quarta_feira and segunda_feira > quinta_feira and segunda_feira > sexta_feira :
    print("\nO dia escolhido pelos colaboradores é SEGUNDA-FEIRA.")
elif terca_feira > segunda_feira and terca_feira > quarta_feira and terca_feira > quinta_feira and terca_feira > sexta_feira :
    print("\nO dia escolhido pelos colaboradores é TERÇA-FEIRA.")
elif quarta_feira > segunda_feira and quarta_feira > terca_feira and quarta_feira > quinta_feira and quarta_feira > sexta_feira :
    print("\nO dia escolhido pelos colaboradores é QUARTA-FEIRA.")
elif quinta_feira > segunda_feira and quinta_feira > terca_feira and quinta_feira > quarta_feira and quinta_feira > sexta_feira :
    print("\nO dia escolhido pelos colaboradores é QUINTA-FEIRA.")
elif sexta_feira > segunda_feira and sexta_feira > terca_feira and sexta_feira > quarta_feira and sexta_feira > quinta_feira :
    print("\nO dia escolhido pelos colaboradores é SEXTA-FEIRA.")

#Em caso de empate:
else:
    print("\nHouve um empate. Por favor entre em contato com a direção ou tentem novamente.")



