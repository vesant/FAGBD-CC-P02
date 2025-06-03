import sqlite3


# função de criação de tabela 
def create_table(table_name, table_parameters):
    return f"CREATE TABLE IF NOT EXISTS {table_name} ({table_parameters});"