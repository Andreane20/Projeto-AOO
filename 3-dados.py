import sqlite3


# 1- Conectando no BD
conexao = sqlite3.connect('novela.db')


cursor = conexao.cursor()


# 2-Inserindo Dados
cursor.execute(
    """
        INSERT INTO NOVELA(nome, ano_lancamento, audiencia_media )
        VALUES ('Mar de Amor', 2009, 7.0 )
    """

)


conexao.commit()
conexao.close()
