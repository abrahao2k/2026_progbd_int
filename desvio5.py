# Calcule a média de 2 notas digitadas pelo usuário
# e mostre o resultado.
# Se a média for 6 ou mais, diga APROVADO,
# caso contrário, diga REPROVADO.
n1 = float(input("Nota1: "))
n2 = float(input("Nota2: "))

med = (n1+n2)/2
print("Média=", med)

if med >= 6:
    print("APROVADO")
else:
    print("REPROVADO")