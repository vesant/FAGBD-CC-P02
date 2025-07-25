# =================================================================== #
# Sistema de Gestão Hospitalar                                        #
# Autores: Amira Babkir (2024126219) - Vicente Gonçalves (2024122708) #
# IPS (ESTS) - Fundamentos Administração e Gestão BD - CC 2024/25     #
# Reformulado com [rich] para UI na consola                           #
# =================================================================== #

from rich import print
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.traceback import install
import getpass
from datetime import datetime
from func.sqliteCommands import *

install()
console = Console()

# -------------------------- #
# Funções auxiliares simples #
# -------------------------- #

def clear():
    console.print("\n" * 100)

def cifrar(texto):
    # simples cifragem reversa 
    return texto[::-1]

def decifrar(texto_cifrado):
    return texto_cifrado[::-1]

def op_in():
    console.print("[yellow]Opção inválida![/yellow]")
    
def espera():
    input("\nClique ENTER para continuar...")

def validar_data(data_str, formato="%Y-%m-%d"):
    try:
        return datetime.strptime(data_str, formato)
    except ValueError:
        return None
        
def validar_data_hora(data_str, formato="%Y-%m-%d %H:%M"):
    try:
        data_valida = datetime.strptime(data_str, formato)
        return data_valida
    except ValueError:
        return None

def input_inteiro(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            console.print("[red]Entrada inválida! Insira um número inteiro.[/red]")

def input_obrigatorio(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        console.print("[red]---- ATENÇÃO -- Campo Obrigatório! ----[/red]")

def listar_pacientes_simples():
    pacientes = buscar_paciente_por_nome("")
    console.print("\nPacientes disponíveis:")
    for p in pacientes:
        console.print(f"ID: {p[0]} | Nome: {p[1]}")

def listar_medicos_simples():
    medicos = buscar_medico_por_nome("")
    console.print("\nMédicos disponíveis:")
    for m in medicos:
        console.print(f"ID: {m[0]} | Nome: {m[1]} | Especialidade: {m[2]}")

def listar_enfermeiros_simples():
    enfers = buscar_enfermeiro_por_nome("")
    console.print("\nEnfermeiros disponíveis:")
    for e in enfers:
        console.print(f"ID: {e[0]} | Nome: {e[1]}")

# --------------------------- #
#           LOGIN             #
# --------------------------- #

# vai fazer o login do utilizador no sistema com autenticação e feedback
def login():
    clear()
    console.print(Panel("#======# LOGIN NO SISTEMA #======#"))
    login = input("Username: ")
    senha = getpass.getpass("Password: ")

    user = autenticar_user(login, senha)
    if user:
        gravar_log(user[0], "login", "sucesso")
        console.print("[green]Login efetuado com sucesso![/green]\n")
        return user
    else:
        console.print("[red]Username ou password incorretos.[/red]")
        espera()
        return None

# ---------------- #
# menus do sistema #
# ---------------- #

def menu_admin(user):
    while True:
        clear()
        print(Panel("#=====# Menu Administrador #=====#"))
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
            op_in()
            espera()

def menu_paciente(user):
    while True:
        clear()
        print(Panel("#=====# Menu Paciente #=====#"))
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
            op_in()
            espera()

def menu_medico(user):
    while True:
        clear()
        print(Panel("#=====# Menu Médico #=====#"))
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
            op_in()
            espera()

def menu_enfermeiro(user):
    while True:
        clear()
        print(Panel("#=====# Menu Enfermeiro #=====#"))
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
            op_in()
            espera()

# ----------------- #
# funçoes dos menus #
# ----------------- #

# vai fazer o registo de um novo paciente com cifragem do prontuário
def adicionar_paciente_menu(user):
    clear()
    console.print(Panel("#==# Adicionar Paciente #==#"))
    nome = input_obrigatorio("Nome: ")
    
    while True:
        data_nasc = input("Data de nascimento (YYYY-MM-DD): ")
        if validar_data(data_nasc):
            break
        console.print("[red]Formato inválido. Use YYYY-MM-DD[/red]")
        
    genero = input_obrigatorio("Gênero: ")
    contato = input_obrigatorio("Contato: ")
    prontuario = input_obrigatorio("Prontuário médico (texto livre): ")
    prontuario_cifrado = cifrar(prontuario)  # cifra aqui!

    try:
        id_pac = adicionar_paciente(nome, data_nasc, genero, contato, prontuario_cifrado)
        gravar_log(user[0], "add_paciente", "sucesso")
        console.print(f"[green]Paciente adicionado com ID: {id_pac}[/green]")
    except Exception as e:
        gravar_log(user[0], "add_paciente", "falha")
        console.print(f"[red]Erro ao adicionar paciente:[/red] {e}")
    espera()

# vai adicionar médico ou enfermeiro conforme a escolha
def adicionar_funcionario_menu(user):
    clear()
    console.print(Panel("#==# Adicionar Funcionário #==#"))
    console.print("1. Médico")
    console.print("2. Enfermeiro")
    tipo = input("Opção: ")
    nome = input_obrigatorio("Nome: ")
    contato = input_obrigatorio("Contato: ")
    if tipo == "1":
        espec = input_obrigatorio("Especialidade: ")
        try:
            idm = adicionar_medico(nome, espec, contato)
            gravar_log(user[0], "add_medico", "sucesso")
            console.print(f"[green]Médico adicionado com ID: {idm}[/green]")
        except Exception as e:
            gravar_log(user[0], "add_medico", "falha")
            console.print(f"[red]Erro ao adicionar médico:[/red] {e}")
    elif tipo == "2":
        try:
            ide = adicionar_enfermeiro(nome, contato)
            gravar_log(user[0], "add_enfermeiro", "sucesso")
            console.print(f"[green]Enfermeiro adicionado com ID: {ide}[/green]")
        except Exception as e:
            gravar_log(user[0], "add_enfermeiro", "falha")
            console.print(f"[red]Erro ao adicionar enfermeiro:[/red] {e}")
    else:
        op_in()
    espera()

# vai agendar uma consulta com paciente e médico
def agendar_consulta_menu(user):
    clear()
    console.print(Panel("#==# Agendar Consulta #==#"))
    try:
        listar_pacientes_simples()
        id_pac = input_inteiro("ID do paciente: ")
        listar_medicos_simples()
        id_med = input_inteiro("ID do médico: ")
        while True:
            data_cons = input("Data da consulta (YYYY-MM-DD HH:MM): ")
            if validar_data_hora(data_cons):
                break
            console.print("[red]Formato inválido. Use YYYY-MM-DD HH:MM[/red]")
    
        status = "agendada"
        idc = agendar_consulta(id_pac, id_med, data_cons, status)
        gravar_log(user[0], "agendar_consulta", "sucesso")
        console.print(f"[green]Consulta agendada com ID: {idc}[/green]")
    except Exception as e:
        gravar_log(user[0], "agendar_consulta", "falha")
        console.print(f"[red]Erro ao agendar consulta:[/red] {e}")
    espera()


# vai adicionar um tratamento a um paciente
def adicionar_tratamento_menu(user):
    clear()
    console.print(Panel("#==# Adicionar Tratamento #==#"))
    try:
        listar_pacientes_simples()
        id_pac = input_inteiro("ID do paciente: ")
        descricao = input_obrigatorio("Descrição do tratamento (máx 1024): ")
        
        while True:
            data_trat = input("Data do tratamento (YYYY-MM-DD): ")
            if validar_data(data_trat):
                break
            console.print("[red]Formato inválido. Use YYYY-MM-DD[/red]")

        idt = adicionar_tratamento(id_pac, descricao[:1024], data_trat)
        gravar_log(user[0], "add_tratamento", "sucesso")
        console.print(f"[green]Tratamento adicionado com ID: {idt}[/green]")
    except Exception as e:
        gravar_log(user[0], "add_tratamento", "falha")
        console.print(f"[red]Erro ao adicionar tratamento:[/red] {e}")
    espera()

# vai adicionar uma prescrição a um paciente
def adicionar_prescricao_menu(user):
    clear()
    console.print(Panel("#==# Adicionar Prescrição #==#"))
    try:
        listar_pacientes_simples()
        id_pac = input_inteiro("ID do paciente: ")
        listar_medicos_simples()
        id_med = input_inteiro("ID do médico: ")
        medicamento = input_obrigatorio("Nome do medicamento: ")
        
        while True:
            data_presc = input("Data da prescrição (YYYY-MM-DD): ")
            if validar_data(data_presc):
                break
            console.print("[red]Formato inválido. Use YYYY-MM-DD[/red]")

        idp = adicionar_prescricao(id_pac, id_med, medicamento, data_presc)
        gravar_log(user[0], "add_prescricao", "sucesso")
        console.print(f"[green]Prescrição adicionada com ID: {idp}[/green]")
    except Exception as e:
        gravar_log(user[0], "add_prescricao", "falha")
        console.print(f"[red]Erro ao adicionar prescrição:[/red] {e}")
    espera()

# vai buscar e mostrar pacientes com output limpo
def visualizar_pacientes_menu(user):
    clear()
    console.print(Panel("#==# Buscar Pacientes #==#"))
    console.print("(deixe em branco para visualizar todos)")
    console.print("1. Por nome")
    console.print("2. Por contato")
    op = input("Opção: ")
    if op == "1":
        nome = input("Nome: ")
        pacientes = buscar_paciente_por_nome(nome)
    else:
        contato = input("Contato: ")
        pacientes = buscar_paciente_por_contato(contato)

    console.print("\n[bold]Resultados:[/bold]")
    if pacientes:
        for pac in pacientes:
            console.print(f"[cyan]{pac[0]}[/cyan] | {pac[1]} | {pac[2]} | {pac[3]} | {pac[4]}")
    else:
        console.print("[yellow]Nenhum paciente encontrado.[/yellow]")
    gravar_log(user[0], "visualizar_pacientes", "sucesso")
    espera()

# vai mostrar lista de médicos ou enfermeiros
def visualizar_funcionarios_menu(user, so_medicos=False):
    clear()
    if so_medicos:
        console.print(Panel("#==# Médicos #==#"))
        medicos = buscar_medico_por_nome("")
        if medicos:
            for m in medicos:
                console.print(f"[cyan]{m[0]}[/cyan] | {m[1]} | {m[2]} | {m[3]}")
        else:
            console.print("[yellow]Nenhum médico encontrado.[/yellow]")
    else:
        console.print("1. Médicos\n2. Enfermeiros")
        op = input("Opção: ")
        if op == "1":
            medicos = buscar_medico_por_nome("")
            if medicos:
                for m in medicos:
                    console.print(f"[cyan]{m[0]}[/cyan] | {m[1]} | {m[2]} | {m[3]}")
            else:
                console.print("[yellow]Nenhum médico encontrado.[/yellow]")
        else:
            enfers = buscar_enfermeiro_por_nome("")
            if enfers:
                for e in enfers:
                    console.print(f"[cyan]{e[0]}[/cyan] | {e[1]} | {e[2]}")
            else:
                console.print("[yellow]Nenhum enfermeiro encontrado.[/yellow]")
    gravar_log(user[0], "visualizar_funcionarios", "sucesso")
    espera()

# vai modificar o contato de um utilizador (paciente/médico/enfermeiro)
def modificar_contato_menu(user):
    clear()
    console.print(Panel("#==# Modificar Contato #==#"))
    console.print("1. Paciente")
    console.print("2. Médico")
    console.print("3. Enfermeiro")
    op = input("Qual tipo de utilizador? ")
    try:
        if op == "1":
            listar_pacientes_simples()
        elif op == "2":
            listar_medicos_simples()
        elif op == "3":
            listar_enfermeiros_simples()
        id = input_inteiro("ID do utilizador: ")
        novo_contato = input_obrigatorio("Novo contato: ")
        if op == "1":
            editar_paciente(id, contato=novo_contato)
        elif op == "2":
            editar_medico(id, contato=novo_contato)
        elif op == "3":
            editar_enfermeiro(id, contato=novo_contato)
        else:
            op_in()
            return
        gravar_log(user[0], "modificar_contato", "sucesso")
        console.print("[green]Contato atualizado![/green]")
    except Exception as e:
        gravar_log(user[0], "modificar_contato", "falha")
        console.print(f"[red]Erro:[/red] {e}")
    espera()

# vai mostrar consultas por data ou intervalo
def visualizar_consultas_menu(user, so_meu_medico=False):
    clear()
    console.print(Panel("#==# Visualizar Consultas #==#"))
    console.print("1. Por dia")
    console.print("2. Por intervalo")
    op = input("Opção: ")
    try:
        if op == "1":
            
            while True:
                data = input("Data (YYYY-MM-DD): ")
                if validar_data(data):
                    break
                console.print("[red]Data inválida. Use o formato YYYY-MM-DD[/red]")
            consultas = buscar_consultas_por_data(data)

        else:
            while True:
                data1 = input("Data início (YYYY-MM-DD): ")
                data2 = input("Data fim (YYYY-MM-DD): ")
                if validar_data(data1) and validar_data(data2):
                    break
                console.print("[red]Datas inválidas. Use o formato YYYY-MM-DD[/red]")
            
            consultas = buscar_consultas_intervalo(data1, data2)

        for c in consultas:
            console.print(c)
        gravar_log(user[0], "visualizar_consultas", "sucesso")
    except Exception as e:
        console.print(f"[red]Erro ao buscar consultas:[/red] {e}")
    espera()

# vai mostrar os tratamentos de um paciente com info do médico
def visualizar_tratamentos_menu(user):
    clear()
    console.print(Panel("#==# Visualizar Tratamentos #==#"))
    try:
        listar_pacientes_simples()
        idp = input_inteiro("ID do paciente: ")
        tratamentos = buscar_tratamentos_paciente_com_medico(idp)
        for t in tratamentos:
            console.print(f"ID: {t[0]}, Descrição: {t[1]}, Data: {t[2]}, Médico: {t[3] or '---'}")
        gravar_log(user[0], "visualizar_tratamentos", "sucesso")
    except Exception as e:
        console.print(f"[red]Erro:[/red] {e}")
    espera()

# vai mostrar prescrições feitas por médico, com filtros
def visualizar_prescricoes_menu(user, so_meu_medico=False):
    clear()
    console.print(Panel("#==# Visualizar Prescrições #==#"))
    try:
        if so_meu_medico:
            id_med = user[0]
        else:
            listar_medicos_simples()
            id_med = input_inteiro("ID do médico: ")
        console.print("1. Por período")
        console.print("2. Por faixa etária e período")
        op = input("Opção: ")
        while True:
            data1 = input("Data início (YYYY-MM-DD): ")
            data2 = input("Data fim (YYYY-MM-DD): ")
            if validar_data(data1) and validar_data(data2):
                break
            console.print("[red]Datas inválidas. Use o formato YYYY-MM-DD[/red]")

        if op == "1":
            prescricoes = buscar_prescricoes_por_medico_periodo(id_med, data1, data2)
        else:
            idade_min = input_inteiro("Idade mínima: ")
            idade_max = input_inteiro("Idade máxima: ")
            prescricoes = buscar_prescricoes_medico_idade(id_med, idade_min, idade_max, data1, data2)
        for p in prescricoes:
            console.print(p)
        gravar_log(user[0], "visualizar_prescricoes", "sucesso")
    except Exception as e:
        console.print(f"[red]Erro:[/red] {e}")
    espera()

# vai mostrar conteúdo de uma tabela à escolha
def visualizar_tabela_menu(user):
    clear()
    console.print(Panel("#==# Visualizar Tabela #==#"))
    tabela = input("Nome da tabela: ")
    try:
        dados = buscar_todos_conteudo_tabela(tabela)
        for d in dados:
            console.print(d)
        gravar_log(user[0], f"visualizar_tabela_{tabela}", "sucesso")
    except Exception as e:
        console.print(f"[red]Erro:[/red] {e}")
    espera()

# vai mostrar logs de acessos
def visualizar_log_menu(user):
    clear()
    console.print(Panel("#==# Log de Acessos #==#"))
    console.print("1. Por período")
    console.print("2. Por utilizador")
    op = input("Opção: ")
    try:
        if op == "1":
            
            while True:
                data1 = input("Data início (YYYY-MM-DD): ")
                data2 = input("Data fim (YYYY-MM-DD): ")
                if validar_data(data1) and validar_data(data2):
                    break
                console.print("[red]Datas inválidas. Use o formato YYYY-MM-DD[/red]")
            logs = buscar_logs_por_periodo(data1, data2)
            
        else:
            id_user = input_inteiro("ID do utilizador: ")
            logs = buscar_logs_por_user(id_user)
        for l in logs:
            console.print(l)
    except Exception as e:
        console.print(f"[red]Erro:[/red] {e}")
    espera()

# vai excluir um paciente
def excluir_paciente_menu(user):
    clear()
    console.print(Panel("#==# Excluir Paciente #==#"))
    listar_pacientes_simples()
    idp = input_inteiro("ID do paciente a excluir: ")
    try:
        afetados = excluir_paciente(idp)
        if afetados:
            console.print("[green]Paciente excluído com sucesso.[/green]")
            gravar_log(user[0], "excluir_paciente", "sucesso")
        else:
            console.print("[yellow]ID não encontrado.[/yellow]")
            gravar_log(user[0], "excluir_paciente", "falha")
    except Exception as e:
        console.print(f"[red]Erro:[/red] {e}")
    espera()

# vai excluir um médico
def excluir_medico_menu(user):
    clear()
    console.print(Panel("#==# Excluir Médico #==#"))
    listar_medicos_simples()
    idm = input_inteiro("ID do médico a excluir: ")
    try:
        afetados = excluir_medico(idm)
        if afetados:
            console.print("[green]Médico excluído com sucesso.[/green]")
            gravar_log(user[0], "excluir_medico", "sucesso")
        else:
            console.print("[yellow]ID não encontrado.[/yellow]")
            gravar_log(user[0], "excluir_medico", "falha")
    except Exception as e:
        console.print(f"[red]Erro:[/red] {e}")
    espera()

# vai excluir um enfermeiro
def excluir_enfermeiro_menu(user):
    clear()
    console.print(Panel("#==# Excluir Enfermeiro #==#"))
    listar_enfermeiros_simples()
    ide = input_inteiro("ID do enfermeiro a excluir: ")
    try:
        afetados = excluir_enfermeiro(ide)
        if afetados:
            console.print("[green]Enfermeiro excluído com sucesso.[/green]")
            gravar_log(user[0], "excluir_enfermeiro", "sucesso")
        else:
            console.print("[yellow]ID não encontrado.[/yellow]")
            gravar_log(user[0], "excluir_enfermeiro", "falha")
    except Exception as e:
        console.print(f"[red]Erro:[/red] {e}")
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
    novo_contato = input_obrigatorio("Novo contato: ")
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
    try:
        conectar()
        try:
            # verifica se a tabela Users existe e tem dados
            total = contar_registros("Users")
        except Exception as e:
            print("[INFO] Tabela 'Users' não existe. A criar estrutura e dados iniciais...")
            create_data_debug()
            main()  # relança o main após inserção
            return

        if total > 0:
            print("Base de dados pronta.")
            while True:
                user = None
                while not user:
                    user = login()
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
        else:
            print("[INFO] A tabela Users está vazia. A inserir dados de debug...")
            create_data_debug()
            main()
    except Exception as e:
        print("Erro fatal:", e)

if __name__ == "__main__":
    main()
