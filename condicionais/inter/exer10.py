num = int(input("Digite seu primeiro nº: "))
num2 = int(input("Digite seu segundo nº: "))
num3 = int(input("Digite seu terceiro nº, sendo ele menor que os dois anteriores: "))

if num > num3 and num2 > num3:
    print("é um triangulo")
else:
    print("Não é um triangulo")