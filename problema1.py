def max_dollars_corrected(m, n, h, d):
    # Initialize the dp array with 0
    dp = [0] * (n + 1)

    # Process each food item
    for i in range(m):
        # Update the dp array in reverse order to avoid overwriting
        for j in range(n, -1, -1):
            # Calculate the new health after eating the food
            new_health = min(j + h[i], n)
            # Update the dp value for the new health
            dp[new_health] = max(dp[new_health], dp[j] + (d[i] if new_health == n else 0))

    # The result is the maximum dollars when health is fully restored
    return dp[n]

def main():

	m, n = map(int, input().split())
	h = list(map(int, input().split()))
	d = list(map(int, input().split()))

	print(max_dollars_corrected(m, n, h, d))

if __name__ == "__main__":
    main()
