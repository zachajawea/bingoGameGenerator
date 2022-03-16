import random as r
import logging
import csv

#Variable to hold list of buzzwords
words = list()


#Pull the list of buzzwords from a file
try:
    file = "buzzWords.txt"
    mode = "r"
    fin = open(file, mode)
    words = fin.readlines()
    logging.info("file read")
except:
    raise
    logging.critical("Error opening file. Closing script.")
    exit(0)

#This is just a test to see what has been loaded into the buzzwords list
logging.debug(words)

#Print a provided number of bingo boards
numberOfBoards = int(input("How many boards to output?"))
columnTitle = "B \t I \t N \t G \t O"

for k in range(numberOfBoards):
    logging.info("Printing Board #"+str(k)+":")

    #Generate Random Numbers
    indexes = r.sample(range(0,len(words)),len(words))
    logging.debug("List of random indexes is:" + str(indexes))

    print(columnTitle)
    for i in range(5):
        for j in range(5):
            word = words[indexes[(i*5)+j]]
            print(word, end = "\t")
        print("\n")
