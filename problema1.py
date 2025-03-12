import sys

# Establecer un valor muy negativo para representar -infinito
INF = -float('inf')

def max_dollars(m, n, h, d):
    # dp[i][hp] representa la cantidad máxima de dólares que se pueden ganar
    # desde el alimento i en adelante con salud hp
    dp = [[INF] * (n + 1) for _ in range(m + 1)]
    
    # Caso base: cuando no hay más alimentos (i == m)
    # Si hp == n, se puede ganar 0 (condición alcanzada)
    # Si hp < n, no se cumple la condición, así que es -infinito
    for hp in range(n + 1):
        if hp == n:
            dp[m][hp] = 0
        else:
            dp[m][hp] = INF
    
    # Llenar la tabla DP desde el último alimento hacia el primero
    for i in range(m - 1, -1, -1):  # Desde m-1 hasta 0
        for hp in range(n + 1):  # Salud de 0 a n
            # Opción 1: Vender el alimento f_i
            value1 = d[i] + dp[i + 1][hp]
            
            # Opción 2: Comer el alimento f_i (solo si hp < n)
            value2 = INF
            if hp < n:
                new_hp = min(hp + h[i], n)  # Nueva salud después de comer
                value2 = dp[i + 1][new_hp]
            
            # Tomar el máximo entre vender y comer (si es posible)
            dp[i][hp] = max(value1, value2)
    
    # El resultado es dp[0][0], que representa la ganancia máxima
    # empezando con hp = 0 y considerando todos los alimentos
    result = dp[0][0]
    if result == INF:
        return 0  # No se puede alcanzar HN = n
    return result



def main():

	m, n = map(int, input().split())
	H = list(map(int, input().split()))
	D = list(map(int, input().split()))

	print(max_dollars(m, n, H, D))

if __name__ == '__main__':
	main()