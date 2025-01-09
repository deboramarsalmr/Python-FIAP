#Exibir título do programa para o usuário
print ("\nCALCULADORA DE PARCELAMENTO DE CARROS\n")

#Solicitando para o usuário o valor do carro
valor_carro = float(input("Informe o valor (em reais) do carro desejado: "))

#À vista: Exibição de valores para o usuário
valor_vista = valor_carro * 0.8
print ("\nO valor final do carro à vista (desconto de 20%) é de R${:.2f}.".format(valor_vista))

#Parcelado: Criando estrutura de repetição
for n_parcela in range (6, 61, 6):
    acrescimo = n_parcela * 0.005
    valor_final = valor_carro + (valor_carro * acrescimo)
    valor_parcela = valor_final / n_parcela

#Parcelado: Exibição de valores para o usuário
    print("O valor final parcelado em {}X é de R${:.2f}, com parcelas de R${:.2f}.".format(n_parcela, valor_final, valor_parcela))
