num = int(input("Digite um número: "))
if num == 0:
    print("Neutro")
elif num > 0 and num % 2 == 0:
    print("Par positivo")
elif num > 0:
    print("Ímpar positivo")
elif num < 0 and num % 2 == 0:
    print("Par negativo")
else:
    print("Ímpar negativo")
