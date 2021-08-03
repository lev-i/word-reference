# loads dictionary
import json

data = json.load(open("dictionary.json"))

# processes input word
# **add functionality for words similar to entry if no entry found
def translate(word):
    
    # ensures input word is all lowercase
    word = word.lower()

# checks dictionary for word
# ** modify to only search keys in keys:values pairs
    if word in data:
       return data[word]
    else:
       return "No entry found."     

# takes user input
word = input("Enter word to define: ")
# translates (lower case)
output = translate(word)

# makes output readable
if type(output) == list:
    for item in output:
        print(item)
else: 
    print(output)
