def max_dollars(m, n, h, d):
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(n + 1):
            # Mantener la mejor opción anterior
            dp[i][j] = dp[i - 1][j]

            # Si se consume el alimento i
            new_health = min(j + h[i - 1], n)
            dp[i][new_health] = max(dp[i][new_health], dp[i - 1][j])

            # Si se vende el alimento i (solo si ya estamos en n)
            if j == n:
                dp[i][j] = max(dp[i][j], dp[i - 1][j] + d[i - 1])

    return dp[m][n]

def main():

	m, n = map(int, input().split())
	H = list(map(int, input().split()))
	D = list(map(int, input().split()))

	print(max_dollars(m, n, H, D))

if __name__ == "__main__":
    main()
