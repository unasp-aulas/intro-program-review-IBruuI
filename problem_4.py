valor_casa = float(input("Qual o valor da casa? "))  # Não alterar
salario = float(input("Qual é o salário? "))  # Não alterar
anos_pagar = int(input("Pagar em quantos anos? "))  # Não alterar

prestacao = valor_casa/(12*anos_pagar)

if prestacao > salario * 0.3:
    print("Reprovado")
else:
    print("Aprovado")
