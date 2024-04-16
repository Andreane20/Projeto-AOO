import sqlite3
# 1- Conectando no BD
conexao = sqlite3.connect('novela.db')
cursor = conexao.cursor()


# 2-Exclusão
id = (1,4)
cursor.execute(
    """
    DELETE FROM Novela
    WHERE id in (?,?)
    """,
    id
)
conexao.commit()
