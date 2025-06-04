import sqlite3
from typing import List, Tuple, Optional

# ----------------- #
# funçao de conexao #
# ----------------- #

# vai abrir (ou criar) a db SQLite e retorna o objeto de conexao
def conectar(db_path: str = "../db/dbHospital.db") -> sqlite3.Connection:
    return sqlite3.connect(db_path)

# ---------------------- #
# funçoes para pacientes #
# ---------------------- #

# vai inserir um novo paciente e retorna o ID gerado automaticamente
def adicionar_paciente(nome, data_nascimento, genero, contato):
    conn = conectar()
    cursor = conn.cursor()
    sql = """
        INSERT INTO Paciente (nome, data_nascimento, genero, contato)
        VALUES (?, ?, ?, ?);
    """
    cursor.execute(sql, (nome, data_nascimento, genero, contato))
    conn.commit()
    novo_id = cursor.lastrowid
    conn.close()
    return novo_id

# vai tualizar os dados de um paciente.
# retorna quantas linhas foram efetivamente modificadas (0 / 1).
def editar_paciente(id_paciente, nome=None, data_nascimento=None, genero=None, contato=None):
    # - id_paciente;
    # - nome, data_nascimento, genero, contato;
    partes = []
    valores = []

    if nome is not None:
        partes.append("nome = ?")
        valores.append(nome)
    if data_nascimento is not None:
        partes.append("data_nascimento = ?")
        valores.append(data_nascimento)
    if genero is not None:
        partes.append("genero = ?")
        valores.append(genero)
    if contato is not None:
        partes.append("contato = ?")
        valores.append(contato)

    # se não houver nada para atualizar, sai logo!
    if not partes:
        return 0

    sql = f"UPDATE Paciente SET {', '.join(partes)} WHERE id_paciente = ?;"
    valores.append(id_paciente)

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(sql, tuple(valores))
    conn.commit()
    afetados = cursor.rowcount
    conn.close()
    return afetados

# vai excluir o paciente cujo id_paciente foi informado
# retorna quantas linhas foram removidas (0 / 1).
def excluir_paciente(id_paciente):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Paciente WHERE id_paciente = ?;", (id_paciente,))
    conn.commit()
    deletados = cursor.rowcount
    conn.close()
    return deletados

# vai retornar uma lista de pacientes, cujo nome contem a variavel informada
# cada item da lista é uma tupla: (id_paciente, nome, data_nascimento, genero, contato)
def buscar_paciente_por_nome(texto):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Paciente WHERE nome LIKE ?;", (f"%{texto}%",))
    resultados = cursor.fetchall()
    conn.close()
    return resultados

# vai retornar uma lista de pacientes, cujo contato contem a variavel informada
def buscar_paciente_por_contato(texto_contato):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Paciente WHERE contato LIKE ?;", (f"%{texto_contato}%",))
    resultados = cursor.fetchall()
    conn.close()
    return resultados

# -------------------- #
# funçoes para medicos #
# -------------------- #

# vai inserir um novo médico 
# retorna o ID gerado.
def adicionar_medico(nome, especialidade, contato):
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO Medico (nome, especialidade, contato) VALUES (?, ?, ?);"
    cursor.execute(sql, (nome, especialidade, contato))
    conn.commit()
    novo_id = cursor.lastrowid
    conn.close()
    return novo_id

# vai atualizar dados de um médico
# retorna quantas linhas foram afetadas.
def editar_medico(id_medico, nome=None, especialidade=None, contato=None):
    partes = []
    valores = []

    if nome is not None:
        partes.append("nome = ?")
        valores.append(nome)
    if especialidade is not None:
        partes.append("especialidade = ?")
        valores.append(especialidade)
    if contato is not None:
        partes.append("contato = ?")
        valores.append(contato)

    if not partes:
        return 0

    sql = f"UPDATE Medico SET {', '.join(partes)} WHERE id_medico = ?;"
    valores.append(id_medico)

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(sql, tuple(valores))
    conn.commit()
    afetados = cursor.rowcount
    conn.close()
    return afetados

# vai excluir o médico com o id_medico informado
# retorna quantas linhas foram deletadas
def excluir_medico(id_medico):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Medico WHERE id_medico = ?;", (id_medico,))
    conn.commit()
    deletados = cursor.rowcount
    conn.close()
    return deletados

# vai retornar uma lista de médicos cujo nome contém a variavel informada 
# cada item: (id_medico, nome, especialidade, contato).
def buscar_medico_por_nome(texto):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Medico WHERE nome LIKE ?;", (f"%{texto}%",))
    resultados = cursor.fetchall()
    conn.close()
    return resultados

# ------------------------ #
# funcoes para enfermeiros #
# ------------------------ #

# vai inserir um novo enfermeiro
# retorna o ID gerado
def adicionar_enfermeiro(nome, contato):
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO Enfermeiro (nome, contato) VALUES (?, ?);"
    cursor.execute(sql, (nome, contato))
    conn.commit()
    novo_id = cursor.lastrowid
    conn.close()
    return novo_id

# vai atualizar dados de um enfermeiro
# retorna quantas linhas foram afetadas
def editar_enfermeiro(id_enfermeiro, nome=None, contato=None):
    partes = []
    valores = []

    if nome is not None:
        partes.append("nome = ?")
        valores.append(nome)
    if contato is not None:
        partes.append("contato = ?")
        valores.append(contato)

    if not partes:
        return 0

    sql = f"UPDATE Enfermeiro SET {', '.join(partes)} WHERE id_enfermeiro = ?;"
    valores.append(id_enfermeiro)

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(sql, tuple(valores))
    conn.commit()
    afetados = cursor.rowcount
    conn.close()
    return afetados

# exclui o enfermeiro com o id_enfermeiro informado 
# retorna quantas linhas foram deletadas.
def excluir_enfermeiro(id_enfermeiro):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Enfermeiro WHERE id_enfermeiro = ?;", (id_enfermeiro,))
    conn.commit()
    deletados = cursor.rowcount
    conn.close()
    return deletados

# vai retornar uma lista de enfermeiros cujo nome contém a variavel informada 
# cada item: (id_enfermeiro, nome, contato)
def buscar_enfermeiro_por_nome(texto):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Enfermeiro WHERE nome LIKE ?;", (f"%{texto}%",))
    resultados = cursor.fetchall()
    conn.close()
    return resultados

# ---------------------- #
# funcoes para consultas #
# ---------------------- #

# vai inserir uma nova consulta no agendamento e retorna o ID gerado.
# - data_consulta: 'YYYY-MM-DD HH:MM'
# - status: ex.: 'agendada'; 'cancelada'; 'realizada'
def agendar_consulta(id_paciente, id_medico, data_consulta, status):
    conn = conectar()
    cursor = conn.cursor()
    sql = """
        INSERT INTO Consulta (id_paciente, id_medico, data_consulta, status)
        VALUES (?, ?, ?, ?);
    """
    cursor.execute(sql, (id_paciente, id_medico, data_consulta, status))
    conn.commit()
    novo_id = cursor.lastrowid
    conn.close()
    return novo_id

# vai atualizar o status de uma consulta para 'cancelada'
# retorna quantas linhas foram afetadas
def cancelar_consulta(id_consulta):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE Consulta SET status = 'cancelada' WHERE id_consulta = ?;", (id_consulta,))
    conn.commit()
    afetados = cursor.rowcount
    conn.close()
    return afetados

# retorna todas as consultas marcadas para um dia específico (YYYY-MM-DD)
# cada item: (id_consulta, id_paciente, id_medico, data_consulta, status)
def buscar_consultas_por_data(data_consulta):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Consulta WHERE DATE(data_consulta) = DATE(?);", (data_consulta,))
    resultados = cursor.fetchall()
    conn.close()
    return resultados

# retorna todas as consultas entre data_inicio e data_fim (inclusive)
# datas no formato 'YYYY-MM-DD'.
def buscar_consultas_intervalo(data_inicio, data_fim):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM Consulta WHERE DATE(data_consulta) BETWEEN DATE(?) AND DATE(?);",
        (data_inicio, data_fim)
    )
    resultados = cursor.fetchall()
    conn.close()
    return resultados

# vai retornar todas as consultas para um determinado paciente
# cada item: (id_consulta, id_paciente, id_medico, data_consulta, status)
def buscar_consultas_por_paciente(id_paciente):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Consulta WHERE id_paciente = ?;", (id_paciente,))
    resultados = cursor.fetchall()
    conn.close()
    return resultados

# ------------------------ #
# funcoes para tratamentos #
# ------------------------ #

# vai inserir um registro de tratamento para um paciente e retorna o ID gerado.
# - data_tratamento: 'YYYY-MM-DD'
# - descricao: texto (até 1024 carac.)
def adicionar_tratamento(id_paciente, descricao, data_tratamento):
    conn = conectar()
    cursor = conn.cursor()
    sql = """
        INSERT INTO Tratamento (id_paciente, descricao, data_tratamento)
        VALUES (?, ?, ?);
    """
    cursor.execute(sql, (id_paciente, descricao, data_tratamento))
    conn.commit()
    novo_id = cursor.lastrowid
    conn.close()
    return novo_id

# vai retornar todos os tratamentos de um paciente, ordenados pela data mais recente
# cada item: (id_tratamento, id_paciente, descricao, data_tratamento)
def buscar_tratamentos_paciente(id_paciente):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM Tratamento WHERE id_paciente = ? ORDER BY data_tratamento DESC;",
        (id_paciente,)
    )
    resultados = cursor.fetchall()
    conn.close()
    return resultados

# ------------------------ #
# funcoes para prescricoes #
# ------------------------ #

# vai inserir uma nova prescrição e retorna o ID gerado
# - data_prescricao: 'YYYY-MM-DD'
# - nome_medicamento: texto com nome do medicamento
def adicionar_prescricao(id_paciente, id_medico, nome_medicamento, data_prescricao):
    conn = conectar()
    cursor = conn.cursor()
    sql = """
        INSERT INTO Prescricao (id_paciente, id_medico, nome_medicamento, data_prescricao)
        VALUES (?, ?, ?, ?);
    """
    cursor.execute(sql, (id_paciente, id_medico, nome_medicamento, data_prescricao))
    conn.commit()
    novo_id = cursor.lastrowid
    conn.close()
    return novo_id

# vai retornar prescrições feitas por um médico entre data_inicio e data_fim
# cada item: (id_prescricao, id_paciente, id_medico, nome_medicamento, data_prescricao)
def buscar_prescricoes_por_medico_periodo(id_medico, data_inicio, data_fim):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM Prescricao WHERE id_medico = ? AND DATE(data_prescricao) BETWEEN DATE(?) AND DATE(?) ORDER BY data_prescricao DESC;",
        (id_medico, data_inicio, data_fim)
    )
    resultados = cursor.fetchall()
    conn.close()
    return resultados

# vai retornar prescrições de um médico para pacientes numa faixa etária (calcula idade por data_nascimento) num periodo 
# cada item: (id_prescricao, id_paciente, id_medico, nome_medicamento, data_prescricao, idade_atual).
def buscar_prescricoes_medico_idade(id_medico, idade_min, idade_max, data_inicio, data_fim):
    conn = conectar()
    cursor = conn.cursor()
    sql = """
        SELECT
            p.id_prescricao,
            p.id_paciente,
            p.id_medico,
            p.nome_medicamento,
            p.data_prescricao,
            (CAST(strftime('%Y', 'now') AS INTEGER) - CAST(strftime('%Y', pa.data_nascimento) AS INTEGER))
              - (strftime('%m-%d', 'now') < strftime('%m-%d', pa.data_nascimento))
              AS idade_atual
        FROM Prescricao p
        JOIN Paciente pa ON p.id_paciente = pa.id_paciente
        WHERE p.id_medico = ?
          AND DATE(p.data_prescricao) BETWEEN DATE(?) AND DATE(?)
          AND ((CAST(strftime('%Y', 'now') AS INTEGER) - CAST(strftime('%Y', pa.data_nascimento) AS INTEGER))
               - (strftime('%m-%d', 'now') < strftime('%m-%d', pa.data_nascimento))) BETWEEN ? AND ?
        ORDER BY p.data_prescricao DESC;
    """
    cursor.execute(sql, (id_medico, data_inicio, data_fim, idade_min, idade_max))
    resultados = cursor.fetchall()
    conn.close()
    return resultados

# ------------------------- #
# funcoes para user e login #
# ------------------------- #

# vai verificar se existe um user com login e senha 
# retorna (id_user, login, tipo_user) se encontrar, None caso contrário
def autenticar_user(login, senha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id_user, login, tipo_user FROM Users WHERE login = ? AND senha = ?;", (login, senha))
    user = cursor.fetchone()
    conn.close()
    return user

# vai inserir um novo user e retorna o ID gerado
# - login: texto único
# - senha: texto (em texto simples ou hash, conforme a aplicação principal)
# - tipo_user: por ex. 'admin', 'paciente', 'medico', 'enfermeiro'
def adicionar_user(login, senha, tipo_user):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Users (login, senha, tipo_user) VALUES (?, ?, ?);", (login, senha, tipo_user))
    conn.commit()
    novo_id = cursor.lastrowid
    conn.close()
    return novo_id

# ----------------- #
# funcoes para logs #
# ----------------- #

# vai inserir um registro de log de acesso e retornar o ID do log
# - id_user: ID de quem executou a ação
# - acao_executada: texto descrevendo a ação (ex: 'login', 'add_paciente', ...)
# - status: texto, ex: 'sucesso' ou 'falha' 
# a coluna 'data' será preenchida automaticamente com a data/hora atual!
def gravar_log(id_user, acao_executada, status):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Log_Acesso (id_user, acao_executada, status) VALUES (?, ?, ?);",
        (id_user, acao_executada, status)
    )
    conn.commit()
    novo_id = cursor.lastrowid
    conn.close()
    return novo_id

# vai retornar todos os logs de um user, em ordem decrescente de data
# cada item: (id_log, id_user, acao_executada, data, status).
def buscar_logs_por_user(id_user):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Log_Acesso WHERE id_user = ? ORDER BY data DESC;", (id_user,))
    resultados = cursor.fetchall()
    conn.close()
    return resultados

# vai retornar todos os logs cujo campo 'data' esteja entre data_inicio e data_fim
# formato das datas: 'YYYY-MM-DD' 
# cada item: (id_log, id_user, acao_executada, data, status).
def buscar_logs_por_periodo(data_inicio, data_fim):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM Log_Acesso WHERE DATE(data) BETWEEN DATE(?) AND DATE(?) ORDER BY data DESC;",
        (data_inicio, data_fim)
    )
    resultados = cursor.fetchall()
    conn.close()
    return resultados

# ------------------ #
# funcoes auxiliares #
# ------------------ #

# Retorna todas as linhas de qualquer tabela informada 
# cada linha é uma tupla com todas as colunas da tabela.
def buscar_todos_conteudo_tabela(tabela):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {tabela};")
    linhas = cursor.fetchall()
    conn.close()
    return linhas

# vai contar quantos registros existem numa tabela
# - tabela: nome da tabela (texto)
# - clausula_where (opcional): string como "genero = ?" para filtrar
# - params (opcional): tupla com valores para a cláusula WHERE 
# retorna o total de linhas
def contar_registros(tabela, clausula_where=None, params=None):
    conn = conectar()
    cursor = conn.cursor()
    if clausula_where:
        cursor.execute(f"SELECT COUNT(*) FROM {tabela} WHERE {clausula_where};", params)
    else:
        cursor.execute(f"SELECT COUNT(*) FROM {tabela};")
    total = cursor.fetchone()[0]
    conn.close()
    return total

# retorna uma lista com os nomes das colunas de uma tabela.
def obter_colunas(tabela):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({tabela});")
    info = cursor.fetchall()
    conn.close()
    # Cada linha: (cid, name, type, notnull, dflt_value, pk)
    colunas = [item[1] for item in info]
    return colunas

# ----- #
# debug #
# ----- #

# inserção de dados, para debug
if __name__ == "__main__":
    # criação de user admin
    admin_id = adicionar_user("adm1", "proj2025@", "admin")
    print("Admin criado com ID:", admin_id)

    # adiciona um paciente
    id_paciente = adicionar_paciente("Ana Silva", "1990-05-12", "F", "+351912345678")
    print("Paciente criado com ID:", id_paciente)

    # adiciona um medico
    id_medico = adicionar_medico("Dr. João", "Cardiologia", "+351912300000")
    print("Médico criado com ID:", id_medico)

    # agenda uma consulta
    id_consulta = agendar_consulta(id_paciente, id_medico, "2025-06-05 14:30", "agendada")
    print("Consulta agendada com ID:", id_consulta)

    # adiciona um tratamento
    id_trat = adicionar_tratamento(id_paciente, "Tratamento de rotina", "2025-06-06")
    print("Tratamento inserido com ID:", id_trat)

    # adiciona uma prescrição
    id_presc = adicionar_prescricao(id_paciente, id_medico, "Paracetamol", "2025-06-05")
    print("Prescrição inserida com ID:", id_presc)

    # grava acesso em log
    log_id = gravar_log(admin_id, "login", "sucesso")
    print("Log de acesso criado com ID:", log_id)

    # mostra pacientes com nome "Ana"
    pacientes = buscar_paciente_por_nome("Ana")
    print("Pacientes encontrados (por nome 'Ana'):", pacientes)

    # conta o total de pacientes
    total_pacs = contar_registros("Paciente")
    print("Total de pacientes cadastrados:", total_pacs)