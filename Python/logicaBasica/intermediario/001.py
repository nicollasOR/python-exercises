# 1. Conta do Restaurante (Divisão Justa)

valor_conta = float(input("Digite o valor total da conta: "))
numero_amigos = int(input("Digite o número de amigos: "))

gorjeta = valor_conta * 0.10
total_com_gorjeta = valor_conta + gorjeta
valor_por_pessoa = total_com_gorjeta / numero_amigos

print(f"\nValor da conta: R$ {valor_conta:.2f}")
print(f"Gorjeta (10%): R$ {gorjeta:.2f}")
print(f"Total com gorjeta: R$ {total_com_gorjeta:.2f}")
print(f"Cada amigo deve pagar: R$ {valor_por_pessoa:.2f}")







## 2. Conversor de Tempo (Minutos para Horas)

minutos_totais = int(input("Digite o tempo em minutos: "))

horas = minutos_totais // 60
minutos = minutos_totais % 60

print(f"{minutos_totais} minutos equivalem a {horas} horas e {minutos} minutos.")


## 3. Calculadora de Salário com Desconto

valor_hora = float(input("Digite o valor ganho por hora: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mes: "))

salario_bruto = valor_hora * horas_trabalhadas
desconto = salario_bruto * 0.08
salario_liquido = salario_bruto - desconto

print(f"\n salario bruto: R$ {salario_bruto:.2f}")
print(f"\n desconto de impostos: R$ {desconto:.2f}")
print(f"\n salario liquido: R$ {salario_liquido:.2f}")


# 4. Consumo de Combustível de Frota

distancia = float(input("Digite a distancia da viagem (km): "))
consumo = float(input("Digite o consumo do carro (km por litro): "))
preco_gasolina = float(input("Digite o preço do litro da gasolina: "))

litros_necessarios = distancia / consumo
custo_total = litros_necessarios * preco_gasolina

print(f"\nLitros necessários: {litros_necessarios:.2f} L")
print(f"Custo total da viagem: R$ {custo_total:.2f}")

# 5. Inversor de Palavras (Truque de Fatiamento)

palavra = input("Digite uma palavra ou frase: ")

palavra_invertida = palavra[::-1]

print(f"Texto invertido: {palavra_invertida}")


# 6. Boletim Detalhado (Formatação de Texto)

nome = input("Digite o nome do aluno: ")
disciplina = input("Digite a disciplina: ")

nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
nota3 = float(input("Digite a 3ª nota: "))
nota4 = float(input("Digite a 4ª nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print("\n BOLETIM ")
print(f"Aluno:      {nome}")
print(f"Disciplina: {disciplina}")
print("\n")
print(f"Nota 1:     {nota1:.1f}")
print(f"Nota 2:     {nota2:.1f}")
print(f"Nota 3:     {nota3:.1f}")
print(f"Nota 4:     {nota4:.1f}")
print("\n")
print(f"Média:      {media:.2f}")
print("\n")


# fsdfsdafsa