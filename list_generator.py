import random

def generate_random(n, start, end, seed):
    random.seed(seed)
    arr = [
        random.randint(start, end)
        for _ in range(n)
    ]
    write_to_file(arr, "random", seed)
    return arr

def generate_sorted(n, start, end, seed):
    random_list = generate_random(n, start, end, seed)
    arr = sorted(random_list)
    write_to_file(arr, "sorted", seed)
    return arr

def generate_reversed(n, start, end, seed):
    random_list = generate_random(n, start, end, seed)
    arr = sorted(random_list, reverse=True)
    write_to_file(arr, "reversed", seed)
    return arr

def write_to_file(arr, arr_type, seed):
    filename = f"{arr_type}_{len(arr)}_seed{seed}.txt"
    with open(filename, "w") as file:
        for num in arr:
            file.write(str(num) + "\n")