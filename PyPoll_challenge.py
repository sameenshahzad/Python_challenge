# Add dependencies 
import os
import csv

csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath) as csvfile :
    csvreader = csv.reader(csvfile, delimiter=',')
    Header = next (csvreader)

    # Tracking votes and candidates
    votes = []
    candidates_list = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]

    #initialize counters and variables 
    total_votes = 0
    total_votes_cand_1 = 0
    total_votes_cand_2 = 0
    total_votes_cand_3 = 0


    for row in csvreader :
        total_votes += 1
        candidate = row[2]

        if candidate == candidates_list[0]:
            total_votes_cand_1 = total_votes_cand_1 + 1

        if candidate == candidates_list[1]:
            total_votes_cand_2 = total_votes_cand_2 + 1

        if candidate == candidates_list[2]:
            total_votes_cand_3 = total_votes_cand_3 + 1

cand_1_percent = round ((total_votes_cand_1 / total_votes)*100,3)
cand_2_percent = round((total_votes_cand_2 / total_votes)*100,3)
cand_3_percent = round((total_votes_cand_3 / total_votes)*100,3)

# Winning candidate

if cand_1_percent > cand_2_percent and cand_3_percent:
    winner = candidates_list[0]

if cand_2_percent > cand_1_percent and cand_3_percent:
    winner = candidates_list[1]

if cand_3_percent > cand_1_percent and cand_2_percent:
    winner = candidates_list[2]

print ("Election Results")
print ("-------------------------")
print ("Total Votes:" + str(total_votes))
print ("-------------------------")
print ("Charles Casper Stockham: ", cand_1_percent,"%","(",total_votes_cand_1, ")")
print ("Diana DeGette: ", cand_2_percent,"%","(",total_votes_cand_2, ")")
print ("Raymon Anthony Doane: ", cand_3_percent,"%","(",total_votes_cand_3, ")")
print ("-------------------------")
print ("Winner = ", winner)
print ("-------------------------")
#----Output file in txt
output_file = os.path.join("PyPoll_results.txt") 

with open(output_file, "w") as datafile:
    print("Election Results", file=datafile)
    print("--------------------------------", file=datafile)
    print ("Total Votes:" + str(total_votes), file=datafile)
    print ("-------------------------", file=datafile)
    print ("Charles Casper Stockham: ", cand_1_percent,"%","(",total_votes_cand_1, ")", file=datafile)
    print ("Diana DeGette: ", cand_2_percent,"%","(",total_votes_cand_2, ")", file=datafile)
    print ("Raymon Anthony Doane: ", cand_3_percent,"%","(",total_votes_cand_3, ")", file=datafile)
    print ("-------------------------", file=datafile)
    print ("Winner = ", winner, file=datafile)
    print ("-------------------------", file=datafile)