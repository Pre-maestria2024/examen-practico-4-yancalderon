from collections import defaultdict

def max_groups(n, k, edges):
    if k == 0 or n == 0:
        return 0

    # Construimos el árbol con listas de adyacencia
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    # Contador global de grupos formados
    total_groups = 0

    # DFS para contar grupos de `k` nodos
    def dfs(node, parent):
        nonlocal total_groups
        subtree_size = 1  # Contamos el nodo actual

        for neighbor in tree[node]:
            if neighbor == parent:
                continue
            size = dfs(neighbor, node)
            subtree_size += size

        # Formamos tantos grupos de `k` como sea posible con los nodos en este subárbol
        groups_formed = subtree_size // k
        total_groups += groups_formed

        # Retornamos los nodos restantes que no se pudieron agrupar aún
        return subtree_size % k

    dfs(0, -1)  # Iniciamos DFS desde la raíz (nodo 0)

    return total_groups

# Entrada de prueba
n, k = 34, 3
edges = [
    (0, 1), (1, 2), (2, 3), (3, 4), (4, 5),
    (2, 6), (6, 7), (0, 8), (8, 9), (9, 10),
    (10, 11), (11, 12), (12, 13), (12, 14),
    (8, 15), (15, 16), (16, 17), (17, 18),
    (15, 19), (19, 20), (20, 21), (20, 22),
    (20, 23), (21, 24), (21, 25), (21, 26),
    (8, 27), (27, 28), (28, 29), (28, 30),
    (29, 31), (31, 32), (31, 33)
]

# Salida esperada: 8
print(max_groups(n, k, edges))
