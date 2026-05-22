# 2. Conta do Restaurante (Divisão Justa)

valorConta = float(input("Digite o valor da conta chefia: "))
amigos = int(input("Digite a quantidade de amigos: "))

gorjeta = valorConta * 0.10
valorTotal_ = valorConta + gorjeta
valorPessoa = valorTotal_ / amigos

print("Total com gorjeta:", valorTotal_)
print("E cada amigo deve pagar:", valorPessoa)