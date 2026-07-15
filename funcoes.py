#----------------------REGISTROS(matriculas de todo mundo)-----------------------
from datetime import date, datetime      
import json                              
import os                                
from dateutil.relativedelta import relativedelta
import subprocess                        

# Nome do TERCEIRO ARQUIVO (onde ficam salvos os dados puros)
ARQUIVO_JSON = "registros_academia.json"

def sair():
    print("--Salvando o seu progresso no diário... Não desligue o console.--")
    print("-- Até logo, Treinador! Sua jornada rumo à Liga Pokémon continua em breve!--")

#-----------------------------------UM SOMZIM TEMPORÁRIO---------------------------------------------

def tocar_som_pokemon(musiquinhapokemon):
    """Função reutilizável para tocar qualquer arquivo MP3 no Linux"""
    try:
        comando = ["ffplay", "-nodisp", "-autoexit", musiquinhapokemon]
        subprocess.Popen(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        pass # Se o computador não tiver o tocador ou o arquivo sumir, o sistema continua rodando sem travar (vai que eu esqueço e apago)


#------------------------------------------EXCEÇÕES - (TUDO QUE NÃO PODE OCORRER)------------------------        
def validar_idade(texto):
    while True:
        try:
            idade = int(input(texto))
            if 0 < idade < 120:
                return idade
            print("Por favor, digite uma idade válida (entre 1 e 120 anos).") #vai que existe alguém assim né, no guiness tem...
        except ValueError:
            print("Erro: Digite apenas números inteiros! Tente novamente.")

def validar_float(texto):
    """Valida entradas decimais como Peso e Altura"""
    while True:
        try:
            valor = float(input(texto))
            if valor > 0:
                return valor
            print("Por favor, digite un valor maior que zero.")
        except ValueError:
            print("Erro: Digite apenas números (use ponto em vez de vírgula). Tente novamente.")

#----------------FUNÇÃO REUTILIZÁVEL (dá pra usar pra várias coisas ex.: digitar somente os números presente no menu :) )-----------------------
def validar_opcao(texto, opcoes_validas):
    """Garante que o usuário escolha apenas uma das opções numéricas do menu"""
    while True:
        try:
            opcao = int(input(texto))
            if opcao in opcoes_validas:
                return opcao
            print(f"Opção inválida! Escolha uma das opções: {opcoes_validas}")
        except ValueError:
            print("Erro: Digite apenas o número da opção desejada.")

def acessar_registros():
    # PASSO A PASSO JSON: Se o terceiro arquivo já existir, traz os dados dele.
    if os.path.exists(ARQUIVO_JSON):
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
            registros = json.load(f)
    else:
        registros = []
        
    meses_por_frequencia = {1: 1, 2: 3, 3: 12}  

# MENU SIMPLIFICADO:novo registro, consulta de bloqueios, planos, relatórios e CRUD (menu "principal, ou secundário no caso")
    opcao2 = validar_opcao("1 - Realizar novo registro\n 2 - Acessar registros já cadastrados e checar bloqueios\n 3 - Planos\n 4 - Relatórios com Filtros\n 5 - Alterar ou Remover Aluno\n Escolha: ", [1, 2, 3, 4, 5])
    print("--"*90)
    
    if opcao2 == 1:
        nome = input("Digite seu nome completo: ")
        peso = validar_float("Digite o seu peso atual *em gramas: ") 
        altura = validar_float("Digite a sua altura *em centímetros: ")
        idade = validar_idade("Digite a sua idade: ")
        opcao3 = validar_opcao("Digite a opção desejada: \n 1 - Acessar planos/modalidades e horários\n 2 - Voltar\n Escolha: ", [1, 2])

        opcao_planos = "Vazio"
        opcao_modalidades = "Vazio"
        data_matricula_str = "Vazio"
        data_vencimento_str = "Vazio"
        pagamento_status = "Não Efetuado" # Começa padrão como não efetuado caso o usuário volte

        if opcao3 == 1:
            print("Conheça nossos planos:")
            opcao_planos = validar_opcao("1 - Plano Caverna Diglet (básico) R$:100,00:\n Inclui equipamentos de uso diário, uso do espaço para lanches e local para banhos.\n\n 2 - Plano Área da elite (premium) R$: 200,00:\n Inclui sauna privativa;\n acompanhamento com nutricionista;\n personal trainner especializado;\n e brindes personalizados da nossa academia.\n\n**Esses valores não incluem as modalidades escolhidas a parte**\n Escolha: ", [1, 2])
            print("--"*90)
                   
            print("Escolha a duração do plano:")
            frequencia = validar_opcao("1 - Mensal\n2 - Trimestral\n3 - Anual\n Escolha: ", [1, 2, 3])
            print("--"*90)

# Cálculo automático das datas
            hoje = date.today()
            meses_adicionais = meses_por_frequencia.get(frequencia, 1) 
            vencimento = hoje + relativedelta(months=meses_adicionais)
                    
            data_matricula_str = hoje.strftime("%d/%m/%Y")
            data_vencimento_str = vencimento.strftime("%d/%m/%Y")

# --- CONCILIANDO AS TURMAS DE PROFESSORES COM LIMITE DE 40 ALUNOS ---
            if os.path.exists("aulas_academia.json"):
                with open("aulas_academia.json", "r", encoding="utf-8") as f:
                    aulas_academia = json.load(f)
            else:
                aulas_academia = []

            if not aulas_academia:
                print("\n[Aviso] Nenhum professor ou horário cadastrado pela administração ainda!")
                opcao_modalidades = "Nenhuma aula escolhida"
            else:
                print("--"*90)
                print("\n--- TURMAS E HORÁRIOS DISPONÍVEIS (Limite: 40 por turma) ---")
                opcoes_validas_turma = []
                
                for idx, turma in enumerate(aulas_academia, start=1):
                    vagas = 40 - turma["alunos_matriculados"]
                    print(f" {idx} - {turma['modalidade'].upper()} | Prof. {turma['professor']} | Horário: {turma['horário']} ({vagas} vagas restantes)")
                    opcoes_validas_turma.append(idx)
                
                while True:
                    escolha_turma = validar_opcao("Escolha o número da turma que deseja se matricular: ", opcoes_validas_turma)
                    turma_selecionada = aulas_academia[escolha_turma - 1]
                    
                    if turma_selecionada["alunos_matriculados"] >= 40:
                        print("-- Um SNORLAX selvagem apareceu e bloqueou a entrada desta turma! -- ")
                        print(" --  (Turma lotada com 40 treinadores. Escolha outro horário ou use uma Poké Flauta.) -- ")

                    else:
                        turma_selecionada["alunos_matriculados"] += 1
                        
                        with open("aulas_academia.json", "w", encoding="utf-8") as f:
                            json.dump(aulas_academia, f, indent=4, ensure_ascii=False)
                            
                        opcao_modalidades = f"{turma_selecionada['modalidade']} com Prof. {turma_selecionada['professor']} às {turma_selecionada['horário']}"
                        print(f" Matrícula confirmada na turma de {turma_selecionada['modalidade']}!")
                        break

# -------------------------------------------------- MENU DE PAGAMENTO FICTÍCIO -------------------------------------------------------------
            print("="*30)
            print("      TELA DE PAGAMENTO")
            print("="*30)
            forma_pago = validar_opcao("Escolha a forma de pagamento:\n 1 - PIX\n 2 - Cartão de Crédito\n Escolha: ", [1, 2])
            
            if forma_pago == 1:
                pagamento_status = "Efetuado via PIX"
                tocar_som_pokemon("pokemon_healed.mp3")
                print("\n[Sistema] QR Code gerado... Pagamento aprovado!")
            elif forma_pago == 2:
                pagamento_status = "Efetuado via Cartão de Crédito"
                tocar_som_pokemon("pokemon_healed.mp3")
                print("\n[Sistema] Cartão processado... Pagamento aprovado!")
            print("="*30)

        # Montagem correta da ficha do aluno e salvamento do valor arrecadado
        valor_base = 100.0 if opcao_planos == 1 else (200.0 if opcao_planos == 2 else 0.0)
        registro = {
            "nome": nome,
            "peso": peso,
            "altura": altura,
            "idade": idade,
            "opcao_planos": opcao_planos,
            "opcao_modalidades": opcao_modalidades,
            "data_matricula": data_matricula_str,
            "data_vencimento": data_vencimento_str,
            "pagamento": pagamento_status,
            "valor_pago": valor_base
        }
        registros.append(registro)
        
        with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
            json.dump(registros, f, indent=4, ensure_ascii=False)
        
        print("=================== CENTRO POKÉMON ===================")
        print("  Nurse Joy: 'Obrigada por esperar. Nós restauramos os seus atributos...")
        print("  parâmetros de Treinador para o potencial máximo!'")
        print("  -- Cadastro concluído! Esperamos ver você novamente! --")
        print("======================================================")



    elif opcao2 == 2:
        print("--- STATUS DE ACESSO DOS ALUNOS ---")
        if not registros:
            print("Nenhum registro encontrado no arquivo separado.")
        else:
            for r in registros:
                vencimento_str = r["data_vencimento"]
                forma_pagamento = r.get("pagamento", "Não Efetuado")
                
                if vencimento_str == "Vazio" or forma_pagamento == "Não Efetuado":
                    status = "Acesso Bloqueado (Inadimplente / Falta plano)"
                else:
                    hoje = date.today()
                    data_vencimento = datetime.strptime(vencimento_str, "%d/%m/%Y").date()
                    if hoje > data_vencimento:
                        status = "Acesso Bloqueado (Mensalidade Vencida)"
                    else:
                        status = f"Acesso Liberado ({forma_pagamento})"
                
                print(f"Treinador: {r['nome']} | Vencimento: {vencimento_str} | Status: {status}")

    elif opcao2 == 3:
        print("\n--- INFORMAÇÕES DE PLANOS ---")
        print("1. Plano Caverna Diglet - Básico R$:100,00")
        print("2. Plano Área da Elite - Premium R$:200,00")

        # 4 - REQUISITO EXIGIDO: Relatórios com filtros estruturados (Soma financeira e lista de inadimplentes)
    elif opcao2 == 4:
        print("\n--- CENTRAL DE RELATÓRIOS ---")
        filtro = validar_opcao("1 - Listar apenas Alunos Inadimplentes (Bloqueados)\n2 - Faturamento Financeiro Total Arrecadado\n Escolha: ", [1, 2])
        
        if filtro == 1:
            print("\n--- ALUNOS INADIMPLENTES / BLOQUEADOS ---")
            cont = 0
            for r in registros:
                vencimento_str = r["data_vencimento"]
                
                # Se o aluno voltou (Vazio) ou a data de vencimento já passou da data de hoje
                if vencimento_str == "Vazio" or datetime.strptime(vencimento_str, "%d/%m/%Y").date() < date.today():
                    print(f" Aluno: {r['nome']} | Plano Vencido em: {vencimento_str}")
                    cont += 1
            
            if cont == 0:
                print("Excelente! Nenhum aluno inadimplente encontrado.")
            else:
                print(f"\nTotal de alunos inadimplentes: {cont}")
                
        elif filtro == 2:
            print("\n--- RELATÓRIO FINANCEIRO DE KANTO ---")
            total = sum(r.get("valor_pago", 0.0) for r in registros)
            print(f"Receita Bruta Total Arrecadada: R$ {total:.2f}")
            print(f"Total de matrículas ativas no sistema: {len(registros)}")

                    
