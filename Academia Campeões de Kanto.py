import funcoes 


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

while True:
    opcao = int(input("\nDigite a opção desejada:\n 1 - Acessar registros\n 2 - Acessar sistema da academia\n 3 - Sair\n "))
    
    if opcao == 3:
        funcoes.sair()
        break
        
    elif opcao == 1:
        funcoes.acessar_registros()
            

            #agora como que eu voltaria lá pra cima???????????????????????????????????????????W

    elif opcao == 2:
        print("--"*90)
        print("BEM-VINDO AO SISTEMA DA ACADEMIA!")
        print("--"*90)
        opcao_sistema = int(input("Digite a opção desejada:\n 1 - Adicionar professor(a)/aula\n 2 - Alterar professor(a)/aula\n 3 - Adicionar modalidade\n 4 - Alterar modalidades\n"))
        
        if opcao_sistema == 1:
            professor = input("Digite o nome do professor: ")
            horario = float(input("Digite o horário da aula: ")) #o horario tem que ser em qual formato? 12:00? 12h? será se o sistema sabe que 9 da noite são 21:00??????????????????????????????W
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

                #Não sei se faço isso com os horários tbm...????????????????????????????????????

        elif opcao_sistema == 3:
            # Reaproveitando a lógica de adicionar aula
            professor = input("Digite o nome do professor da nova modalidade: ")
            horario = float(input("Digite o horário: "))
            modalidade = input("Digite a nova modalidade: ")
            aula = {
                "professor": professor,
                "horário": horario,
                "modalidade": modalidade,
                #eu preciso copiar o dicionário todo de novo só pra mudar a modalidade?????????????????????????????????????????????WWW
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

