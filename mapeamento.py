"""
Map - recebendo uma função e passando por cada elemento de uma lista
"""
produtos = [
    {'Nome': 'p1', 'preco': 50},
    {'Nome': 'p2', 'preco': 13},
    {'Nome': 'p3', 'preco': 50.55},
    {'Nome': 'p4', 'preco': 22},
    {'Nome': 'p5', 'preco': 100},
    {'Nome': 'p6', 'preco': 10.50},
    {'Nome': 'p7', 'preco': 15},
    {'Nome': 'p8', 'preco': 6},
    {'Nome': 'p9', 'preco': 0.49},
    {'Nome': 'p10', 'preco': 1},
]

pessoas = [
    {'nome': 'Everton', 'idade': 22},
    {'nome': 'Luiz', 'idade': 50},
    {'nome': 'Anna', 'idade': 20},
    {'nome': 'Jessica', 'idade': 12},
    {'nome': 'Eduardo', 'idade': 10},
    {'nome': 'Maria', 'idade': 5},
    {'nome': 'Lucas', 'idade': 60},
    {'nome': 'Julia', 'idade': 85},
    {'nome': 'Mario', 'idade': 17},
]


# Criando a função que map receberá
def aumentar(p):  # Aqui eu volto o dicionario inteiro
    p['idade'] = round(p['idade'] * 1.20)  # Aumanto em 20%
    return p


nomes = map(aumentar, pessoas)
for pessoa in nomes:
    print(pessoa)

# map recebendo função anonima
novo_preco = map(lambda p: f"R$ {p['preco'] * 1.05:.2f}".replace('.', ','), produtos)
for preco in novo_preco:
    print(preco)

print()
