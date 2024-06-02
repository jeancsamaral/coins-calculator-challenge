# Função que calcula o número de moedas para um determinado valor total
# Abordagem utilizando programação dinâmica
def calculate_coins(notes, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in notes:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount]
