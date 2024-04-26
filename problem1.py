#!python3
"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list

example:
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
Choose a person from the list to replace:Rick
Enter the replacement:Dan
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']

"""

nlist = ['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
print(f"there is a list of people.\nthe list is \"{nlist}\"")
n = input("choose a person from the list to destroy: ")
try:
    a = list.index(n)
    print(a)
except:
    print("user input error")