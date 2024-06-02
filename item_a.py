from coins_calculator import calculate_coins

# Função que calcula o número esperado de moedas
def calculate_min_expected_coins(coin_set):
    total_coins = 0
    for amount in range(1, 100):
        total_coins += calculate_coins(sorted(coin_set), amount)
    return total_coins / 100

def item_a():
    # Lista de moedas disponíveis inicialmente
    list_of_notes = [1, 5, 10, 25, 50, 100]

    # Realização do teste para diferentes valores de x
    min_expected_coins = float('inf')
    optimal_x = 1

    # Teste para x variando de 1 a 100
    for x in range(1, 100):
        current_notes = list_of_notes + [x]

        expected_coins = calculate_min_expected_coins(current_notes)

        if expected_coins < min_expected_coins:
            min_expected_coins = expected_coins
            optimal_x = x

    print(f"O valor otimo para x e {optimal_x}, o qual reduz o numero esperado de moedas na soma para {min_expected_coins:.2f}.")

if __name__ == '__main__':
    item_a()
