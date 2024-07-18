def calculate_speeds(distance,times):

    return [d / t for d, t in zip(distance, times)]

distances = [10, 20, 30, 40, 50]

times = [1, 5, 3, 2, 4]

print(calculate_speeds(distances,times))