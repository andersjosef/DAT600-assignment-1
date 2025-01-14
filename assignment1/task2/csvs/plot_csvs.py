import pandas as pd
import glob


def read_csv(fileName):
    nList = list()
    timeList = list()

    with open (fileName, "r", encoding="utf-8") as f:
        f.__next__()
        for line in f:
            if line == "\n":
                break
            n, time = line.strip().split(",")
            nList.append(int(n))
            timeList.append(float(time))
    return nList, timeList



# Empty data dictionary
data = {}

for file in glob.glob("*.csv"):
    n_list, time_list = read_csv(file)
    name = file.split(".")[0]
    data[name] = dict(zip(n_list, time_list))


for i in range(1, 1000, 100):
    print(f"{i} & {data["java-insertion"][i]:.2e} & {data["python-insertion"][i]:.2e} & {round(data["python-insertion"][i]/data["java-insertion"][i]*100,2)} \\\\")
    print("\\hline")

for i in range(1, 1000, 100):
    print(f"{i} & {data["java-heap"][i]:.2e} & {data["python-heap"][i]:.2e} & {round(data["python-heap"][i]/data["java-heap"][i]*100,2)} \\\\")
    print("\\hline")
