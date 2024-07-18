import random
from collections  import Counter

num_rolls = 500

rolls = [random.randint(1, 6) for _ in range(num_rolls)]

roll_counts = Counter(rolls)

faces = range(1, 7)

result = list(map(lambda face: f"{face}: {roll_counts[face]}", faces))

result = list(filter(lambda x: int(x.split(':')[1]) > 0, result))

for r in result:
    print(r)