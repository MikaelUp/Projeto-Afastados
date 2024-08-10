import sqlite3
# Criando conexão
try:
    con = sqlite3.connect('cadastro_afastados.db')
    print('Conexão com banco de dados bem sucedida')
except sqlite3.Error as e: 
    print('Erro ao conectar com o banco de dados:', e)

# Criando tabela de Afastados ativos
try: 
    with con:
        cur = con.cursor()
        cur.execute(""" 
            CREATE TABLE IF NOT EXISTS Afastados_ativos( 
                Chapa INTEGER PRIMARY KEY NOT NULL, 
                Nome TEXT NOT NULL,
                Data_Pericia DATE, 
                Último_dia_inss,
                Observação TEXT
            )""") 
    print('Tabela Afastados_ativos criada com sucesso')
except sqlite3.Error as e: 
    print('Erro ao criar a tabela Afastados_ativos:', e)

# Criando tabela de Afastados desativados
try: 
    with con:
        cur = con.cursor()
        cur.execute(""" 
            CREATE TABLE IF NOT EXISTS Afastados_desativados( 
                Chapa INTEGER PRIMARY KEY NOT NULL, 
                Nome TEXT NOT NULL,
                Último_dia_inss DATE NOT NULL,
                Mês_de_retorno DATE NOT NULL
            )""") 
    print('Tabela Afastados_desativados criada com sucesso')

except sqlite3.Error as e: 
    print('Erro ao criar a tabela Afastados_ativos:', e)

