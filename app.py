
import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def wordSearch(key):
   
    key = key.lower()
    if key in data:
        return data[key]
    elif key.title() in data:
        return data[key.title()]
    elif len(get_close_matches(key, data.keys())) > 0:
        answer=input("Did you mean %s instead? Enter Y if Yes or N if no: " % get_close_matches(key, data.keys())[0])
        if answer.title() == "Y":
               return data[get_close_matches(key, data.keys())[0]]
        elif answer.title() == "N":
             return "This word does not exist, please check the word"
    else:
        return "We didn't understand your entry"

    
key = input("Please enter a word: ")
output = wordSearch(key)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
