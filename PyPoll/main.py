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

    #Total Votes
    total_votes = sum(candidates_votes.values())
    #print(f"{total_votes})

    #Candidate placements
    first_candidate = total_candidate_votes[0][0][0]
    #print(f"{first_candidate}")
    second_candidate = total_candidate_votes[0][1][0]
    third_candidate = total_candidate_votes[0][2][0]
    fourth_candidate = total_candidate_votes[0][3][0]

    #Voting placement
    first_place = total_candidate_votes[0][0][1]
    #print(f"{first_place}")
    second_place = total_candidate_votes[0][1][1]
    third_place = total_candidate_votes[0][2][1]
    fourth_place = total_candidate_votes[0][3][1]
    
    #Percentage of votes
    for item in total_candidate_votes: 
        first_percentage = format((item[0][1])*100/(sum(candidates_votes.values())),'.3f')
        #print(f'{first_place}')
        second_percentage = format((item[1][1])*100/(sum(candidates_votes.values())),'.3f')
        #print(f'{second_place}')
        third_percentage = format((item[2][1])*100/(sum(candidates_votes.values())),'.3f')
        #print(f'{third_place}')
        fourth_percentage = format((item[3][1])*100/(sum(candidates_votes.values())),'.3f')
        #print(f'{fourth_place}')


    



print("Election Results")
print("-------------------")
print(f"Total Votes: {total_votes}")
print("--------------------")
print(f"{first_candidate}: {first_percentage}% ({first_place}")
print(f"{second_candidate} : {second_percentage}% ({second_place})")
print(f"{third_candidate} : {third_percentage}% ({third_place})")
print(f"{fourth_candidate} : {fourth_percentage}% ({fourth_place})")
print("---------------------")
print(f"Winner : {first_candidate}")
print("---------------------")

output_path = os.path.join("Analysis", "election_results.txt")
with open(output_path, "w") as outfile:
    outfile.write("Election Results\n")
    outfile.write("-------------------\n")
    outfile.write(f"Total Votes: {total_votes}\n")
    outfile.write("--------------------\n")
    outfile.write(f"{first_candidate}: {first_percentage}% ({first_place}\n")
    outfile.write(f"{second_candidate} : {second_percentage}% ({second_place})\n")
    outfile.write(f"{third_candidate} : {third_percentage}% ({third_place})\n")
    outfile.write(f"{fourth_candidate} : {fourth_percentage}% ({fourth_place})\n")
    outfile.write("---------------------\n")
    outfile.write(f"Winner : {first_candidate}\n")
    outfile.write("---------------------\n")
    





        
        
         

    


    


    





        

