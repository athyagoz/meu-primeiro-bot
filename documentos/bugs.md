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

## Bug 03: Ausência de Botão de Ações (Editar/Excluir)
- **Severidade:** Alta (Impede a gestão dos dados)
- **Local:** Listagem de Funcionários / Cards

### Comportamento Esperado:
Cada registro de funcionário deve apresentar um menu (geralmente representado por três pontinhos "...") que permita abrir as opções de "Editar" e "Excluir".

### Comportamento Atual:
O card do funcionário exibe apenas o Nome, CPF e um toggle de "Etapa concluída". Não há botões ou ícones para acessar as funções de edição ou exclusão.


## Bug 04: Botões do Menu Lateral Inativos
- **Severidade:** Média (Impede a navegação entre módulos)
- **Local:** Menu Lateral Esquerdo (Sidebar)

### Comportamento Esperado:
Ao clicar nos ícones do menu lateral (Dashboard, Configurações, etc.), o usuário deve ser redirecionado para uma tela com a mensagem "Em breve".

### Comportamento Atual:
Os ícones são clicáveis visualmente (o cursor muda), mas nenhuma ação ocorre. O sistema permanece na mesma tela e não redireciona o usuário.
