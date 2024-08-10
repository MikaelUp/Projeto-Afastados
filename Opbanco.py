import sqlite3

# Criando conexão
try:
    con = sqlite3.connect('cadastro_afastados.db')
    print('Conexão com banco de dados bem sucedida')
except sqlite3.Error as e: 
    print('Erro ao conectar com o banco de dados:', e)

# Tabela de afastados ativos -----------------------------------------------

# Cadastrar  Afastado ativo
def cadastrar_afastado_ativo(i):
    with con: 
        cur = con.cursor()
        i.extend([None] * (5 - len(i)))
        query = "INSERT INTO Afastados_ativos (Chapa, Nome, Data_Pericia, Último_dia_inss, Observação) VALUES (?,?,?,?,?)"
        cur.execute(query,i)
# Se algum dos valores não for obrigatório e não estiver presente, coloque `None`

cadastrar_afastado_ativo(['2296', 'Mikael Sales Barros', '01/08/2024', '30/09/2024'])

#Ver afastados