# Lista que representa o que o robô encontrou no site
itens_no_site = ["ITEM 1", "ITEM 1", "ITEM 1"]

print("--- Iniciando Teste de Interface ---")

# O robô verifica se todos os itens são iguais (o que seria um erro)
if len(set(itens_no_site)) == 1:
    print("ERRO ENCONTRADO: O menu exibe itens repetidos!")
else:
    print("SUCESSO: O menu está variado conforme o esperado.")

print("--- Teste Finalizado ---")
