#----------------------REGISTROS------------------------
from datetime import date
from dateutil.relativedelta import relativedelta

def sair():
    print("Saindo do sistema... Até logo, Treinador!")
def  acessar_registros():
    registros=[]
    # Mapeamento para o cálculo de vencimento das datas
    meses_por_frequencia = {1: 1, 2: 3, 3: 12}  # 1=Mensal, 2=Trimestral, 3=Anual crie essas variáveis agora com o valor 'Vazio'. Se o usuário entrar nos planos, a gente muda o valor delas. Se ele decidir voltar, elas continuam existindo (vazias), e o dicionário é criado sem quebrar o sistema

    opcao2 = int(input("1 - Realizar novo registro\n 2 - Acessar registro já cadastrado\n 3 - Planos\n"))
    if opcao2 == 1:
        nome = input("Digite seu nome completo: ")
        peso = float(input("Digite o seu peso atual *em gramas: "))
        altura = float(input("Digite a sua altura *em centímetros: "))
        idade = int(input("Digite a sua idade: "))
        opcao3 = int(input("Digite a opção desejada: \n 1 - Acessar planos/modalidades e horários\n 2 - Voltar\n"))

        #none pra quando voltar tudo não ter que criar de novo...
        opcao_planos = None
        opcao_modalidades = None
        data_matricula_str = None
        data_vencimento_str = None

        if opcao3 == 1:
            print("Conheça nossos planos:")
            opcao_planos = int(input("1 - Plano Caverna Diglet (básico) R$:100,00:\n Inclui equipamentos de uso diário, uso do espaço para lanches e local para banhos.\n\n 2 - Plano Área da elite (premium) R$: 200,00:\n Inclui sauna privativa;\n acompanhamento com nutricionista;\n personal trainner especializado;\n e brindes personalizados da nossa academia.\n\n**Esses valores não incluem as modalidades escolhidas a parte**\n"))
                    
            # --- NOVO: Escolha da recorrência para cálculo das datas ---
            print("Escolha a duração do plano:")
            frequencia = int(input("1 - Mensal\n2 - Trimestral\n3 - Anual\n"))
                    
            # Cálculo automático das datas
            hoje = date.today()
            meses_adicionais = meses_por_frequencia.get(frequencia, 1) # Padrão 1 mês caso digite errado
            vencimento = hoje + relativedelta(months=meses_adicionais)
                    
            # Formatando para o padrão brasileiro string
            data_matricula_str = hoje.strftime("%d/%m/%Y")
            data_vencimento_str = vencimento.strftime("%d/%m/%Y")
            # -----------------------------------------------------------

            opcao_modalidades = int(input("\nPara deixar o nosso serviço ainda mais completo temos as modalidades que ficam a escolha do cliente, quantas quiser!\n 1 - Crossfit\n 2 - Pilates\n 3 - Zumba\n 4 - Jiu-jitsu\n"))
            #e como eu vou saber qual o horário de cada modalidade? se ela está está disponível? se é horário comercial ou não?

            registro = {
            "nome": nome,
            "peso": peso,
            "altura": altura,
            "idade": idade,
            "opcao_planos": opcao_planos,
            "opcao_modalidades": opcao_modalidades,
            "data_matricula": data_matricula_str,
            "data_vencimento": data_vencimento_str
                }

            registros.append(registro) # Salvando o dicionário 
        print("\n--- Registro Concluído com Sucesso! ---")
        print(registros)
            