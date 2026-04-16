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

## MENU DO SISTEMA ####
while True:
    print("== SISTEMA DE RESTAURANTE ==")
    print("1-Cadastrar")
    print("2-Pesquisar")
    print("3-Alterar")
    print("4-Excluir")
    print("5-Sair")
    op = input("Qual opção? ")

    if op == "1" : cadastrar()
    elif op == "2" : pesquisar()
    elif op == "5" : break
    