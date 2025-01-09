#Exibir título do programa para o usuário
print ("\nCALCULADORA DE DÍVIDAS\n")

#Solicitando para o usuário o valor da dívida
valor_divida = float(input("Informe o valor (em reais) da divida: "))

#À vista (1 parcela): Exibição de valores para o usuário
valor_vista = valor_divida * 0.8
percentual_juros = 0
print ("\nO valor final da dívida em 1X (à vista) é de R${:.2f}.".format(valor_divida))

#Parcelado: Criando estrutura de repetição
for n_parcelas in range (3, 13, 3):
    if n_parcelas == 3:
        percentual_juros = 0.10
    elif n_parcelas == 6:
        percentual_juros = 0.15
    elif n_parcelas == 9:
        percentual_juros = 0.20
    elif n_parcelas == 12:
        percentual_juros = 0.25

    valor_final = valor_divida + (valor_divida * percentual_juros)
    valor_parcela = valor_divida / n_parcelas
    
    # Parcelado: Exibição de valores para o usuário
    print("O valor final parcelado em {}X é de R${:.2f}, com parcelas de R${:.2f}.".format(n_parcelas, valor_final, valor_parcela))

