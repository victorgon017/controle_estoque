estoque = [
    ["Teclado", 0, 120.00],
    ["Mouse", 0, 80.00],
    ["Monitor", 0, 950.00]
]

for produto in estoque:
    produto[1] = int(input(f"Digite o estoque de {produto[0]}: "))

for produto in estoque:
    if produto[1] < 5:
        print(f"Atenção: estoque baixo para o produto {produto[0]}")