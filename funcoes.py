#----------------------REGISTROS------------------------
from datetime import date, datetime      
import json                              
import os                                
from dateutil.relativedelta import relativedelta

# Nome do TERCEIRO ARQUIVO (onde ficam salvos os dados puros)
ARQUIVO_JSON = "registros_academia.json"

def sair():
    print("Saindo do sistema... Até logo, Treinador!")

#------------------------------------------EXCEÇÕES - (TUDO QUE NÃO PODE OCORRER)------------------------        
def validar_idade(texto):
    while True:
        try:
            idade = int(input(texto))
            if 0 < idade < 120:
                return idade
            print("Por favor, digite uma idade válida (entre 1 e 120 anos).")
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

#----------------FUNÇÃO REUTILIZÁVEL-----------------------
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

    opcao2 = validar_opcao("1 - Realizar novo registro\n 2 - Acessar registros já cadastrados e checar bloqueios\n 3 - Planos\n Escolha: ", [1, 2, 3])
    
    if opcao2 == 1:
        nome = input("Digite seu nome completo: ")
        peso = validar_float("Digite o seu peso atual *em gramas: ") 
        altura = validar_float("Digite a sua altura *em centímetros: ")
        idade = validar_idade("Digite a sua idade: ")
        opcao3 = validar_opcao("Digite a opção desejada: \n 1 - Acessar planos/modalidades e horários\n 2 - Voltar\n Escolha: ", [1, 2])

        # Variáveis iniciando vazias
        opcao_planos = "Vazio"
        opcao_modalidades = "Vazio"
        data_matricula_str = "Vazio"
        data_vencimento_str = "Vazio"
        pagamento_status = "Não Efetuado" # Começa padrão como não efetuado caso o usuário volte

        if opcao3 == 1:
            print("Conheça nossos planos:")
            opcao_planos = validar_opcao("1 - Plano Caverna Diglet (básico) R$:100,00:\n Inclui equipamentos de uso diário, uso do espaço para lanches e local para banhos.\n\n 2 - Plano Área da elite (premium) R$: 200,00:\n Inclui sauna privativa;\n acompanhamento com nutricionista;\n personal trainner especializado;\n e brindes personalizados da nossa academia.\n\n**Esses valores não incluem as modalidades escolhidas a parte**\n Escolha: ", [1, 2])
                    
            print("Escolha a duração do plano:")
            frequencia = validar_opcao("1 - Mensal\n2 - Trimestral\n3 - Anual\n Escolha: ", [1, 2, 3])
                    
            # Cálculo automático das datas
            hoje = date.today()
            meses_adicionais = meses_por_frequencia.get(frequencia, 1) 
            vencimento = hoje + relativedelta(months=meses_adicionais)
                    
            data_matricula_str = hoje.strftime("%d/%m/%Y")
            data_vencimento_str = vencimento.strftime("%d/%m/%Y")

            opcao_modalidades = validar_opcao("\nPara deixar o nosso serviço ainda mais completo temos as modalidades que ficam a escolha do cliente, quantas quiser!\n 1 - Crossfit\n 2 - Pilates\n 3 - Zumba\n 4 - Jiu-jitsu\n Escolha: ", [1, 2, 3, 4])

            # --- NOVO: MENU DE PAGAMENTO FICTÍCIO ---
            print("\n" + "="*30)
            print("      TELA DE PAGAMENTO")
            print("="*30)
            forma_pago = validar_opcao("Escolha a forma de pagamento:\n 1 - PIX\n 2 - Cartão de Crédito\n Escolha: ", [1, 2])
            
            if forma_pago == 1:
                pagamento_status = "Efetuado via PIX"
                print("\n[Sistema] Gerando QR Code fictício... Pagamento aprovado!")
            elif forma_pago == 2:
                pagamento_status = "Efetuado via Cartão de Crédito"
                print("\n[Sistema] Processando dados do cartão... Pagamento aprovado!")
            print("="*30)

        # O campo 'pagamento' foi adicionado aqui no dicionário
        registro = {
            "nome": nome,
            "peso": peso,
            "altura": altura,
            "idade": idade,
            "opcao_planos": opcao_planos,
            "opcao_modalidades": opcao_modalidades,
            "data_matricula": data_matricula_str,
            "data_vencimento": data_vencimento_str,
            "pagamento": pagamento_status # Salva o método de pagamento no registro
        }

        registros.append(registro) 
        
        # PASSO A PASSO JSON: Salva no terceiro arquivo separado
        with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
            json.dump(registros, f, indent=4, ensure_ascii=False)
            
        print("\n--- Registro Concluído com Sucesso! ---")
        print(registros)

    elif opcao2 == 2:
        print("\n--- STATUS DE ACESSO DOS ALUNOS ---")
        if not registros:
            print("Nenhum registro encontrado no arquivo.")
        else:
            for r in registros:
                vencimento_str = r["data_vencimento"]
                forma_pagamento = r.get("pagamento", "Não Efetuado") # Pega o pagamento salvo ou define padrão
                
                # Se o pagamento não foi feito ou o usuário voltou, o acesso é bloqueado
                if vencimento_str == "Vazio" or forma_pagamento == "Não Efetuado":
                    status = "🔴 Acesso Bloqueado (Falta efetuar pagamento do plano)"
                else:
                    # Compara a data de hoje com o vencimento guardado no JSON
                    hoje = date.today()
                    data_vencimento = datetime.strptime(vencimento_str, "%d/%m/%Y").date()
                    
                    if hoje > data_vencimento:
                        status = "🔴 Acesso Bloqueado (Mensalidade Vencida)"
                    else:
                        status = f"🟢 Acesso Liberado ({forma_pagamento})"
                
                print(f"Treinador: {r['nome']} | Vencimento: {vencimento_str} | Status: {status}")

    elif opcao2 == 3:
        print("\n--- INFORMAÇÕES DE PLANOS ---")
        print("1. Plano Caverna Diglet - Básico R$:100,00")
        print("2. Plano Área da Elite - Premium R$:200,00")
