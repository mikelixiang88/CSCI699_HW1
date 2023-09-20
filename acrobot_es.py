import numpy as np

def parse_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    data = [tuple(map(float, line.strip().replace('(', '').replace(')', '').split(','))) for line in lines]
    return data

def estimate_lengths(filename):
    data = parse_input(filename)
    A_x = []
    A_y = []
    b_x = []
    b_y = []

    for (theta1, theta2, x, y) in data:
        A_x.append([np.cos(theta1), np.cos(theta1 + theta2)])
        b_x.append(x)
        A_y.append([np.sin(theta1), np.sin(theta1 + theta2)])
        b_y.append(y)

    A_x = np.array(A_x)
    A_y = np.array(A_y)
    b_x = np.array(b_x)
    b_y = np.array(b_y)
    l1_x, l2_x = np.linalg.lstsq(A_x, b_x, rcond=None)[0]
    l1_y, l2_y = np.linalg.lstsq(A_y, b_y, rcond=None)[0]
    print(f"Estimated l1_x: {l1_x}")
    print(f"Estimated l2_x: {l2_x}")
    print(f"Estimated l1_y: {l1_y}")
    print(f"Estimated l2_y: {l2_y}")
    l1 = (l1_x + l1_y) / 2
    l2 = (l2_x + l2_y) / 2

    return l1, l2

filename = "noisy_acrobot.txt"
data=parse_input(filename)
l1, l2 = estimate_lengths(filename)
print(f"Estimated l1: {l1}")
print(f"Estimated l2: {l2}")
