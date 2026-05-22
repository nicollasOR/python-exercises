poco = 10
subir = 3
escorregar = 2
caracol = 0
while caracol != None:
    caracol += subir
    print(f" o Caracol subiu {subir} metros")
    caracol -= escorregar
    print(f" Mas escorregou {escorregar} metros")
    if(caracol == 10):
        print("subiu tudo")
        print(caracol)
        break
