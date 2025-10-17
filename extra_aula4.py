#O programa será um pequeno sistema de gerenciamento de estoque para uma loja, onde o usuário pode adicionar produtos, atualizar a quantidade em estoque e calcular o valor total do estoque.
# Sistema de Gestão de Stock Simplificado

# Solicitação dos dados do item 1
print("Insira os dados do item 1")
nome1 = input("Nome do item 1: ")
preco1 = float(input("Preço do item 1 (em euros): "))
quantidade1 = int(input("Quantidade do item 1: "))

# Solicitação dos dados do item 2
print("\nInsira os dados do item 2")
nome2 = input("Nome do item 2: ")
preco2 = float(input("Preço do item 2 (em euros): "))
quantidade2 = int(input("Quantidade do item 2: "))

# Solicitação dos dados do item 3
print("\nInsira os dados do item 3")
nome3 = input("Nome do item 3: ")
preco3 = float(input("Preço do item 3 (em euros): "))
quantidade3 = int(input("Quantidade do item 3: "))

# Cálculo do valor total do stock para cada item
valor_total1 = preco1 * quantidade1
valor_total2 = preco2 * quantidade2
valor_total3 = preco3 * quantidade3

# Cálculo do valor total do stock
valor_total_stock = valor_total1 + valor_total2 + valor_total3

# Exibição dos resultados
print("\nResumo do Stock:")
print("Item 1: " + nome1 + " | Preço: €" + str(preco1) + " | Quantidade: " + str(quantidade1) + " | Valor Total: €" + str(valor_total1))
print("Item 2: " + nome2 + " | Preço: €" + str(preco2) + " | Quantidade: " + str(quantidade2) + " | Valor Total: €" + str(valor_total2))
print("Item 3: " + nome3 + " | Preço: €" + str(preco3) + " | Quantidade: " + str(quantidade3) + " | Valor Total: €" + str(valor_total3))

print("\nValor Total do Stock: €" + str(valor_total_stock))



