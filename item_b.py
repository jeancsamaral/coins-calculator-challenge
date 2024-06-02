import concurrent.futures
from coins_calculator import calculate_coins

def calculate_expected_coins(x, y, list_of_notes):
    current_notes = list_of_notes + [x, y]
    total_coins = 0
    for amount in range(1, 100):
        total_coins += calculate_coins(sorted(current_notes, reverse=False), amount)
    expected_coins = total_coins / 100
    return expected_coins, x, y

def item_b():
    # Lista de moedas disponíveis inicialmente
    list_of_notes = [1, 5, 10, 25, 50, 100]

    min_expected_coins = float('inf')
    optimal_x = 1
    optimal_y = 1

    futures = []
    # Realiza o testes para todas as duplas
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for x in range(1, 100):
            for y in range(x, 100):
                futures.append(executor.submit(calculate_expected_coins, x, y, list_of_notes))

        for future in concurrent.futures.as_completed(futures):
            expected_coins, x, y = future.result()
            if expected_coins < min_expected_coins:
                min_expected_coins = expected_coins
                optimal_x = x
                optimal_y = y

    print(f"O valor otimo para x foi de {optimal_x} e o valor otimo para y foi de {optimal_y}, o qual reduz o numero esperado de moedas na soma para {min_expected_coins:.2f}.")

if __name__ == '__main__':
    item_b()
