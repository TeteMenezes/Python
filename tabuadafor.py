#Esther Laura
limite1 = int(input("Digite o Primeiro Número"))
limite2 = int(input("Digite o Segundo Número"))

limiteInferior = min(limite1, limite2)
limiteSuperior = max(limite1, limite2)

soma = 0
for i in range(limiteInferior, limiteSuperior + 1):
    if i % 2 == 0:
        soma += 1

print(f"A soma dos números pares entre {limiteInferior} e {limiteSuperior} é: {soma}")