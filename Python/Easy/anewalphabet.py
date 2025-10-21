a = str(input()).lower() # Convert input to lowercase to handle uppercase letters

print( # Print the transformed string
    a.replace('a', '@')
    .replace('b', '8')
    .replace('c', '(')
    .replace('d', '|)')
    .replace('e', '3')
    .replace('f', '#')
    .replace('g', '6')
    .replace('h', '[-]')
    .replace('i', '|')
    .replace('j', '_|')
    .replace('k', '|<')
    .replace('l', '1')
    .replace('m', '[]\/[]')
    .replace('n', '[]\[]')
    .replace('o', '0')
    .replace('p', '|D')
    .replace('q', '(,)')
    .replace('r', '|Z')
    .replace('s', '$')
    .replace('t', "']['") # important cant have '']['' use "']['" instead
    .replace('v', '\/')
    .replace('w', '\/\/')
    .replace('x', '}{')
    .replace('y', '`/')
    .replace('z', '2')) # Prints the input string with each letter replaced by the next letter in the alphabet, wrapping around from z to a

