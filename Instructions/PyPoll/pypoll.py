import os
import csv
filepath ="C:\\Users\\aptho\\Downloads\\Instructions\\Instructions\\PyPoll\\Resources\\election_data.csv"
voter = 0
candidates = []
votecount = []
khancount = [] 
correycount = []
licount = []
otooleycount = []


    
with open(filepath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    first_row = next(csvreader)
    voter = 1
    khan = 0
    correy = 0
    li = 0 
    otooley = 0
    

    for row in csvreader:
        voter += 1 
        votecount = str(first_row[0])  
        candidates.append(row[2])
        
    for candidate in candidates:
        if candidate == "Khan":
            khancount.append(candidates)
            khan = len(khancount)
        elif candidate == "Correy":
            correycount.append(candidates)
            correy = len(correycount)
        elif candidate == "Li":
            licount.append(candidates)
            li = len(licount)
        else:
            otooleycount.append(candidates)
            otooley = len(otooleycount)

    

    khan_per =round(((khan / voter) * 100), 2)
    correy_per = round(((correy / voter) * 100), 2)
    li_per = round (((li / voter) *100), 2)
    otooley_per = round(((otooley / voter) *100),2)
    

  
print("Election Results") 
print("---------------------------") 
print(f"Total Votes: {voter}") 
print("----------------------------") 
print(f"Khan:{khan_per} % {khan}") 
print(f"Correy:{correy_per} % {correy}") 
print(f"Li:{li_per} % {li}") 
print(f"O'Tooley:{otooley_per} % {otooley}") 
print("----------------------------") 
print(f"Winner: Khan ") 