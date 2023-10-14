import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('cadastro.db')
cursor = conn.cursor()

# Função de login
def login(email, senha):
    try:
        # Verifica se o e-mail e a senha correspondem aos dados no banco de dados
        cursor.execute("SELECT * FROM cadastro WHERE email=? AND senha=?", (email, senha))
        if cursor.fetchone():
            print("Login realizado com sucesso!")
            return True
        else:
            print("E-mail ou senha incorretos!")
            return False

    except Exception as e:
        print("Erro ao realizar login:", e)
        return False

# Exemplo de uso da função de login
login("fulano@gmail.com", "123456")
login("fulano@gmail.com", "senhaerrada")

# Fechamento da conexão com o banco de dados
conn.close()