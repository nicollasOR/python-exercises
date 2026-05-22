# tabuada = int(input("Insira seu número: "))

# for i in range(1, 11):
#     print("O numero ", tabuada, " quando multiplicado por ", i, " É igual a ", i)


# soma = 0

# for i in range(1, 6):
#     prompt = int(input("Coloque seu novo numero: "))
#     print("Aqui está seu numero ", prompt)

# while True:
#     prompt = int(input("1 - Continuar // 2 - Sair  "))
#     if(prompt == 1 or prompt == "1"):
#         print("você escolheu continuar!")
#     elif(prompt == 2 or prompt == "2"):
#         break
#     else:
#         print("Escolha apenas o número da opção.")

# print("----------- Insira as notas de sua Aluna --------")
# prompt = 0
# for i in range(1, 5):
#     prompt += float(input(f"Insira a {i} º nota da aluna: "))

# print(f"A média final da aluna é {prompt / 4}")


# prompt = int(input("Digite um numero e irei imprimir a quantidade de vezes dele! \n"))

# for i in range(0, prompt):
#     print(prompt)

# prompt = int(input("Digite um numero e irei imprimir todos os numeros pares dele \n"))
# for i in range(1, prompt):
#     if(i % 2 == 0):
#         print(i)

# saldoAtual = 500
# while saldoAtual == 500:
#     prompt = int(input("Você deseja qual opção? \n 1 - Sacar \n 2 - Sair \n"))
#     if(prompt == 2):
#         saldoAtual += .000000000001
#         break
#     if(prompt == 1):
#         saque = float(input("Insira o valor de Saque: "))
#         saldoAtual -= saque
