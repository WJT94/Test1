import time

start = 0
end = 0
bigList = []
size = 10000000


def refresh_list():
    global start
    global end
    print("\nCreating a fresh list...")
    start = time.time()
    bigList.clear()
    for i in range(size):
        bigList.append(i)
    end = time.time()
    print_time()


def print_time():
    global start
    global end
    print(str((end - start) * 1000.0), "milliseconds")


print(f"Adding 1 to all values in a list of {'{:,}'.format(size)} numbers.")

refresh_list()
print(f"\n'for i in range(len(list))' method for {'{:,}'.format(len(bigList))} entries.")
start = time.time()
for i in range(len(bigList)):
    bigList[i] += 1
end = time.time()
print_time()

refresh_list()
print(f"\n'enumerate list[i] += 1' method for {'{:,}'.format(len(bigList))} entries.")
start = time.time()
for i, v in enumerate(bigList):
    bigList[i] += 1
end = time.time()
print_time()

refresh_list()
print(f"\n'enumerate list[i] = v + 1' method for {'{:,}'.format(len(bigList))} entries.")
start = time.time()
for i, v in enumerate(bigList):
    bigList[i] = v + 1
end = time.time()
print_time()
