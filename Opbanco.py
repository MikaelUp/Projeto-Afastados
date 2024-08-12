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
        # Se algum dos valores não for obrigatório e não estiver presente, coloque `None`
        i.extend([None] * (5 - len(i)))
        query = "INSERT INTO Afastados_ativos (Chapa, Nome, Data_Pericia, Último_dia_inss, Observação) VALUES (?,?,?,?,?)"
        cur.execute(query,i)

cadastrar_afastado_ativo(['2296', 'Mikael Sales Barros', '01/08/2024', '30/09/2024'])

#Ver afastados (Selecionar R)
def Ver_Afastados():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Afastados_ativos')
        linha = cur.fetchall()

        for i in linha: 
            lista.append(i)
    
    return lista

# print(Ver_Afastados())

# Atualizar os afastados (Uptade u)
def Atualizar_afastados(i):
    with con:
        cur = con.cursor()
        query = "UPTADE Afastados_ativos SET Nome=?, Data_Pericia=?, Último_dia_inss=?, Observação=? WHERE Chapa=?" 
        cur.execute(query, i)

# Deletar os afastados (D)
def Deletar_afastados(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Afastados_ativos WHERE Chapa=?"
        cur.execute('query, i')

