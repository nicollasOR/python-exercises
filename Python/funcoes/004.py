def imc_calc(peso, altura):
    return peso / (altura * altura)

def imc_classificar(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif(imc >= 18.5 and imc <= 24.9):
        return "Peso normal"
    else:
        return "Sobrepeso"

prompt = float(input("Insira seu peso: "))
prompt2 = float(input("Insira sua altura: "))


valorFinal = imc_calc(prompt, prompt2)
classificar = imc_classificar(valorFinal)

print(f"Seu imc é de {valorFinal:.2f} e sua classificacao é: {classificar}")