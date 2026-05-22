temperatura = float(input("Insira a tempera em C°: "))
def analisarClima():
    if(temperatura < 15):
        print("Friozao")
    elif(temperatura >= 15 and temperatura <= 25):
        print("ta bao")
    else:
        print("Quente em")


analisarClima()
    