## CONEXÃO COM O BD ##
import mariadb

conexao = mariadb.connect(host="localhost",
                          user="root",
                          password="",
                          database="restaurante")

cursor = conexao.cursor()

## CADASTRAR ########
def cadastrar():
    prato = input("Nome do prato: ")
    valor = input("Valor: ").replace(',','.')
    sql = f'''INSERT INTO cardapio VALUES(
            null, '{prato}', {valor}); '''
    cursor.execute(sql)
    conexao.commit()
    print("GRAVADO COM SUCESSO.\n\n")

## PESQUISAR ##########
def pesquisar():
    prato = input("Nome do prato: ")
    sql = f'''SELECT * FROM cardapio
              WHERE prato LIKE '%{prato}%' '''
    cursor.execute(sql)
    for linha in cursor:
        print("Código:", linha[0])
        print("Prato:", linha[1])
        print("Valor:", linha[2], "\n")

## EXCLUIR #############
def excluir():
    cod = input("Código do prato: ")
    cursor.execute(f'''SELECT * FROM cardapio
                       WHERE codigo = {cod}; ''')
    if cursor.rowcount == 0 :
        print("Código não encontrado. \n")
    
    else : # rowcount > 0
        for linha in cursor:
            print(linha)
        
        resp = input("Excluir? (s/n) ")
        if resp == 's' :
            cursor.execute(f'''DELETE FROM cardapio
                               WHERE codigo = {cod}; ''')
            conexao.commit()
            print("Excluído com sucesso.\n\n")
                           

## ALTERAR ############################
def alterar():
    cod = input("Código do prato: ")
    cursor.execute(f'''SELECT * FROM cardapio
                       WHERE codigo = {cod}; ''')
    if cursor.rowcount == 0 :
        print("Código não encontrado. \n")
    else : # rowcount > 0
        for linha in cursor:
            print(linha)
        resp = input("Alterar? (s/n) ")
        if resp == 's' :
            coluna = input("Qual coluna? (prato/valor) ")
            info = input("Qual a nova informação? ")
            cursor.execute(f'''UPDATE cardapio 
                            SET {coluna} = '{info}'
                            WHERE codigo = {cod}; ''')
            conexao.commit()
            print("Alterado com sucesso.\n\n")
    
    
    
    
    

## MENU DO SISTEMA ####
while True:
    print("== SISTEMA DE RESTAURANTE ==")
    print("1-Cadastrar")
    print("2-Pesquisar")
    print("3-Alterar")
    print("4-Excluir")
    print("5-Sair")
    op = input("Qual opção? ")

    if   op == "1" : cadastrar()
    elif op == "2" : pesquisar()
    elif op == "3" : alterar()
    elif op == "4" : excluir()
    elif op == "5" : break
    
cursor.close()
conexao.close()