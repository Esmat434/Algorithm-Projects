from analyzer import run_test
import matplotlib.pyplot as plt

if __name__ == '__main__':
    results = run_test()
    for size,res in results.items():
        print(f"\nList Size: {size}")
        for algo, metrics in res.items():
            print(f"{algo}: Time={metrics['time']:.5f}s, Comparisons={metrics['comparisons']}, Swaps={metrics['swaps']}")

    sizes = list(results.keys())
    for algo in results[sizes[0]].keys():
        times = [results[size][algo]["time"] for size in sizes]
        plt.plot(sizes, times, label=algo)
    
    plt.xlabel("Input Size")
    plt.ylabel("Time (seconds)")
    plt.title("Sorting Algorithms Performance")
    plt.legend()
    plt.show()