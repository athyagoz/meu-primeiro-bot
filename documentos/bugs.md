# Relatório de Bugs de Interface (UI)

## Bug 01: Itens do Menu Superior Repetidos
- **Severidade:** Baixa (Visual/Conteúdo)
- **Local:** Cabeçalho (Header)

### Comportamento Esperado (Protótipo)
Os itens de navegação no topo devem estar numerados sequencialmente para facilitar a identificação: 
- Item 1
- Item 2
- Item 3

### Comportamento Atual (Site)
Todos os itens do menu exibem o texto estático "ITEM 1" repetidamente.

---
### Notas de Automação
Verificar se o loop de renderização no código está utilizando uma variável dinâmica ou apenas uma string fixa.


## Bug 02: Falha ao Salvar Novo Funcionário
- **Severidade:** Alta (Impede o uso principal do sistema)
- **Local:** Modal "Adicionar Funcionário"

### Passo a Passo para Reproduzir:
1. Clique em "+ Adicionar Funcionário".
2. Preencha Nome e CPF corretamente.
3. Clique no botão "Salvar".

### Comportamento Esperado:
O formulário deve fechar e o novo funcionário deve aparecer na tabela principal.

### Comportamento Atual:
Os dados desaparecem dos campos de preenchimento, o formulário não fecha e o funcionário **não é adicionado** à lista.


## Testes de Validação (Passo 3 - Fluxo Negativo)
- **Cenário:** Tentar salvar com campos vazios ou CPF inválido.
- **Resultado:** **PASSOU**.
- **Observações:** O sistema exibiu corretamente as mensagens de erro em vermelho para o campo "Nome" e barrou CPFs incompletos, impedindo o envio de dados inválidos.
