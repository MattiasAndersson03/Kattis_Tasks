a = int(input())
trees = list(map(int, input().split())) # Takes a list of integers as input
trees.sort(reverse=True) # Sorts the list of trees in descending order
max_days = 0
for i in range(len(trees)):
    max_days = max(max_days, trees[i] + i + 1) # Calculates the maximum days needed
print(max_days + 1) # Prints the result incremented by 1