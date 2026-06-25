# 🏋️ Trabalho Final — Sistema de Gestão de Academia

**Instituto Federal de Educação, Ciência e Tecnologia do Piauí — IFPI / Campus Corrente**

**Disciplina:** Algoritmos e Lógica de Programação

**Curso:** Análise e Desenvolvimento de Sistemas (ADS)

---

## 🎯 Objetivo

Desenvolver um **sistema de gestão** completo, aplicando os conceitos estudados ao longo da disciplina: variáveis e tipos de dados, estruturas de decisão e repetição, listas e dicionários, funções, validação de dados e organização do código.

O sistema deverá ser implementado atendendo aos requisitos descritos para o tema escolhido (Sistema de Academia), além dos **requisitos mínimos comuns** a todos os projetos.

---

## 📋 Orientações Gerais

- **Equipes:** Individual *(você e Deus)*.
- **Tema:** Sistema de Academia.
- **Linguagem:** Python 3.
- **Entrega:** repositório/pasta com o código-fonte + este README preenchido.
- **Apresentação:** demonstração do sistema funcionando + explicação do código.
- **Prazo de entrega:** `15/07/2026`

---

## ✅ Requisitos Mínimos (comuns a todos os temas)

O sistema **deve** conter:

1. **Menu principal** com navegação (laço de repetição até o usuário escolher sair).
2. **Cadastro completo (CRUD)** das principais entidades:
   - **C**riar (incluir novo registro)
   - **R**ecuperar (listar / consultar)
   - **U**pdate (alterar dados de um registro)
   - **D**elete (remover registro)
3. **Pelo menos 4 entidades** relacionadas entre si.
4. **Validação de dados de entrada** (não aceitar valores inválidos, campos vazios, opção inexistente no menu etc.).
5. **Regras de negócio** específicas do tema (cálculos, multas, descontos, verificação de disponibilidade etc.).
6. **Manipulação de datas/horas** quando o tema exigir (uso do módulo `datetime`).
7. **Pelo menos 2 relatórios/consultas** com filtro (ex.: listar todos os registros de um período, calcular um total etc.).
8. **Uso de funções** para organizar o código (evitar todo o programa em um único bloco).

### ⭐ Diferenciais (pontuação extra)
- Persistência de dados em arquivo (`.json`, `.csv` ou `.txt`).
- Tratamento de exceções (`try / except`).
- Interface organizada e amigável no terminal.
- Código comentado e bem identado.

---

## 🗂️ Tema Escolhido

### 🏋️ Sistema de Academia

A academia oferece diferentes **planos** (mensal, trimestral e anual), além de diversas **modalidades/aulas**, ministradas por instrutores em horários determinados. Eventualmente uma modalidade é suspensa ou um instrutor é afastado, e novos planos e modalidades são criados — sendo necessário manter o cadastro de planos, modalidades e instrutores sempre atualizado.

Os clientes procuram a academia para se matricular. Primeiro é necessário cadastrá-los, registrando dados pessoais e (quando houver) a avaliação física. Depois, o aluno escolhe o plano e as modalidades — **a mensalidade varia conforme o plano, a quantidade de modalidades e o horário (comercial/reduzido)**. Na matrícula, registra-se a data de adesão e calcula-se a **data de vencimento** conforme o plano.

A cada acesso do aluno, registra-se data/hora de entrada e verifica-se a situação do pagamento. Se a mensalidade estiver **vencida**, o acesso é bloqueado e a inadimplência é sinalizada. Na **renovação**, recalcula-se o vencimento; no **cancelamento** antes do fim do período, aplicam-se as regras de rescisão (cobrança ou devolução proporcional).

---

## 📊 Critérios de Avaliação

| Critério | Descrição | Pontos |
|---|---|---|
| Funcionamento do menu e CRUD | Menu navegável e cadastro completo das entidades | 2,0 |
| Regras de negócio | Cálculos, multas, descontos e verificações corretas | 2,5 |
| Validação de dados | Tratamento de entradas inválidas | 1,5 |
| Relatórios/consultas | Consultas com filtro funcionando | 1,5 |
| Organização do código | Uso de funções, identação e clareza | 1,5 |
| Apresentação | Demonstração e domínio do código pela aluna | 1,0 |
| **Total** | | **10,0** |

---

## 👥 Identificação do Aluno

| Nome | Sistema |
|---|---|
| Maria Luiza Alves Vieira | 6 — Academia |

---

## 🚀 Como Executar

```bash
python main.py
