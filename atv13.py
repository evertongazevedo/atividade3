n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

print("Soma:", n1 + n2)

if n1 > n2:
    print("Maior:", n1)
elif n2 > n1:
    print("Maior:", n2)
else:
    print("São iguais")
