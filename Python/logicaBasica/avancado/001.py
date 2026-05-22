valor = input("Insira seu numero de 3 digitos: ")

if len(valor) == 3:
    valor = int(valor)

    valorUni = valor % 10
    valorDez = (valor // 10) % 10
    valorCent = valor // 100

    print(valorUni)
    print(valorDez)
    print(valorCent)
else:
    print("Tem que ser exatamente 3 digitos")