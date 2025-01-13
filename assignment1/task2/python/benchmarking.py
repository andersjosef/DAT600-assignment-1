from sortingAlgorithms import insertion_sort, heap_sort
import matplotlib.pyplot as plt
import time

def init_csv(file):
    with open(file, "w", encoding="utf-8") as f:
        f.write("n,time\n")

def append_to_csv(file, n, time):
    with open(file, "a", encoding="utf-8") as f:
        f.write(f"{n},{time}\n")


def plot_sort(sortFunc, name, max, step):
    fileName = f"python-{name}.csv" 
    init_csv(fileName)
    Yaxis = []
    Xaxis = []
    for i in range(1, max, step):
        nums = list(range(i, 0, -1))
        start_time = time.perf_counter()
        sortFunc(nums)
        end_time = time.perf_counter()
        delta_time = end_time - start_time
        append_to_csv(fileName, len(nums), delta_time)
        Xaxis.append(len(nums))
        Yaxis.append(delta_time)

    plt.plot(Xaxis, Yaxis, label=name)

n = 10000
step = 10
plot_sort(heap_sort, "Heap", n, step)
plot_sort(insertion_sort, "Insertion", n, step)
plt.xlabel("n")
plt.ylabel("Time taken")
plt.legend()
plt.show()
