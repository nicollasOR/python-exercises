taxa_base = 5

distancia = float(input("Qual é a distancia da entrea (em km)?  "))
chovendo = input("está chovendo? ")
madrugada = input("Está de noite? ")

print(f"Taxa base: R$", taxa_base)

if distancia > 5.0:
    taxa_base = taxa_base + 3
    print(f"Adicionado 3 à taxa base, ficando no total de R$", taxa_base)
if chovendo == "sim":
    taxa_base = taxa_base + 4
    print(f"Adicionado 4 à taxa base, ficando no total de R$", taxa_base)

if madrugada == "sim":
    taxa_base = taxa_base + 5
    print(f"Adicionado 5 à taxa base, ficando no total de R$", taxa_base)
