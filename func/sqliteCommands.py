import sqlite3

# função de criação de tabela 
def create_table(table_name, table_parameters):
    cnt = sqlite3.connect("db/dbHospital.db")  # abre database

    cnt.execute(f"DROP TABLE IF EXISTS {table_name};") # faz drop da tabela, se existir

    create_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({table_parameters});" # cria uma nova tabela 
    cnt.execute(create_sql)

    cnt.commit()
    cnt.close()

    return f"Tabela '{table_name}' criada com sucesso."