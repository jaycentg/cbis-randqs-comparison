import random

def generate_random(n, start, end, seed):
    random.seed(seed)
    return [
        random.randint(start, end)
        for _ in range(n)
    ]

def generate_sorted(n, start, end, seed):
    random_list = generate_random(n, start, end, seed)
    return sorted(random_list)

def generate_reversed(n, start, end, seed):
    random_list = generate_random(n, start, end, seed)
    return sorted(random_list, reverse=True)