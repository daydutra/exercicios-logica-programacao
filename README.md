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
