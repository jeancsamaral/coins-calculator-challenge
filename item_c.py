from coins_calculator import calculate_coins
import concurrent.futures
from itertools import combinations

def calculate_min_expected_coins(coin_set):
    total_coins = 0
    for amount in range(1, 100):
        total_coins += calculate_coins(sorted(coin_set), amount)
    return total_coins / 100

def process_combination(combination):
    expected_coins = calculate_min_expected_coins(combination)
    return expected_coins, combination

def process_inner_combination(x, y, z, w, best_combination):
    current_notes = [best_combination[0]] + [x, y, z, w]
    total_coins = 0
    for amount in range(1, 100):
        total_coins += calculate_coins(sorted(current_notes, reverse=False), amount)
    expected_coins = total_coins / 100
    return expected_coins, x, y, z, w

# Função principal
# Emprego de processamento paralelo
def item_c():
    initial_coins = []

    # Calculo dos quocientes da divisão de 100
    for i in range(1, 99):
        currentNumber = int(100 // i)
        if currentNumber not in initial_coins:
            initial_coins.append(currentNumber)

    # Ordenação crescente dos quocientes
    initial_coins = sorted(initial_coins)
    min_expected_coins = float('inf')
    best_combination = None
    
    # Encontra o melhor set de 5 valores para as moedas
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(process_combination, combination) for combination in combinations(initial_coins, 5)]
        for future in concurrent.futures.as_completed(futures):
            expected_coins, combination = future.result()
            if expected_coins < min_expected_coins:
                min_expected_coins = expected_coins
                best_combination = combination

    optimal_x = best_combination[1]
    optimal_y = best_combination[2]
    optimal_z = best_combination[3]
    optimal_w = best_combination[4]
    
    # Oscila os valores encontrados para otimizá-los
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = []
        for x in range(initial_coins[initial_coins.index(best_combination[1])-1], initial_coins[initial_coins.index(best_combination[1])+1]+1):
            for y in range(initial_coins[initial_coins.index(best_combination[2])-1], initial_coins[initial_coins.index(best_combination[2])+1]+1):
                for z in range(initial_coins[initial_coins.index(best_combination[3])-1], initial_coins[initial_coins.index(best_combination[3])+1]+1):
                    for w in range(initial_coins[initial_coins.index(best_combination[4])-1], initial_coins[initial_coins.index(best_combination[4])+1]+1):
                      futures.append(executor.submit(process_inner_combination, x, y, z, w, best_combination))
        
        for future in concurrent.futures.as_completed(futures):
            expected_coins, x, y, z, w = future.result()
            if expected_coins < min_expected_coins:
                min_expected_coins = expected_coins
                optimal_x = x
                optimal_y = y
                optimal_z = z
                optimal_w = w
    
    # Fornece o resultado final
    final_result = [best_combination[0]] + [optimal_x, optimal_y, optimal_z, optimal_w]
    print(f"A melhor combinacao de moedas foi {final_result}, que reduz o numero esperado de moedas para {min_expected_coins:.2f}.")

if __name__ == '__main__':
    item_c()
