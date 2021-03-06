# allows loading json files
import json

# functionality for similar words
from difflib import get_close_matches as gcm

# loads dictionary
data = json.load(open("dictionary.json"))

# processes input word
def translate(word):
    
    # ensures input word is all lowercase
    word = word.lower()

# checks dictionary for word
# ** modify to only search keys in keys:values pairs
    if word in data:
       return data[word]
# search for similar word if input word is not found
    elif len(gcm(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no"% gcm(word, data.keys())[0])
        if (yn.lower() == "y"):
            return data[gcm(word, data.keys())[0]]
        else:
            return "No entry found."
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
