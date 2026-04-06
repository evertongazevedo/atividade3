valor = input("Digite um valor: ")
try:
    num = int(valor)
    print("Quadrado:", num ** 2)
except:
    print("Não é número inteiro")
