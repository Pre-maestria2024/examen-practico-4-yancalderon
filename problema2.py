from collections import defaultdict

def max_groups(n, k, edges):
    if n == 0 or k == 0:
        return 0
    
    # Construir el árbol como un grafo dirigido
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
    
    groups = 0
    
    def dfs(node):
        nonlocal groups
        count = 1  # Contamos el nodo actual
        for child in tree[node]:
            count += dfs(child)  # Acumulamos los nodos del subárbol
        
        # Contamos cuántos grupos de tamaño k podemos formar
        groups += count // k
        return count % k  # Retornamos los nodos restantes que no formaron un grupo
    
    dfs(0)  # La raíz es 0
    return groups

def main():

    n, k = map(int, input().split())
    edges = []

    for i in range(n-1):
        u,v = map(int,input().split())
        edges.append((u,v))

    print(max_groups(n, k, edges))


if __name__  == '__main__':
    main()
