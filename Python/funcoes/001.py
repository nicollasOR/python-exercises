preco = int(input("Insira o preco do produto: "))
desconto = (100 - float(input("Insira o seu cupom de desconto ")))  /100


def aplicandoDesconto():
    if(preco < 100):
        print("O produto pode ter desconto não!")
    else: 
        print("O produto pode ter desconto sim!")
        aplicar_desconto = preco * desconto
        print("O preço passou a ser:", aplicar_desconto)
aplicandoDesconto()
    

