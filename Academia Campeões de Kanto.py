print("Bem vindos a Academia Campeões de Kanto")
print(" "*90)
print("MISSÃO: Nossa missão é guiar a jornada de cada aluno rumo ao seu potencial máximo, transformando o esforço diário em evolução\n constante. Queremos despertar o verdadeiro mestre que existe em você,superando qualquer desafio dentro e fora do treino.")
print(" "*90)
print("VISÃO: Nossa visão é consolidar a Campeões de Kanto como o principal ginásio de referência em saúde e alta performance.Buscamos\n expandir nossa comunidade e formar uma liga de líderes imparáveis, prontos para alcançar o topo.")
print(" "*90)
print("VALORES: Nossos valores são a Evolução Contínua para ficar mais forte a cada dia e o Espírito de Treinador focado em disciplina. \nFortalecemos a União de Equipe no apoio mútuo e a Resiliência de Rocha para superar qualquer obstáculo.")

print("--"*90)

registros=[]
opcao=int(input("Digite a opção desejada:\n 1- Acessar registros\n 2 - Acessar sistema da academia\n 3- sair\n "))
while opcao !=3:
    if opcao == 1:
        opcao2=int(input("1 - Realizar novo registro\n 2 - Acessar registro já cadastrado\n"))
        if opcao2 == 1:
            nome=input("Digite seu nome completo: ")
            peso=float(input("Digite o seu peso atual *em gramas:"))
            altura=float(input("Digite a sua altura *em centímetros"))
            idade=int(input("Digite a sua idade: "))

            registro= {
            "nome":nome,
            "peso": peso,
            "altura":altura,
            "idade":idade,
    }

            registros.append(f"{registro}")
            print(registros)

            opcao3=int(input("Digite a opção desejada: \n 1-  Acessar planos/modalidades e horários\n 2 - voltar\n"))
            if opcao3==1:
                print("Conheça nossos planos:")
                opcao_planos=int(input("1 - Plano Caverna Diglet (básico) R$:100,00:\n Inclui equipamentos de uso diário, uso do espaço para lanches e local para banhos.\n\n 2 - Plano Área da elite (premium) R$: 200,00:\n Inclui sauna privativa;\n acompanhamento com nutricionista;\n personal trainner especializado;\n e brindes personalizados da nossa academia.\n\n**Esses valores não incluem as modalidades escolhidas a parte** "))
                opcao_modalidades=int(input("Para deixar o nosso serviço ainda mais completo temos as modalidades que ficam a escolha do cliente, quantas quiser!\n 1 - Crossfit"))