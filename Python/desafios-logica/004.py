def eh_primo(numero):
    for i in range(1, 10):
        numero = (i % 2 == i)
        print(f" Eh primo, o numero: {numero}")
        break       


print(eh_primo(1))
