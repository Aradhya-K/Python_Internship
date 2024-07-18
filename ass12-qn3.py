import random
def generate_random_list(size, lower_bound=0, upper_bound=100):
    """
    Generate a list of random integers.

    Parameters:
    size (int): Number of random integers to generate.
    lower_bound (int): Lower bound of the random integers (inclusive).
    upper_bound (int): Upper bound of the random integers (inclusive).

    Returns:
    list: List of random integers.
    """
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]
def select_random_items(lst, k):
    """
    Select k random items from a list.

    Parameters:
    lst (list): The list to select items from.
    k (int): Number of items to select.

    Returns:
    list: List of k randomly selected items.
    """
    return random.sample(lst, k)
random_list = generate_random_list(20, 1, 50)
print("Generated list:", random_list)
selected_items = select_random_items(random_list, 5)
print("Randomly selected items", selected_items)