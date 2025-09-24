import random
import time
import algorithms

def test_algorithm(algorithm, data):
    start = time.time()
    sorted_arr, comparisons, swaps = algorithm(data)
    end = time.time()
    return {
        "time": end - start,
        "comparisons": comparisons,
        "swaps": swaps  
    }

def run_test():
    sizes = [100, 500, 1000]
    results = {}
    algos = {
        "Bubbl Sort": algorithms.bubble_sort,
        "Insertion Sort": algorithms.insertion_sort,
        "Merge Sort": algorithms.merge_sort,
        "Selection Sort": algorithms.selection_sort
    }

    for size in sizes:
        data = [random.randint(1,1000) for _ in range(size)]
        results[size] = {}
        for name , algo in algos.items():
            results[size][name]= test_algorithm(algo, data)
    return results
print(run_test())