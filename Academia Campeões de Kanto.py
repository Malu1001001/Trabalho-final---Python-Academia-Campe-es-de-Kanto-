import funcoes 
import json                          # Necessário para salvar o arquivo separado das turmas
import os                            # Necessário para verificar se o arquivo já existe

#-------------------------------------CONTROLE DE PERSISTÊNCIA DE DADOS COM JSON-----------------------------------
# Nome do arquivo separado (terceiro arquivo) onde as turmas dos professores ficam guardadas
ARQUIVO_AULAS = "aulas_academia.json"

def carregar_aulas():
    """Traz os professores e turmas salvos no arquivo de volta para o programa"""
    if os.path.exists(ARQUIVO_AULAS):
        with open(ARQUIVO_AULAS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []  # Se o arquivo não existir ainda, começa com uma lista vazia

def salvar_aulas(dados):
    """Grava as atualizações das turmas diretamente no arquivo separado JSON"""
    with open(ARQUIVO_AULAS, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
#----------------------------------------------------------------------------------------------------------------

print(f"Bem-vindos à Academia Campeões de Kanto:")
print(" "*90)
print("MISSÃO: Nossa missão é guiar a jornada de cada aluno rumo ao seu potencial máximo, transformando o esforço diário em evolução\n constante. Queremos despertar o verdadeiro mestre que existe em você,superando qualquer desafio dentro e fora do treino.")
print(" "*90)
print("VISÃO: Nossa visão é consolidar a Campeões de Kanto como o principal ginásio de referência em saúde e alta performance.Buscamos\n expandir nossa comunidade e formar uma liga de líderes imparáveis, prontos para alcançar o topo.")
print(" "*90)
print("VALORES: Nossos valores são a Evolução Contínua para ficar mais forte a cada dia e o Espírito de Treinador focado em disciplina. \nFortalecemos a União de Equipe no apoio mútuo e a Resiliência de Rocha para superar qualquer obstáculo.")

print("--"*90)

registros = []
aulas = carregar_aulas()  

while True:
    opcao = funcoes.validar_opcao("\nDigite a opção desejada:\n 1 - Acessar registros de alunos\n 2 - Acessar sistema da academia (Professores)\n 3 - Sair\n Escolha: ", [1, 2, 3])
    
    if opcao == 3:
        funcoes.sair()
        break
        
    elif opcao == 1:
        funcoes.acessar_registros()
#------------------------------------------------SISTEMA DA ACADEMIA------------------------------------------------------------------
    elif opcao == 2:
        print("--"*90)
        print("BEM-WINDO AO SISTEMA DA ACADEMIA!")
        print("--"*90)
        
        opcao_sistema = funcoes.validar_opcao("Digite a opção desejada:\n 1 - Adicionar professor(a)/aula\n 2 - Alterar professor(a)/aula\n 3 - Adicionar modalidade\n 4 - Alterar modalidades\n Escolha: ", [1, 2, 3, 4])
        
        if opcao_sistema == 1:
            professor = input("Digite o nome do professor: ")
            modalidade = input("Digite a modalidade: ")
            
            #Solicita os dois horários disponíveis do professor
            print(f"Defina os dois horários de treino para o Prof. {professor}:")
            horario1 = input("Digite o 1º Horário (ex: 08:00): ")
            horario2 = input("Digite o 2º Horário (ex: 19:00): ")

            aula1 = {
                "professor": professor,
                "modalidade": modalidade,
                "horário": horario1,
                "alunos_matriculados": 0 
            }
            aula2 = {
                "professor": professor,
                "modalidade": modalidade,
                "horário": horario2,
                "alunos_matriculados": 0 
            }
            
            aulas.append(aula1)
            aulas.append(aula2)
            salvar_aulas(aulas) # Grava as turmas no terceiro arquivo "aulas_academia.json"
            print(f"Prof. {professor} cadastrado com sucesso nos horários {horario1} e {horario2}!")

        elif opcao_sistema == 2:
            professor1 = input("Digite o nome do professor que deseja substituir: ")
            professor2 = input("Digite o nome do professor que entrará no lugar: ")
            
            professor_encontrado = False
            for aula in aulas:
                if aula["professor"] == professor1:
                    aula["professor"] = professor2
                    professor_encontrado = True
            
            if professor_encontrado:
                salvar_aulas(aulas) 
                print("Professor substituído com sucesso!")
            else:
                print("Professor não encontrado.")

        elif opcao_sistema == 3:
            professor = input("Digite o nome do professor da nova modalidade: ")
            horario = input("Digite o horário (ex: 14:30): ")
            modalidade = input("Digite a nova modalidade: ")
            aula = {
                "professor": professor,
                "horário": horario,
                "modalidade": modalidade,
                "alunos_matriculados": 0 
            }
            aulas.append(aula)
            salvar_aulas(aulas) 
            print("Nova modalidade cadastrada!")
            
        elif opcao_sistema == 4:
            modalidade1 = input("Digite a modalidade a ser substituída: ")
            modalidade2 = input("Digite a modalidade que entrará no lugar: ")
            
            modalidade_encontrada = False
            for aula in aulas:
                if aula["modalidade"] == modalidade1:
                    aula["modalidade"] = modalidade2
                    modalidade_encontrada = True
                    
            if modalidade_encontrada:
                salvar_aulas(aulas) 
                print("Modalidade substituída com sucesso!")
            else:
                print("Modalidade não encontrada.")
