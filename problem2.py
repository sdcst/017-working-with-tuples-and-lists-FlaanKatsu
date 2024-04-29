#! python3
"""
Print the list named "fruit".
Ask the user to enter a word
If the word is in the list, delete all occurrences of that word from the list
If the word is not in the list, add the word to the list
Print out the updated list

inputs:
string

outputs:
list

examples:
['apple', 'cherry', 'kiwi', 'apple', 'banana', 'strawberry', 'kiwi', 'blueberry', 'kiwi']
Enter a word from the list:kiwi
['apple', 'cherry', 'apple', 'banana', 'strawberry', 'blueberry']

['apple', 'cherry', 'kiwi', 'apple', 'banana', 'strawberry', 'kiwi', 'blueberry', 'kiwi']
Enter a word from the list:orange
word not in list
['apple', 'cherry', 'kiwi', 'apple', 'banana', 'strawberry', 'kiwi', 'blueberry', 'kiwi', 'orange']

"""

fruit = ["apple","cherry","kiwi","apple","banana","strawberry","kiwi","blueberry","kiwi"]

a = 0
print(fruit)
n = input("Please enter a word from the list, or to add to the list: ")
a = fruit.count(n)
if a > 0:
    for i in range (0,a):
        fruit.remove(n)
    print(fruit)
elif a == 0:
    fruit.append(n)
    print(fruit)