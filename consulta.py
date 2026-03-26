import mariadb
conexao = mariadb.connect(host="localhost", user="root",
                    password="", database="playstore")
cursor = conexao.cursor()

## PESQUISA DOS DADOS ##########################

prog = input("Nome do programa: ")

sql = f'''SELECT * FROM apps
          WHERE nome LIKE '%{prog}%' '''

cursor.execute(sql)

for linha in cursor:
    #print(linha)
    print("Código:\t", linha[0])
    print("Nome:\t", linha[1])
    print("Versão:\t", linha[2])
    print("Preço:\t", linha[3])
    print("---------------------")

cursor.close()
conexao.close()