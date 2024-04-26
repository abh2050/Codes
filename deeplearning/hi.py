import random

def generate_random_numbers(n, start=1, end=100):
    """Generate n random numbers between start and end (inclusive)."""
    return [random.randint(start, end) for _ in range(n)]

# Generate 10 random numbers between 1 and 100
random_numbers = generate_random_numbers(10)
print(random_numbers)
# Daily change made at 2024-04-25 22:21:50
# Daily change made at 2024-04-25 22:22:16
# Change made at 2024-04-25 22:30:39
# Change made at 2024-04-25 22:31:01