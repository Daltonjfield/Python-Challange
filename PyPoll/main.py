import os
import csv
import collections
from collections import Counter

#Variables
candidates = []
total_candidate_votes = []


csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        #print(row)
        candidates.append(row[2])

    #Created a sorted list of the candidates 
    voter_list = sorted(candidates)

    #Find the number of votes per candidate and put into a list in ascending order
    candidates_votes = Counter(voter_list)
    total_candidate_votes.append(candidates_votes.most_common())
    #print(f'{total_candidate_votes}')

    #Percentage of votes
    for item in total_candidate_votes: 
        first_place = format((item[0][1])*100/(sum(candidates_votes.values())),'.3f')
        #print(f'{first_place}')
        second_place = format((item[1][1])*100/(sum(candidates_votes.values())),'.3f')
        #print(f'{second_place}')
        third_place = format((item[2][1])*100/(sum(candidates_votes.values())),'.3f')
        #print(f'{third_place}')
        fourth_place = format((item[3][1])*100/(sum(candidates_votes.values())),'.3f')
        #print(f'{fourth_place}')




        
        
         

    


    


    





        

