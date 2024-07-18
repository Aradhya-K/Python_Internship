def solve_puzzles(total_heads, total_legs):

    for num_chickens in range(total_heads + 1):

        num_rabbits = total_heads - num_chickens 

        if 2* num_chickens + 4* num_rabbits ==  total_legs:
            return num_chickens, num_rabbits
    return None 

total_heads = 35
total_legs = 94

solution = solve_puzzles(total_heads, total_legs)

if solution:
    chickens,rabbits = solution
    print(f"Chickens: {chickens}, Rabbits :{rabbits}")

else:
    print("no solution found")    