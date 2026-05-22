prompt1 = float(input("Qual é o seu saldo?\n "))
prompt = float(input("Insira o valor do empréstimo que você quer fazer:\n "))
def avaliar_emprestimo(valor, valor2):
    if(valor2 > valor * 0.3):
        print("pode fazer um emprestimo nao nego")
        return False
    else:
        print("Pode fazer meu fio")
        return True
avaliar_emprestimo(prompt1, prompt)