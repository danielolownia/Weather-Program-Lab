import random

num = int(input("How many days of tempereratures do you want? Enter a number: "))

for i in range(num):
    temp = random.randint(-10, 40)
    print(f"Day {i + 1}: {temp:1f}°C")
