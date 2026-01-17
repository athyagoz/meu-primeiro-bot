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
