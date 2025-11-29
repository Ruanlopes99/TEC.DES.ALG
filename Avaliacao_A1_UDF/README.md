**Sistema de Gestão de Eventos**

**Autor:** Ruan Lopes Dourado
**Disciplina:** Técnicas de Desenvolvimento de Algoritmos (Avaliação A1)
**Data:** 28/11/2025


## Sobre o Projeto
O **Sistema de Gestão de Eventos** é um sistema interativo desenvolvido em Python para auxiliar na organização de festas escolares. O objetivo foi aplicar os quatro pilares da programação aprendidos em aula (Condicionais, Repetição, Listas e Dicionários) em um cenário real e útil.

O sistema funciona através de um **Menu Principal**, onde o usuário pode navegar entre as funcionalidades sem precisar reiniciar o programa.


## Funcionalidades e Explicação Técnica

O projeto está dividido em 4 módulos principais, acessíveis pelo menu numérico:

### 1. Portaria (Verificação de Idade)
* **Conceito Técnico:** Estruturas Condicionais (`if`, `elif`, `else`).
* **Funcionamento:** O sistema pede a idade do convidado e define a cor da pulseira:
    * **+18 anos:** Pulseira Dourada (Acesso Total).
    * **+16 anos:** Pulseira Prata (Acesso com Responsável).
    * **-16 anos:** Entrada Negada.
* **Destaque:** Implementação de tratamento de erro (`try/except`) para garantir que o sistema não trave se o usuário digitar letras em vez de números.

### 2.Gerador de Rifas (Sorteio)
* **Conceito Técnico:** Estruturas de Repetição (`for`, `while`) e Operadores Matemáticos (`%`).
* **Funcionamento:** Para o sorteio de brindes, o sistema gera automaticamente uma sequência de números de 1 a 100, filtrando apenas os **números pares** (usando o operador de resto `% 2 == 0`).
* **Implementação:** O código demonstra o uso tanto do laço `for` (automático) quanto do `while` (manual com contador).

### 3.Lista VIP (Convidados)
* **Conceito Técnico:** Manipulação de Listas (`list` / `[]`).
* **Funcionamento:** Permite cadastrar nomes de convidados importantes.
* **Destaque:** Usa o método `.append()` para inserir nomes dinamicamente na lista e um laço `for` para exibir o relatório final de presença.

### 4.Consumação (Aniversariantes)
* **Conceito Técnico:** Dicionários (`dict` / `{}`).
* **Funcionamento:** Gerencia o crédito de consumação dos aniversariantes do mês.
* **Diferencial:** Diferente da lista simples, aqui utilizamos o conceito de **Chave e Valor**. O sistema associa o **Nome do Aniversariante** (Chave) ao **Valor em Reais** (Valor) que ele tem direito a gastar.
