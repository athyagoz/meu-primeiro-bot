# Estratégia de Automação de Testes

Para este desafio, planejei a automação de duas funcionalidades críticas usando **Python + Selenium**:

## 1. Automação do Cadastro de Funcionários
- **Objetivo:** Garantir que o formulário de cadastro seja preenchido e enviado sem erros manuais.
- **Lógica:**
    1. Acessar a URL do sistema.
    2. Localizar o elemento do botão "Adicionar" via XPath.
    3. Comandar o navegador para digitar dados válidos nos campos de Nome e CPF.
    4. Acionar o evento de clique no botão "Salvar".

## 2. Automação da Validação de Campos (Fluxo Negativo)
- **Objetivo:** Validar se o sistema bloqueia o envio de formulários vazios.
- **Lógica:**
    1. Abrir o modal de cadastro.
    2. Clicar em "Salvar" sem preencher nenhum dado.
    3. Verificar se o elemento de alerta (texto em vermelho) aparece na tela.
