alturaTotal = 20
alturaMin = 0.1
metade = 0

while alturaTotal > alturaMin:
    metade = alturaTotal / 2
    alturaTotal = metade
    print(alturaTotal)
    if(alturaTotal == alturaMin):
        print(f"{alturaTotal} eh isso ai")
        break