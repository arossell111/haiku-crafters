import csv
import random

def get_data():
    words = {}
    with open('../../data/wan_pairs.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            if row[0] not in words:
                words[row[0]] = [(row[1], float(row[2]))]
            else:
                words[row[0]].append((row[1], float(row[2])))
    return words

words = get_data()
cue = None

while cue == None:
    cue = input("Enter your cue: ")
    if cue in words:
        print("Your cue is", cue)
    else:
        cue = None
        print("Invalid cue")


print(words[cue][random.randint(0, len(words[cue]))])