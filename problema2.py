def spooky_brook_solution(n, k, edges):
    if k == 0:
        return 0
    
    # Construir el árbol (grafo dirigido desde la raíz)
    tree = [[] for _ in range(n)]
    for u, v in edges:
        tree[u].append(v)
    
    memo = {}
    
    def dp(node, remaining):
        if (node, remaining) in memo:
            return memo[(node, remaining)]
        
        if not tree[node]:
            if remaining == 1:
                return 1
            return 0
        
        # Inicializar resultado
        result = 0
        
        # Opción 1: Incluir este nodo en el grupo actual
        if remaining == 1:
            # Sumamos 1 (por el grupo completado) y exploramos comenzar nuevos grupos en cada hijo
            result = 1 + sum(dp(child, k) for child in tree[node])
        else:
            for child in tree[node]:
                continue_with_child = dp(child, remaining - 1)
                
                others = sum(dp(other, k) for other in tree[node] if other != child)
                
                # Actualizamos el resultado si encontramos una mejor combinación
                result = max(result, continue_with_child + others)
        
        # Opción 2: No incluir este nodo en ningún grupo (empezar desde los hijos)
        skip_result = sum(dp(child, k) for child in tree[node])
        result = max(result, skip_result)
        
        memo[(node, remaining)] = result
        return result
    
    return dp(0, k)

def main():

    n, k = map(int, input().split())

    edges = []
    for i in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    result = spooky_brook_solution(n, k, edges)
    
    print(result)

if __name__ == '__main__':
    main()