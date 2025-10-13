n = int(input().strip())
s = input().strip() # Read input string

if "lv" in s: # Check if 'lv' is in the string
    print(0) # Both 'l' and 'v' are present
elif ('l' in s) or ('v' in s):
    print(1) # Only one of 'l' or 'v' is present
else:
    print(2) # Neither 'l' nor 'v' is present