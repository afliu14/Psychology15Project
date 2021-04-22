import csv
import sys
import string
import random

# # pre-COVID data
with open("Confessions_PreCovid.csv", "r") as file:
    reader = csv.reader(file)
    entry = random.sample(list(reader), 200)
    count = 0
    for row in entry:
        if  count == 0:
            count += 1
            continue
        else:
            pretext = row[2]
            presplittext = pretext.split()
            preiwords = 0
            prewewords = 0

            for word in presplittext:
                if word.lower() in ["i"]:
                    preiwords += 1
                if word.lower() in ["we"]:
                    prewewords += 1
            pretotalwords = sum([i.strip(string.punctuation).isalpha() for i in presplittext])

            preipercent = round(preiwords / pretotalwords * 100, 3)
            prewepercent = round(prewewords / pretotalwords * 100, 3)

            print(preipercent)
            print(prewepercent)

# post-COVID data
with open("covidpostconfessions.csv", "r") as file:
    reader = csv.reader(file)
    count= 0
    entry = random.sample(list(reader), 200)
    for row in entry:
        if  count == 0:
            count += 1
            continue
        else:
            posttext = row[2]
            postsplittext = posttext.split()
            postiwords = 0
            postwewords = 0

            for word in postsplittext:
                if word.lower() in ["i"]:
                    postiwords += 1
                if word.lower() in ["we"]:
                    postwewords += 1
            posttotalwords = sum([i.strip(string.punctuation).isalpha() for i in postsplittext])

            postipercent = round(postiwords / posttotalwords * 100, 3)
            postwepercent = round(postwewords / posttotalwords * 100, 3)

            print(postipercent)
            print(postwepercent)