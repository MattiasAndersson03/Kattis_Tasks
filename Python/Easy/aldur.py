a = int(input())  # Reads an integer input representing the count of numbers
numbers = []

for _ in range(a): 
    num = int(input()) # Reads each number input 
    numbers.append(num) # Appends the number to the list
print(min(numbers)) # Prints the smallest number from the list