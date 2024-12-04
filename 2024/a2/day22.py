import numpy as np

def is_safe(x):
    return (np.all(x < 0) or np.all(x > 0)) and np.all(np.abs(x) <= 3)

safe = [0, 0]
with open("input.txt") as file:
    for line in file:
        x = np.fromstring(line, sep=" ")
        safe[0] += int(is_safe(np.diff(x)))
        for i in range(len(x)):
            if is_safe(np.diff(np.delete(x, [i]))):
                safe[1] += 1
                break
print(safe)