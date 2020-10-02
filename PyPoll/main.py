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

    voter_list = sorted(candidates)
    #print(f'{voter_list}')

    candidates_list = Counter(voter_list)
    #print(f'{candidates}')

    total_candidate_votes.append(candidates_list.most_common())
    print(f'{total_candidate_votes}')
    


    





        

