import mariadb    # carregar o driver

conexao = mariadb.connect(host="localhost",  # dados conexão
                          user="root",
                          password="",
                          database="escola")

print("Conectado com sucesso.")

cursor = conexao.cursor()  # cursor / obj que executa sql

#### CADASTRO ##############################

nome  = input("Nome do aluno: ")
curso = input("Qual o curso? ")
serie = input("Qual a série? ")

sql = f'''INSERT INTO alunos
          VALUES(null, '{nome}', '{curso}',
          {serie}); '''

cursor.execute(sql)  # excuta o comando no bd
conexao.commit()     # confirma a gravação

print("Gravado com sucesso.")
