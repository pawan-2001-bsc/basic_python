"""
Write a Python program that takes two numbers, start and end, and prints all prime numbers in that range.

Example:
  For start = 10, end = 30:
  11, 13, 17, 19, 23, 29
"""


start=int(input("Enter starting number:"))

end=int(input("Enter ending number:"))



for i in range(start,end):
    if i<2:
        continue

    is_prime=True

    for j in range(2,i):
        if i%j==0:
            is_prime=False
            break


    if is_prime:
        print(i)
