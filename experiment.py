import cbis
import list_generator
import randomized_quick_sort
import time

RANDOM_SEED = 12

def do_cbis(arr, arr_type):
    start_time = time.time()
    # tidak disimpan di variabel agar waktu assignment tidak dihitung
    cbis.cbis(arr)
    end_time = time.time()
    delta = (end_time - start_time) * 1000
    print(f"Sorting CBIS dengan array {arr_type} berukuran {len(arr)} menghabiskan {delta:.10f} ms.")

def do_rand_quicksort(arr, arr_type):
    start_time = time.time()
    # tidak disimpan di variabel agar waktu assigmment tidak dihitung
    randomized_quick_sort.quicksort_helper(arr)
    end_time = time.time()
    delta = (end_time - start_time) * 1000
    print(f"Sorting Randomized Quicksort dengan array {arr_type} berukuran {len(arr)} menghabiskan {delta:.10f} ms.")

def main():
    print("Perbandingan Algoritma Sorting")
    print("Clustered Binary Insertion Sort vs Randomized Quick Sort")
    print("oleh Jaycent Gunawan Ongris - 2106750231 - DAA C")
    print("="*80)

    arr_small_rand = list_generator.generate_random(200, 1, 500, RANDOM_SEED)
    arr_small_sorted = list_generator.generate_sorted(200, 1, 500, RANDOM_SEED)
    arr_small_reversed = list_generator.generate_reversed(200, 1, 500, RANDOM_SEED)

    arr_medium_rand = list_generator.generate_random(2000, 1, 5000, RANDOM_SEED)
    arr_medium_sorted = list_generator.generate_sorted(2000, 1, 5000, RANDOM_SEED)
    arr_medium_reversed = list_generator.generate_reversed(2000, 1, 5000, RANDOM_SEED)

    arr_large_rand = list_generator.generate_random(20000, 1, 50000, RANDOM_SEED)
    arr_large_sorted = list_generator.generate_sorted(20000, 1, 50000, RANDOM_SEED)
    arr_large_reversed = list_generator.generate_reversed(20000, 1, 50000, RANDOM_SEED)

    do_cbis(arr_small_rand, "random")
    do_cbis(arr_small_sorted, "sorted")
    do_cbis(arr_small_reversed, "reversed")

    print("="*80)
    
    do_rand_quicksort(arr_small_rand, "random")
    do_rand_quicksort(arr_small_sorted, "sorted")
    do_rand_quicksort(arr_small_reversed, "reversed")

    print("="*80)

    do_cbis(arr_medium_rand, "random")
    do_cbis(arr_medium_sorted, "sorted")
    do_cbis(arr_medium_reversed, "reversed")

    print("="*80)
    
    do_rand_quicksort(arr_medium_rand, "random")
    do_rand_quicksort(arr_medium_sorted, "sorted")
    do_rand_quicksort(arr_medium_reversed, "reversed")

    print("="*80)

    do_cbis(arr_large_rand, "random")
    do_cbis(arr_large_sorted, "sorted")
    do_cbis(arr_large_reversed, "reversed")

    print("="*80)
    
    do_rand_quicksort(arr_large_rand, "random")
    do_rand_quicksort(arr_large_sorted, "sorted")
    do_rand_quicksort(arr_large_reversed, "reversed")

if __name__ == '__main__':
    main()