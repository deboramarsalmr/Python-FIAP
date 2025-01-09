#Exibir título do programa para o usuário
print ("\nCALCULADORA DE ALÍQUOTA DE IMPOSTO DE RENDA (IR)\n")

#Solicitando dados ao usuário
tipo_investimento = int(input("Tipos de investimento:\n1- CDB(Certificado de Depósito Bancário)\n2- LCI (Letra de Crédito Imobiliário) \n3- LCA (Letra de Crédito do Agronegócio)\nPor favor, escolha o número correspondente ao tipo de investimento: \n"))

#Criando condições para tipo de investimento
if tipo_investimento == 2 or tipo_investimento == 3:
    print("\nO tipo de investimento escolhido é isento de imposto de renda.")
elif tipo_investimento == 1:
    valor_resgate = float(input("Digite o valor (em reais) a ser resgatado: "))
    if valor_resgate < 0:
        print("O número informado é inválido. Por favor reinicie o programa e tente novamente.")

    # Criando condições para dias investidos
    if valor_resgate > 0:
        dias_investidos = int(input("Digite o número de dias que o valor permaneceu investido: "))
        valor_ir = 0

        if 0 <= dias_investidos <= 180:
            valor_ir = valor_resgate * 0.225
        elif 181 <= dias_investidos <= 360:
            valor_ir = valor_resgate * 0.20
        elif 361 <= dias_investidos <= 720:
            valor_ir = valor_resgate * 0.175
        elif dias_investidos > 720:
            valor_ir = valor_resgate * 0.15
        else:
            print ("Número de dias investidos inválido.")

        # Exibindo resultado para o usuário
        print("O valor do imposto de renda a ser pago é de R${:.2f}.".format(valor_ir))
else:
    print ("\nO número informado é inválido. Por favor reinicie o programa e tente novamente.")



