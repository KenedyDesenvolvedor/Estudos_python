frase = "Eu amo comer amoras no café da manhã"

print("Contagem direta: ", frase.count("amo"))

contador = 0
lista_termos = frase.split()
for termo in lista_termos:
    if termo == "amo":
        contador += 1
print("Contagem correta: ", contador)