# place this file inside the same folder as your CSV results file
# from explorer. >save as>csv file

# this script will take from each csv the topic and the corresponding sentiment and prevelance
# then output for easy copy pasting into excel for a nice table

# kyle august 22 2018
# Credit for Nina's help


import csv
import glob
import pandas as pd

# change the csvnames to the names of the files with quotes surrounding
# with a comma seperating the names
excel_names = glob.glob("*.xlsx")  # List of csv files

# list of labels you want to compare
# then just run the program
listoflabels = ["Overall Staff Service",
                "Food and Drink",
                "Overall Seat",
                "Time Issues",
                "In Flight Entertainment",
                "Overall Cost",
                "Overall Baggage"]  # List of lables you want

for names in excel_names:
    excel_file = pd.read_excel(names,0)

    labels = []
    pos_scores = []
    neg_scores = []
    prevelances = []

    for row in excel_file:
        label = row[1]
        pos_score = row[7]
        neg_score = row[6]
        prevelance = row[3]

        labels.append(label)
        pos_scores.append(pos_score)
        neg_scores.append(neg_score)
        prevelances.append(prevelance)

print(names)

print("topic", ",", "prevelance", ",", "positive sentiment", ",", "negative sentiment", ",", "net sentiment")
for topics in listoflabels:
    j = [pos for pos, char in enumerate(labels) if char == topics]
    k = [pos for pos, char in enumerate(labels) if char == topics]
    l = [pos for pos, char in enumerate(labels) if char == topics]

    print(topics, ",", prevelances[k[0]], ",", pos_scores[j[0]], ",", neg_scores[l[0]], ",",
          float(pos_scores[j[0]]) - float(neg_scores[l[0]]))

