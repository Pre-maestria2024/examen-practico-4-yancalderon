# INF representar -infinito
INF = -float('inf')

def max_dolares(m, n, h, d):
    # dp[i][hp] representa la cantidad maxima de dolares que se pueden ganar
    # desde el alimento i en adelante con salud hp
    dp = [[INF] * (n + 1) for _ in range(m + 1)]
    
    # Caso base: cuando no hay mas alimentos (i == m)
    # Si hp == n, se puede ganar 0 (condicion alcanzada)
    # Si hp < n, no se cumple la condicion, asi que es -infinito
    for hp in range(n + 1):
        if hp == n:
            dp[m][hp] = 0
        else:
            dp[m][hp] = INF
    
    # Llenar la tabla DP desde el ultimo alimeto hacia el primero
    for i in range(m - 1, -1, -1):  # Desde m-1 hasta 0
        for hp in range(n + 1):  # Salud de 0 a n
            # 1: Vender el alimento f_i
            value1 = d[i] + dp[i + 1][hp]
            
            # 2: Comer el alimento f_i (solo si hp < n)
            value2 = INF
            if hp < n:
                new_hp = min(hp + h[i], n)  # Nueva salud despuess de comer
                value2 = dp[i + 1][new_hp]
            
            # Tomar el maximo entre vender y comer (si es posible)
            dp[i][hp] = max(value1, value2)
    
    # El resultado es dp[0][0], que representa la ganancia maxima
    # empezando con hp = 0 y considerando todos los alimentos
    result = dp[0][0]
    if result == INF:
        return 0  # No se puede alcanzar HN = n
    return result

def main():

	m, n = map(int, input().split())
	H = list(map(int, input().split()))
	D = list(map(int, input().split()))

	print(max_dolares(m, n, H, D))

if __name__ == '__main__':
	main()