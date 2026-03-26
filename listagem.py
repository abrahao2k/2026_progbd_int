import mariadb
conexao = mariadb.connect(host="localhost", user="root",
                    password="", database="playstore")
cursor = conexao.cursor()

## LISTAGEM DOS DADOS ##########################

cursor.execute("SELECT * FROM apps")

for linha in cursor:
    #print(linha)
    print("Código:\t", linha[0])
    print("Nome:\t", linha[1])
    print("Versão:\t", linha[2])
    print("Preço:\t", linha[3])
    print("---------------------")

cursor.close()
conexao.close()