# 📂 Exercícios de Lógica de Programação

Este repositório contém a resolução dos exercícios práticos passados pelo professor na matéria de Lógica de Programação, no curso Técnico em Informática do IF Sudeste MG.

## 🛠️ Tecnologias utilizadas
- **Linguagem:** Python 🐍
- **Editor de Código:** Visual Studio Code (VS Code) 💻
- **Controle de Versão:** Git e GitHub 🚀

## 📑 Exercício: Sistema de Triagem do Centro de Resgate Ambiental

**Enunciado:**
>A ONG "EcoVida" atende chamados de resgate de animais em uma reserva biológica e conta com apenas 3 veterinários plantonistas: Dr. Carlos, Dra. Amanda e o coordenador-chefe Dr. Renato. Como a equipe é reduzida, eles não conseguem atender todos os chamados ao mesmo tempo. Você foi contratada para criar um sistema de triagem em Python para equilibrar a divisão de tarefas entre eles.
>
>Regras de Negócio e Requisitos:
>
>Tipos de Chamados: Cada ocorrência registrada possui um código numérico para o tipo de animal:
>
>   1 – Ave
>
>   2 – Réptil
>
>   3 – Pequeno Mamífero
>
>   4 – Onça-Parda
>
>Níveis de Urgência: Toda ocorrência deve ter um nível de gravidade: Baixo, Médio ou Alto.
>
>Regra Especial da Onça-Parda: Toda ocorrência do tipo 4 (Onça-Parda) tem, obrigatoriamente, nível de gravidade Alto e deve ser atribuída sempre ao coordenador-chefe, Dr. Renato.
>
>Distribuição Equilibrada: Qualquer outra ocorrência (tipos 1, 2 ou 3) deve ser atribuída automaticamente ao veterinário que tiver menos ocorrências acumuladas até aquele momento.
>
>Funcionamento do Sistema e Saídas:
>
>A cada novo registro: O sistema deve ler os dados da ocorrência e, logo em seguida, imprimir na tela a quantidade atual de chamados de cada um dos 3 veterinários (para acompanhar o equilíbrio).
>
>Encerramento: A entrada de dados deve continuar acontecendo dentro de um laço de repetição. O programa só deve parar quando o usuário digitar um código de tipo de animal diferente de 1, 2, 3 ou 4.
>
>Relatório Final: Assim que o programa for encerrado, ele deve exibir:
>
>O total de ocorrências registradas para cada um dos 4 tipos de animais.
>
>O total acumulado de cada nível de gravidade (quantas foram Baixo, quantas Médio e quantas Alto).

## 💡 Conceitos praticados:
- **Boas Práticas de Programação (Constantes):** Eliminação de "números mágicos" através da definição de constantes em maiúsculo (`CODIGO_AVE`, `CODIGO_URGENCIA_ALTO`), melhorando a legibilidade e manutenção do código.
- **Entrada e Saída de Dados:** Uso de `input()` e formatação avançada de strings com `f-strings` para exibição de menus e relatórios claros.
- **Variáveis e Acumuladores:** Criação de variáveis de controle para contagem e consolidação de dados estatísticos.
- **Estruturas Condicionais Aninhadas:** Aplicação eficiente de `if`, `elif` e `else` para tomada de decisões baseadas nas regras de negócio da ONG.
- **Estruturas de Repetição (Laços):** Uso de loops `while` para gerenciar o fluxo principal do sistema e garantir a validação rigorosa de dados de entrada.
- **Lógica de Distribuição e Balanceamento:** Algoritmo de comparação para identificar o menor valor acumulado e realizar o balanceamento de tarefas entre os veterinários plantonistas.

---

## 📑 Exercício: Sistema de Orçamento de Planos de Saúde

**Enunciado:**
>A plataforma "LifeCompare" é um sistema web que ajuda usuários a simular e comparar o valor de planos de saúde de duas grandes operadoras parceiras: VITA Saúde e OMEGA Seguros. Você foi contratada para desenvolver o motor de cálculo desse sistema em Python.
>
>Dados de Entrada Esperados por Cliente:
>(O sistema deve ser capaz de processar vários clientes em um laço de repetição)
>
>Sexo: (1 – Feminino, 2 – Masculino; qualquer outro valor encerra o programa).
>
>Idade: (Deve estar entre 18 e 80 anos; caso contrário, o programa deve exibir uma mensagem de erro e exigir que o usuário digite uma idade válida antes de continuar).
>
>Renda Mensal do Cliente: (Mínimo de R$ 2.000,00; caso seja menor, exibir erro e pedir para digitar novamente).
>
>Anos de Contribuição: Tempo em anos que o cliente já possui outra apólice com a plataforma (valor inteiro >= 0).
>
>Histórico de Internações: Número de internações hospitalares nos últimos 3 anos (valor inteiro >= 0).
>
>Detalhamento das Regras de Negócio
>VITA SAÚDE:
>Valor Base: 10% da renda mensal do cliente.
>
>Ajuste por Idade (Atenção aos Limites!):
>Menor que 30 anos: acréscimo de 2% por ano abaixo dos 30 anos, até um máximo de 16% de acréscimo. (Se o cálculo ultrapassar 16%, o programa deve limitar o acréscimo em 16%).
>
>Maior que 50 anos: desconto de 1% por ano acima dos 50 anos, até o limite de 15% de desconto. (Se o cálculo ultrapassar 15%, o programa deve limitar o desconto em 15%).
>
>Anos de Contribuição (Fidelidade):
>Clientes com mais de 3 anos de contribuição recebem 5% de desconto no valor final do plano.
>
>Histórico de Internações:
>Se o cliente tiver mais de 2 internações, aplica-se um acréscimo de 20% sobre o valor do plano (aplicado após os descontos e acréscimos anteriores).
>
>OMEGA SEGUROS:
>Valor Base: 12% da renda mensal do cliente.
>
>Descontos Acumulados (aplicados juntos diretamente sobre o Valor Base):
>Sexo Feminino: 5% de desconto.
>
>Idade >= 30 anos: desconto adicional de 10%.
>
>Fidelidade: 3% de desconto por ano de contribuição do cliente, até no máximo 15% de desconto.
>
>Nota: Todos os descontos acima da OMEGA são somados e aplicados de uma vez sobre o valor base.
>
>Histórico de Internações:
>0 internações: bônus (desconto) de 10% aplicado sobre o valor final do plano.
>
>1 ou 2 internações: valor normal (sem bônus e sem penalidade).
>
>3 ou mais internações: o cliente torna-se inelegível para contratar a OMEGA Seguros.
>
>Funcionamento do Sistema e Saídas:
>Para cada cliente processado:
>Exibir o valor final do plano calculado para a VITA Saúde.
>
>Exibir o valor final do plano para a OMEGA Seguros (ou exibir a mensagem "INELEGÍVEL", caso ele tenha 3 ou mais internações).
>
>Relatório Final (Exibido assim que um código de sexo inválido for digitado):
>Número total de clientes processados com sucesso;
>
>Quantidade de clientes que foram considerados inelegíveis na OMEGA Seguros;
>
>Média dos valores dos planos por operadora (calculando a média da OMEGA apenas entre os clientes que foram elegíveis);
>
>O maior e o menor valor de plano registrado para cada uma das duas operadoras (desconsiderando os valores de quem foi inelegível na OMEGA).

### 💡 Conceitos praticados:
- **Modularização (Funções):** Criação de funções personalizadas com `def` para isolar as regras de negócio de cada operadora.
- **Retorno Múltiplo de Dados:** Funções retornando mais de uma informação simultaneamente (`valor` e `status de elegibilidade`).
- **Lógica Estatística Avançada:** Controle de fluxo para descobrir médias, maiores e menores valores de forma independente para cada empresa, tratando exceções (clientes inelegíveis).  

---

## 📑 Exercício: Análise e Classificação de Triângulos

**Enunciado:**
>Um triângulo é uma figura geométrica plana formada por três segmentos de reta (a, b, c). Para que três valores formem um triângulo válido, é **obrigatório** que a medida de qualquer um dos lados seja estritamente menor que a soma das medidas dos outros dois.
>
>### Classificação dos Triângulos:
>- **Equilátero:** Todos os 3 lados são iguais.
>- **Isósceles:** Apenas 2 lados são iguais.
>- **Escaleno:** Todos os 3 lados são diferentes.
>
>## 🎯 Objetivo
>
>Desenvolva um programa na linguagem **Python** que leia sucessivamente conjuntos de três valores numéricos (a, b, c) representando os lados de um triângulo. 
>
>O programa deve continuar lendo entradas até que o usuário informe um conjunto de três valores que **não formem um triângulo** (condição de parada).
>
>Ao final da execução (quando a condição de parada for atingida), o programa deve calcular e exibir:
>
>1. **a)** O **menor perímetro** entre os triângulos do tipo **escaleno**.
>2. **b)** A **maior** e a **menor área** entre os triângulos do tipo **equilátero**.
>3. **c)** A **quantidade total** de triângulos do tipo **isósceles**.
>4. **d)** A **média dos perímetros** de todos os triângulos válidos lidos.
>5. **e)** A **soma das áreas** de todos os triângulos válidos lidos.
>
>⚠️ **Atenção:** O término da entrada de dados é identificado no momento em que os três valores (a, b, c) **não** formarem um triângulo. Esse triângulo inválido não entra nos cálculos das estatísticas.

---

## 💡 Conceitos praticados:
- **Modularização e Funções:** Criação de função personalizada (`calcula_triangulo`) com retorno de múltiplos valores e documentação via *docstrings*.
- **Estruturas de Decisão:** Aplicação de `if`, `elif` e `else` para classificação geométrica (triângulos equiláteros, escalenos e isósceles) e prevenção de redundâncias lógicas.
- **Estruturas de Repetição:** Utilização de laços `while` para validação de dados de entrada e controle de fluxo do programa.
- **Validação de Dados:** Garantia de integridade de dados (verificando se os lados formam um triângulo válido e impedindo valores menores ou iguais a zero).
- **Módulos Nativos:** Uso da biblioteca `math` (`math.sqrt`) para operações matemáticas.
- **Acumuladores e Sinalizadores (*Flags*):** Manipulação de variáveis para cálculo de totais, somatórias, médias, maiores e menores valores (usando `None` para inicialização segura).
- **Formatação de Saída:** Uso de *f-strings* com formatação de casas decimais (`:.1f`) para exibição clara de dados.
