import math

data = (10.0, 10.0, 10.0, 10.0, 10.0)

strategies = (
    ("Усереднене", lambda d: sum(d) / len(d)),
    ("Середнє перемноження", lambda d: math.prod(d) ** (1 / len(d))),
    ("Середнє пропорційне", lambda d: len(d) / sum(1 / x for x in d))
)

def find_max_average(data_tuple:tuple, strategy_tuple:tuple):
    results = []
    for name, func in strategy_tuple:
        result = func(data_tuple)
        results.append((name, result))
        print(f"-> Обчислення {name} = {result:.3f}")
    max_name, max_value = max(results, key=lambda x: x[1])
    print(f"\nНайвищий результат ({max_name}) = {max_value:.3f}")
    return max_name, max_value

if __name__ == "__main__":
    find_max_average(data, strategies)