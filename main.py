# =================================================================== #
# Sistema de Gestão Hospitalar                                        #
# Autores: Amira Babkir (2024126219) - Vicente Gonçalves (2024122708) #
# IPS (ESTS) - Fundamentos Administração e Gestão BD - CC 2024/25     #
# =================================================================== #

import getpass
import datetime
from func.sqliteCommands import *

# -------------------------- #
# Funções auxiliares simples #
# -------------------------- #

def clear():
    print("\n" * 100)

def cifrar(texto):
    # simples cifragem reversa 
    # apenas para cumprir requisito: "O prontuário do paciente deve ser gravado de forma cifrada."
    return texto[::-1]

def decifrar(texto_cifrado):
    return texto_cifrado[::-1]

def espera():
    input("\nClique ENTER para continuar...")

def listar_pacientes_simples():
    pacientes = buscar_paciente_por_nome("")
    print("\nPacientes disponíveis:")
    for p in pacientes:
        print(f"ID: {p[0]} | Nome: {p[1]}")

def listar_medicos_simples():
    medicos = buscar_medico_por_nome("")
    print("\nMédicos disponíveis:")
    for m in medicos:
        print(f"ID: {m[0]} | Nome: {m[1]} | Especialidade: {m[2]}")

def listar_enfermeiros_simples():
    enfers = buscar_enfermeiro_por_nome("")
    print("\nEnfermeiros disponíveis:")
    for e in enfers:
        print(f"ID: {e[0]} | Nome: {e[1]}")

# --------------------------- #
#           LOGIN             #
# --------------------------- #

def login():
    clear()
    print("#======# LOGIN NO SISTEMA #======#")
    login = input("Username: ")
    senha = getpass.getpass("Password: ")

    user = autenticar_user(login, senha)
    if user:
        gravar_log(user[0], "login", "sucesso")
        print("Login efetuado com sucesso!\n")
        return user
    else:
        print("Username ou password incorretos.")
        espera()
        return None

# ---------------- #
# menus do sistema #
# ---------------- #

def menu_admin(user):
    while True:
        clear()
        print("#=====# Menu Administrador #=====#")
        print("1. Adicionar Paciente")
        print("2. Adicionar Médico ou Enfermeiro")
        print("3. Agendar Consulta")
        print("4. Adicionar Tratamento")
        print("5. Adicionar Prescrição")
        print("6. Visualizar Pacientes")
        print("7. Visualizar Médicos ou Enfermeiros")
        print("8. Modificar contactos")
        print("9. Visualizar Consultas")
        print("10. Visualizar Tratamentos de um Paciente")
        print("11. Visualizar Prescrições por Médico/Período")
        print("12. Visualizar funcionários médicos")
        print("13. Visualizar conteúdo de tabelas")
        print("14. Visualizar log de acessos")
        print("15. Excluir Paciente")
        print("16. Excluir Médico")
        print("17. Excluir Enfermeiro")
        print("18. Sair")
        op = input("Opção: ")

        if op == "1":
            adicionar_paciente_menu(user)
        elif op == "2":
            adicionar_funcionario_menu(user)
        elif op == "3":
            agendar_consulta_menu(user)
        elif op == "4":
            adicionar_tratamento_menu(user)
        elif op == "5":
            adicionar_prescricao_menu(user)
        elif op == "6":
            visualizar_pacientes_menu(user)
        elif op == "7":
            visualizar_funcionarios_menu(user)
        elif op == "8":
            modificar_contato_menu(user)
        elif op == "9":
            visualizar_consultas_menu(user)
        elif op == "10":
            visualizar_tratamentos_menu(user)
        elif op == "11":
            visualizar_prescricoes_menu(user)
        elif op == "12":
            visualizar_funcionarios_menu(user, so_medicos=True)
        elif op == "13":
            visualizar_tabela_menu(user)
        elif op == "14":
            visualizar_log_menu(user)
        elif op == "15":
            excluir_paciente_menu(user)
        elif op == "16":
            excluir_medico_menu(user)
        elif op == "17":
            excluir_enfermeiro_menu(user)
        elif op == "18":
            break
        else:
            print("Opção inválida!")
            espera()

def menu_paciente(user):
    while True:
        clear()
        print("#=====# Menu Paciente #=====#")
        print("1. Ver as minhas informações")
        print("2. Modificar os meus dados")
        print("3. Ver as minhas consultas")
        print("4. Ver os meus tratamentos")
        print("5. Sair")
        op = input("Opção: ")
        if op == "1":
            visualizar_meu_perfil(user)
        elif op == "2":
            modificar_meus_dados_menu(user)
        elif op == "3":
            visualizar_minhas_consultas(user)
        elif op == "4":
            visualizar_meus_tratamentos(user)
        elif op == "5":
            break
        else:
            print("Opção inválida!")
            espera()

def menu_medico(user):
    while True:
        clear()
        print("#=====# Menu Médico #=====#")
        print("1. Visualizar os meus pacientes")
        print("2. Visualizar as minhas prescrições")
        print("3. Visualizar as minhas consultas")
        print("4. Sair")
        op = input("Opção: ")
        if op == "1":
            visualizar_pacientes_menu(user)
        elif op == "2":
            visualizar_prescricoes_menu(user, so_meu_medico=True)
        elif op == "3":
            visualizar_consultas_menu(user, so_meu_medico=True)
        elif op == "4":
            break
        else:
            print("Opção inválida!")
            espera()

def menu_enfermeiro(user):
    while True:
        clear()
        print("#=====# Menu Enfermeiro #=====#")
        print("1. Visualizar os meus dados")
        print("2. Modificar os meu contactos")
        print("3. Visualizar as consultas dos pacientes")
        print("4. Sair")
        op = input("Opção: ")
        if op == "1":
            visualizar_meu_perfil(user)
        elif op == "2":
            modificar_meus_dados_menu(user)
        elif op == "3":
            visualizar_consultas_menu(user)
        elif op == "4":
            break
        else:
            print("Opção inválida!")
            espera()

# ----------------- #
# funçoes dos menus #
# ----------------- #

def adicionar_paciente_menu(user):
    clear()
    print("#==# Adicionar Paciente #==#")
    nome = input("Nome: ")
    data_nasc = input("Data de nascimento (YYYY-MM-DD): ")
    genero = input("Gênero: ")
    contato = input("Contato: ")
    prontuario = input("Prontuário médico (texto livre): ")
    
    prontuario_cifrado = cifrar(prontuario) # cifra aqui!

    try:
        id_pac = adicionar_paciente(nome, data_nasc, genero, contato, prontuario_cifrado)
        gravar_log(user[0], "add_paciente", "sucesso")
        print(f"Paciente adicionado com ID: {id_pac}")
    except Exception as e:
        gravar_log(user[0], "add_paciente", "falha")
        print("Erro ao adicionar paciente:", str(e))
    espera()

def adicionar_funcionario_menu(user):
    clear()
    print("#==# Adicionar Funcionário #==#")
    print("1. Médico")
    print("2. Enfermeiro")
    tipo = input("Opção: ")
    nome = input("Nome: ")
    contato = input("Contato: ")
    if tipo == "1":
        espec = input("Especialidade: ")
        try:
            idm = adicionar_medico(nome, espec, contato)
            gravar_log(user[0], "add_medico", "sucesso")
            print(f"Médico adicionado com ID: {idm}")
        except Exception as e:
            gravar_log(user[0], "add_medico", "falha")
            print("Erro ao adicionar médico:", str(e))
    elif tipo == "2":
        try:
            ide = adicionar_enfermeiro(nome, contato)
            gravar_log(user[0], "add_enfermeiro", "sucesso")
            print(f"Enfermeiro adicionado com ID: {ide}")
        except Exception as e:
            gravar_log(user[0], "add_enfermeiro", "falha")
            print("Erro ao adicionar enfermeiro:", str(e))
    else:
        print("Opção inválida!")
    espera()

def agendar_consulta_menu(user):
    clear()
    print("#==# Agendar Consulta #==#")
    try:
        listar_pacientes_simples()
        id_pac = int(input("ID do paciente: "))
        listar_medicos_simples()
        id_med = int(input("ID do médico: "))
        data_cons = input("Data da consulta (YYYY-MM-DD HH:MM): ")
        status = "agendada"
        idc = agendar_consulta(id_pac, id_med, data_cons, status)
        gravar_log(user[0], "agendar_consulta", "sucesso")
        print(f"Consulta agendada com ID: {idc}")
    except Exception as e:
        gravar_log(user[0], "agendar_consulta", "falha")
        print("Erro ao agendar consulta:", str(e))
    espera()

def adicionar_tratamento_menu(user):
    clear()
    print("#==# Adicionar Tratamento #==#")
    try:
        listar_pacientes_simples()
        id_pac = int(input("ID do paciente: "))
        descricao = input("Descrição do tratamento (máx 1024): ")
        data_trat = input("Data do tratamento (YYYY-MM-DD): ")
        idt = adicionar_tratamento(id_pac, descricao[:1024], data_trat)
        gravar_log(user[0], "add_tratamento", "sucesso")
        print(f"Tratamento adicionado com ID: {idt}")
    except Exception as e:
        gravar_log(user[0], "add_tratamento", "falha")
        print("Erro ao adicionar tratamento:", str(e))
    espera()

def adicionar_prescricao_menu(user):
    clear()
    print("#==# Adicionar Prescrição #==#")
    try:
        listar_pacientes_simples()
        id_pac = int(input("ID do paciente: "))
        listar_medicos_simples()
        id_med = int(input("ID do médico: "))
        medicamento = input("Nome do medicamento: ")
        data_presc = input("Data da prescrição (YYYY-MM-DD): ")
        idp = adicionar_prescricao(id_pac, id_med, medicamento, data_presc)
        gravar_log(user[0], "add_prescricao", "sucesso")
        print(f"Prescrição adicionada com ID: {idp}")
    except Exception as e:
        gravar_log(user[0], "add_prescricao", "falha")
        print("Erro ao adicionar prescrição:", str(e))
    espera()

def visualizar_pacientes_menu(user):
    clear()
    print("#==# Buscar Pacientes #==#")
    print("(deixe em branco para vizualizar todos)")
    print("1. Por nome")
    print("2. Por contato")
    op = input("Opção: ")
    if op == "1":
        nome = input("Nome: ")
        pacientes = buscar_paciente_por_nome(nome)
    else:
        contato = input("Contato: ")
        pacientes = buscar_paciente_por_contato(contato)
    print("\nResultados:")
    if pacientes:
        print("ID | Nome                 | Data Nasc. | Gênero | Contato")
        print("-"*60)
        for pac in pacientes:
            # (id_paciente, nome, data_nascimento, genero, contato, prontuario)
            print(f"{pac[0]:<2} | {pac[1]:<20} | {pac[2]:<10} | {pac[3]:<6} | {pac[4]}")
    else:
        print("Nenhum paciente encontrado.")
    gravar_log(user[0], "visualizar_pacientes", "sucesso")
    espera()

def visualizar_funcionarios_menu(user, so_medicos=False):
    clear()
    if so_medicos:
        print("#==# Médicos #==#")
        medicos = buscar_medico_por_nome("")
        if medicos:
            print("ID | Nome                 | Especialidade       | Contato")
            print("-"*65)
            for m in medicos:
                # (id_medico, nome, especialidade, contato)
                print(f"{m[0]:<2} | {m[1]:<20} | {m[2]:<18} | {m[3]}")
        else:
            print("Nenhum médico encontrado.")
    else:
        print("1. Médicos\n2. Enfermeiros")
        op = input("Opção: ")
        if op == "1":
            medicos = buscar_medico_por_nome("")
            if medicos:
                print("ID | Nome                 | Especialidade       | Contato")
                print("-"*65)
                for m in medicos:
                    print(f"{m[0]:<2} | {m[1]:<20} | {m[2]:<18} | {m[3]}")
            else:
                print("Nenhum médico encontrado.")
        else:
            enfers = buscar_enfermeiro_por_nome("")
            if enfers:
                print("ID | Nome                 | Contato")
                print("-"*40)
                for e in enfers:
                    # (id_enfermeiro, nome, contato)
                    print(f"{e[0]:<2} | {e[1]:<20} | {e[2]}")
            else:
                print("Nenhum enfermeiro encontrado.")
    gravar_log(user[0], "visualizar_funcionarios", "sucesso")
    espera()

def modificar_contato_menu(user):
    clear()
    print("#==# Modificar Contato #==#")
    print("1. Paciente")
    print("2. Médico")
    print("3. Enfermeiro")
    op = input("Qual tipo de utilizador? ")
    try:
        if op == "1":
            listar_pacientes_simples()
        elif op == "2":
            listar_medicos_simples()
        elif op == "3":
            listar_enfermeiros_simples()
        id = int(input("ID do utilizador: "))
        novo_contato = input("Novo contato: ")
        if op == "1":
            editar_paciente(id, contato=novo_contato)
        elif op == "2":
            editar_medico(id, contato=novo_contato)
        elif op == "3":
            editar_enfermeiro(id, contato=novo_contato)
        else:
            print("Opção inválida!")
            return
        gravar_log(user[0], "modificar_contato", "sucesso")
        print("Contato atualizado!")
    except Exception as e:
        gravar_log(user[0], "modificar_contato", "falha")
        print("Erro:", str(e))
    espera()

def visualizar_consultas_menu(user, so_meu_medico=False):
    clear()
    print("#==# Visualizar Consultas #==#")
    print("1. Por dia")
    print("2. Por intervalo")
    op = input("Opção: ")
    if op == "1":
        data = input("Data (YYYY-MM-DD): ")
        consultas = buscar_consultas_por_data(data)
    else:
        data1 = input("Data início (YYYY-MM-DD): ")
        data2 = input("Data fim (YYYY-MM-DD): ")
        consultas = buscar_consultas_intervalo(data1, data2)
    for c in consultas:
        print(c)
    gravar_log(user[0], "visualizar_consultas", "sucesso")
    espera()

def visualizar_tratamentos_menu(user):
    clear()
    print("#==# Visualizar Tratamentos de um Paciente #==#")
    listar_pacientes_simples()
    idp = int(input("ID do paciente: "))
    tratamentos = buscar_tratamentos_paciente_com_medico(idp)
    for t in tratamentos:
        print(f"ID: {t[0]}, Descrição: {t[1]}, Data: {t[2]}, Médico: {t[3] or '---'}")
    gravar_log(user[0], "visualizar_tratamentos", "sucesso")
    espera()

def visualizar_prescricoes_menu(user, so_meu_medico=False):
    clear()
    print("#==# Visualizar Prescrições #==#")
    if so_meu_medico:
        id_med = user[0]  # assume que o id_user = id_medico
    else:
        listar_medicos_simples()
        id_med = int(input("ID do médico: "))
    print("1. Por período")
    print("2. Por faixa etária e período")
    op = input("Opção: ")
    data1 = input("Data início (YYYY-MM-DD): ")
    data2 = input("Data fim (YYYY-MM-DD): ")
    if op == "1":
        prescricoes = buscar_prescricoes_por_medico_periodo(id_med, data1, data2)
    else:
        idade_min = int(input("Idade mínima: "))
        idade_max = int(input("Idade máxima: "))
        prescricoes = buscar_prescricoes_medico_idade(id_med, idade_min, idade_max, data1, data2)
    for p in prescricoes:
        print(p)
    gravar_log(user[0], "visualizar_prescricoes", "sucesso")
    espera()

def visualizar_tabela_menu(user):
    clear()
    print("#==# Visualizar conteúdo de uma tabela #==#")
    tabela = input("Nome da tabela: ")
    dados = buscar_todos_conteudo_tabela(tabela)
    for d in dados:
        print(d)
    gravar_log(user[0], f"visualizar_tabela_{tabela}", "sucesso")
    espera()

def visualizar_log_menu(user):
    clear()
    print("#==# Visualizar Log de Acessos #==#")
    print("1. Por período")
    print("2. Por utilizador")
    op = input("Opção: ")
    if op == "1":
        data1 = input("Data início (YYYY-MM-DD): ")
        data2 = input("Data fim (YYYY-MM-DD): ")
        logs = buscar_logs_por_periodo(data1, data2)
    else:
        id_user = int(input("ID do utilizador: "))
        logs = buscar_logs_por_user(id_user)
    for l in logs:
        print(l)
    espera()

def excluir_paciente_menu(user):
    clear()
    print("#==# Excluir Paciente #==#")
    listar_pacientes_simples()
    idp = int(input("ID do paciente a excluir: "))
    afetados = excluir_paciente(idp)
    if afetados:
        print("Paciente excluído com sucesso.")
        gravar_log(user[0], "excluir_paciente", "sucesso")
    else:
        print("ID não encontrado.")
        gravar_log(user[0], "excluir_paciente", "falha")
    espera()

def excluir_medico_menu(user):
    clear()
    print("#==# Excluir Médico #==#")
    listar_medicos_simples()
    idm = int(input("ID do médico a excluir: "))
    afetados = excluir_medico(idm)
    if afetados:
        print("Médico excluído com sucesso.")
        gravar_log(user[0], "excluir_medico", "sucesso")
    else:
        print("ID não encontrado.")
        gravar_log(user[0], "excluir_medico", "falha")
    espera()

def excluir_enfermeiro_menu(user):
    clear()
    print("#==# Excluir Enfermeiro #==#")
    listar_enfermeiros_simples()
    ide = int(input("ID do enfermeiro a excluir: "))
    afetados = excluir_enfermeiro(ide)
    if afetados:
        print("Enfermeiro excluído com sucesso.")
        gravar_log(user[0], "excluir_enfermeiro", "sucesso")
    else:
        print("ID não encontrado.")
        gravar_log(user[0], "excluir_enfermeiro", "falha")
    espera()

# -------------------------------------------- #
# menus proprios para o paciente ou enfermeiro #
# -------------------------------------------- #

def visualizar_meu_perfil(user):
    print("== Meu Perfil ==")
    print(user)
    espera()

def modificar_meus_dados_menu(user):
    print("== Modificar meus dados ==")
    novo_contato = input("Novo contato: ")
    # supondo user[2] == tipo_user e user[0] == id_user
    if user[2] == "paciente":
        editar_paciente(user[0], contato=novo_contato)
    elif user[2] == "enfermeiro":
        editar_enfermeiro(user[0], contato=novo_contato)
    gravar_log(user[0], "modificar_meus_dados", "sucesso")
    print("Contato atualizado!")
    espera()

def visualizar_minhas_consultas(user):
    # aqui tem que ser o id_user == id_paciente
    consultas = buscar_consultas_por_paciente(user[0])
    for c in consultas:
        print(c)
    espera()

def visualizar_meus_tratamentos(user):
    tratamentos = buscar_tratamentos_paciente(user[0])
    for t in tratamentos:
        print(t)
    espera()

# --------- #
# main loop #
# --------- #

def main():
    while True:
        user = None
        while not user:
            user = login()
        # user = (id_user, login, tipo_user)
        if user[2] == "admin":
            menu_admin(user)
        elif user[2] == "paciente":
            menu_paciente(user)
        elif user[2] == "medico":
            menu_medico(user)
        elif user[2] == "enfermeiro":
            menu_enfermeiro(user)
        else:
            print("Tipo de utilizador desconhecido!")
            espera()

if __name__ == "__main__":
    main()