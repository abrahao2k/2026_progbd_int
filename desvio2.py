# pergunta a idade e diz se é
# criança, adolescente ou adulto
idade = int(input("Digite sua idade: "))

if idade <= 11:
    print("Você é criança.")

# if idade >= 12:
#     if idade <= 17:
#         print("Você é adolescente.")

if 12 <= idade <= 17 :      #intervalo simplificado
    print("Você é adolescente.")

if idade >= 18:
    print("Você é adulto.")