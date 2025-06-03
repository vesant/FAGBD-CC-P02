# import de bibliotecas 
import sqlite3

#import de metodos externos
from func.sqliteCommands import create_table

#main
def main():
    result = create_table("users", "id INTEGER PRIMARY KEY")
    print(result)

# main classes
if __name__ == "__main__":
    main()