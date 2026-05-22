idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("acesso liberado")

elif idade == 19:
    print("elif")

else:
    print("acesso negado")

cor = input("digite a cor do semáforo (verde/ amarelo / vermelho): ")

if cor == "verde":
    print("pode passar")

elif cor == "amarelo":
    print("vá com calma")

elif cor == "vermelho":
    print("Acelera com tudo")
else:
    print("cor inválida")

print("--- financiamento veiculo ---")
    
salario = float(input("Digite seu salário em R$: "))
nome_limpo = input("seu nome está limpo? (s/n): ").lower()

if salario >= 2000 and nome_limpo == "s":
    print("Financiamento aprovved")
else:
    print("Negado")