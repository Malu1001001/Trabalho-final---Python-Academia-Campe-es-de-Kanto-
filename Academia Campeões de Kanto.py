from datetime import date
from dateutil.relativedelta import relativedelta

print("Bem vindos a Academia Campeões de Kanto")
print(" "*90)
print("MISSÃO: Nossa missão é guiar a jornada de cada aluno rumo ao seu potencial máximo, transformando o esforço diário em evolução\n constante. Queremos despertar o verdadeiro mestre que existe em você,superando qualquer desafio dentro e fora do treino.")
print(" "*90)
print("VISÃO: Nossa visão é consolidar a Campeões de Kanto como o principal ginásio de referência em saúde e alta performance.Buscamos\n expandir nossa comunidade e formar uma liga de líderes imparáveis, prontos para alcançar o topo.")
print(" "*90)
print("VALORES: Nossos valores são a Evolução Contínua para ficar mais forte a cada dia e o Espírito de Treinador focado em disciplina. \nFortalecemos a União de Equipe no apoio mútuo e a Resiliência de Rocha para superar qualquer obstáculo.")

print("--"*90)

registros = []
aulas = []  # Inicializada fora do loop para não apagar os dados a cada repetição

# Mapeamento para o cálculo de vencimento das datas
meses_por_frequencia = {1: 1, 2: 3, 3: 12}  # 1=Mensal, 2=Trimestral, 3=Anual crie essas variáveis agora com o valor 'Vazio'. Se o usuário entrar nos planos, a gente muda o valor delas. Se ele decidir voltar, elas continuam existindo (vazias), e o dicionário é criado sem quebrar o sistema

while True:
    opcao = int(input("\nDigite a opção desejada:\n 1 - Acessar registros\n 2 - Acessar sistema da academia\n 3 - Sair\n "))
    
    if opcao == 3:
        print("Saindo do sistema... Até logo, Treinador!")
        break
        
    elif opcao == 1:
        opcao2 = int(input("1 - Realizar novo registro\n 2 - Acessar registro já cadastrado\n"))
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

            registros.append(registro) # Salvando o dicionário w
            print("\n--- Registro Concluído com Sucesso! ---")
            print(registros)

    elif opcao == 2:
        print("--"*90)
        print("BEM-VINDO AO SISTEMA DA ACADEMIA!")
        print("--"*90)
        opcao_sistema = int(input("Digite a opção desejada:\n 1 - Adicionar professor(a)/aula\n 2 - Alterar professor(a)/aula\n 3 - Adicionar modalidade\n 4 - Alterar modalidades\n"))
        
        if opcao_sistema == 1:
            professor = input("Digite o nome do professor: ")
            horario = float(input("Digite o horário da aula: "))
            modalidade = input("Digite a modalidade: ")

            aula = {
                "professor": professor,
                "horário": horario,
                "modalidade": modalidade,
            }
            aulas.append(aula)
            print("Aula adicionada com sucesso!")

        elif opcao_sistema == 2:
            professor1 = input("Digite o nome do professor que deseja substituir: ")
            professor2 = input("Digite o nome do professor que entrará no lugar: ")
            for aula in aulas:
                if aula["professor"] == professor1:
                    aula["professor"] = professor2
                    print("Professor substituído com sucesso!")
                    break

                #Não sei se faço isso com os horários tbm...

        elif opcao_sistema == 3:
            # Reaproveitando a lógica de adicionar aula
            professor = input("Digite o nome do professor da nova modalidade: ")
            horario = float(input("Digite o horário: "))
            modalidade = input("Digite a nova modalidade: ")
            aula = {
                "professor": professor,
                "horário": horario,
                "modalidade": modalidade,
                #eu preciso copiar o dicionário todo de novo só pra mudar a modalidade?
            }
            aulas.append(aula)
            print("Nova modalidade cadastrada!")
            
        elif opcao_sistema == 4:
            modalidade1 = input("Digite a modalidade a ser substituída: ")
            modalidade2 = input("Digite a modalidade que entrará no lugar: ")
            for aula in aulas:
                if aula["modalidade"] == modalidade1:
                    aula["modalidade"] = modalidade2
                    print("Modalidade substituída com sucesso!")
                    break