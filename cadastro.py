import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('cadastro.db')
cursor = conn.cursor()

# Criação da tabela de cadastro
cursor.execute('''CREATE TABLE IF NOT EXISTS cadastro
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL,
                cpf TEXT UNIQUE)''')

# Função de cadastro
def cadastrar(nome, email, senha, cpf=None):
    try:
        # Verifica se o e-mail já está cadastrado
        cursor.execute("SELECT * FROM cadastro WHERE email=?", (email,))
        if cursor.fetchone():
            print("E-mail já cadastrado!")
            return False

        # Verifica se o CPF já está cadastrado
        if cpf:
            cursor.execute("SELECT * FROM cadastro WHERE cpf=?", (cpf,))
            if cursor.fetchone():
                print("CPF já cadastrado!")
                return False

        # Insere os dados no banco de dados
        cursor.execute("INSERT INTO cadastro (nome, email, senha, cpf) VALUES (?, ?, ?, ?)", (nome, email, senha, cpf))
        conn.commit()
        print("Cadastro realizado com sucesso!")
        return True

    except Exception as e:
        print("Erro ao cadastrar:", e)
        return False

# Exemplo de uso da função de cadastro
cadastrar("Fulano de Tal", "fulano@gmail.com", "123456")
cadastrar("Beltrano de Tal", "beltrano@gmail.com", "654321", "12345678900")

# Fechamento da conexão com o banco de dados
conn.close()