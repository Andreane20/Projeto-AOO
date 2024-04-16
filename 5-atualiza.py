import sqlite3
# 1- Conectando no BD
conexao = sqlite3.connect('novela.db')
cursor = conexao.cursor()


# 2-Atualização
id = 1
cursor.execute(
    """
    UPDATE NOVELA set nome = ?
    WHERE id = ?
    """,
    ("Avenida Brasil", id)
   
)
conexao.commit()