# Make a program that prints 3 random numbers.
import random

# Generate and print 3 random numbers
for _ in range(3):
    random_number = random.randint(
        1, 100
    )  # Generates a random integer between 1 and 100 (inclusive)
    print(random_number)