# Projeto de QA: Teste de Gestão de Funcionários

Este repositório contém o desafio técnico de Analista de Teste/QA. O objetivo foi validar as funcionalidades de um sistema de gestão de funcionários, identificar bugs de interface e lógica, e planejar a automação dos processos.

## Tecnologias Utilizadas
- **Documentação:** Markdown (GitHub)
- **Linguagem:** Python
- **Ferramenta de Automação:** Selenium WebDriver (Planejamento)
- **Gestão de Código:** Git & GitHub

## Estrutura do Projeto
- **`/documentos`**: Contém o Plano de Teste, o Relatório de Bugs detalhado e a Estratégia de Automação.
- **`/codigo`**: Scripts em Python que demonstram a lógica de validação automatizada.

## Resumo dos Testes Realizados
Durante a execução do projeto, foram realizados:
1. **Testes de UI (Interface):** Comparação do site com o protótipo (Identificado erro de repetição de itens no menu).
2. **Testes Funcionais:** Verificação do fluxo de criação, edição e exclusão.
3. **Testes de Validação:** Teste de campos obrigatórios e formato de dados (CPF).
4. **Testes de Navegação:** Verificação da integridade dos links do menu lateral.

## Principais Bugs Encontrados
Foram identificados 4 bugs principais, sendo os mais críticos:
- Dados que desaparecem ao tentar salvar um novo funcionário.
- Ausência de botões para Editar e Excluir registros.
- Links do menu lateral inativos.

---
## Como visualizar os resultados
1. Acesse a pasta `documentos` para ler o **[Relatório de Bugs](documentos/bugs.md)**.
2. Acesse o **[Plano de Teste](documentos/plano-de-teste.md)** para entender a metodologia aplicada.
3. Veja o arquivo **[validador_menu.py](codigo/validador_menu.py)** para entender a lógica de automação proposta.

---
**Desenvolvido por Alyson Thyago** 
