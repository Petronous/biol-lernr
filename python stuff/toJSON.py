import json

with open('answers.txt', 'r', encoding = 'utf-8') as of:
    with open('answers.json', 'w', encoding = 'utf-8') as target:
        arr = of.read().split('\n.\n')
        #print(arr[1])
        json.dump(arr, target)

with open('questions.txt', 'r', encoding = 'utf-8') as of:
    with open('questions.json', 'w', encoding = 'utf-8') as target:
        arr = of.read().split('\n')
        #print(arr[1])
        json.dump(arr, target)
