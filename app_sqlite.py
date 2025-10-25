"""
Avaliação – Python + SQLite
Tema: CRUD em 'alunos'

O que o script deve fazer:
1) Criar 'escola.db'
2) Criar tabela 'alunos' -> Seguindo o diagrama
3) Inserir registros na tabela alunos
4) Listar todos
5) Buscar por id
6) Atualizar registros
7) Deletar registros

"""


import sqlite3
conn= sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS alunos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    email TEXT
    )''')

print('Tabela criada com sucesso!\n')

cursor.execute('INSERT INTO alunos(nome,idade,email) VALUES(?,?,?)',('Bia',19,'beatriz@gmail.com'))
cursor.execute('INSERT INTO alunos(nome,idade,email) VALUES(?,?,?)',('Cauã',19,'cauaaa@gmail.com'))
cursor.execute('INSERT INTO alunos(nome,idade,email) VALUES(?,?,?)',('Gustavo',18,'gusta@gmail.com'))
conn.commit()
print('Dados completos!\n')


print('Lista de alunos cadastrados:')
cursor.execute('SELECT * FROM alunos')
for linha in cursor.fetchall():
    print(linha)
print()

cursor.execute('UPDATE alunos SET email = ? WHERE nome = ?',('caua2002@gmail.com','Cauã'))
print('após atualização do email do Cauã')
cursor.execute('SELECT * FROM alunos')
for linha in cursor.fetchall():
    print(linha)
print()

cursor.execute('DELETE FROM alunos WHERE id= ?',(2,))
conn.commit()
print('Após deletar o id 1:')
cursor.execute('SELECT * FROM alunos')
for linha in cursor.fetchall():
    print(linha)
print()

conn.close()
