# e-commerce
valor_compra = float(input("Qual é o valor total da compra? "))
booleano_ = input("O cliente é vip? (s/n) ").lower

if valor_compra >= 500 and booleano_ == "s":
    desconto = valor_compra * 0.2
    print("Desconto de 20 aplicado")

elif valor_compra >= 500 and booleano_ == "n":
    desconto = valor_compra * 0.1
    print("Desconto de 10 aplicado")
    
elif valor_compra < 500 and booleano_ == "s":
    desconto = valor_compra * 0.05
    print("desconto de 5 aplicado")

# else:
#     print("nenhum desconto aplicável")
