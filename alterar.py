## CONEXÃO ##
import mariadb
conexao = mariadb.connect(host="localhost",
    user="root",password="",database="playstore")
cursor = conexao.cursor()

## ALTERAÇÃO ##
cod = input("Código do app: ")
cursor.execute(
    "SELECT * FROM apps WHERE codigo = " + cod)

if cursor.rowcount == 0 :
    print("Código não encontrado.")

else:   # encontrou o código
    print(cursor.fetchone()) # pega 1 item do result
    resp = input("Alterar? (s/n) ")
    if resp == "s" :
        
        coluna = input("Qual coluna? (nome/versao/preco) ")
        
        if coluna in ('nome','versao','preco') :
        
            info   = input("Nova informação: ")
            
            sql= f"""UPDATE apps
                     SET {coluna} = '{info}'
                     WHERE codigo = {cod}; """
            cursor.execute(sql)
            conexao.commit() # confirma exclusão no bd
            print("Alterado com sucesso.")
        
        else:
            print("Coluna inválida.")

cursor.close()
conexao.close()
    
    
    
