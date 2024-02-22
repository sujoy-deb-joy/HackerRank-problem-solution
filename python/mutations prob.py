# Read a given string, change the character at a given index and then print the modified string.
def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]