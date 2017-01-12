#!/usr/bin/python3
# David Prater
# 9/13/2015
# Program to determine the outcome of an election

import sys

dictionary = {}
totalElectionVotes = 0

print(("Candidates").center(15), ("Votes").rjust(8), ("Percent").rjust(8))
print(("==========").center(15), ("=====").rjust(8), ("=======").rjust(8))

fo = open(sys.argv[1], "r")

for line in fo:
	curentLine = line.split()
	name = (str(curentLine[0]) + " " + str(curentLine[1]))

	vote = (int(curentLine[2]) + int(curentLine[3]) + int(curentLine[4]) + int(curentLine[5]))
	dictionary[str(name)] = vote
	
	totalElectionVotes += vote
	

fo.close()

totalVotes = 0

winningVotes = 0

for name in dictionary:
	currentvote = dictionary[name]
	if(currentvote > winningVotes):
		winningVotes = currentvote
		winner = name
		winnersvote=currentvote
	totalVotes += currentvote

	percent = str(int(round((currentvote/totalElectionVotes), 2)*100))

	print(str(name).center(15), str(currentvote).rjust(8), str(percent + " %").rjust(8))

#print winner and total election votes
print("\nThe winner is", winner, "with", winnersvote, "votes!")
print("\nTotal votes polled:", totalVotes)

