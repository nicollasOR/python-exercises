mes = int(input("Digite o seu mes (1 a 12): "))

if mes <= 3 and mes>=0:
    print("Primeiro tri")
if mes <= 6 and mes>=4:
    print("segundo tri")
if mes <= 12 and mes>=8:
    print("terceiro tri")
else:
    print("mes invalido")