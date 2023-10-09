# Create a program that generates 100 random numbers and find the frequency of each number.

import random

random_numbers = [random.randint(1, 10) for _ in range(100)]

frequency_dict = {}

for number in random_numbers:
    if number in frequency_dict:
        frequency_dict[number] += 1
    else:
        frequency_dict[number] = 1

for number, frequency in frequency_dict.items():
    print(f"Number {number}: Frequency {frequency}")