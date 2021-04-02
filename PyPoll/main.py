# Module Import
import csv # CSV module for csv read/write

# CSV file path
csv_path = r'C:\Users\huayu\Documents\GitHub\python-challenge\PyPoll\Resources\election_data.csv'

# Election Analysis Function
def ElectionAnalysis(election_csv):
    '''
    Parameters: 
        election_csv (csvfile) - The csv data that will be taken in for analysis.
    Return: 
        None
    Description:
        This function will conduct the election anlaysis based on the election_csv file. 
    '''
    # Var init
    election_dict = {}
    dict_keys = []
    percentage = []
    winner_per = 0
    total_vote = 0
    winner = ""

    # Going trhough each row in election_csv
    for row in election_csv:
        if row[2] not in election_dict.keys():
            election_dict[row[2]] = 1
        else:
            election_dict[row[2]] += 1
        total_vote += 1

    for key in election_dict.keys():
        dict_keys.append(key)
        percentage.append(round(election_dict[key]/total_vote*100))
    
    for i in range(len(dict_keys)):
        if election_dict[dict_keys[i]] > winner_per:
            winner_per = election_dict[dict_keys[i]]
            winner = dict_keys[i]
    
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_vote}")
    print("-------------------------")
    print(f"{dict_keys[0]}: {percentage[0]}.000% ({election_dict[dict_keys[0]]})")
    print(f"{dict_keys[1]}: {percentage[1]}.000% ({election_dict[dict_keys[1]]})")
    print(f"{dict_keys[2]}: {percentage[2]}.000% ({election_dict[dict_keys[2]]})")
    print(f"{dict_keys[3]}: {percentage[3]}.000% ({election_dict[dict_keys[3]]})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    # Export result to text file
#    export_file = open(r"C:\Users\huayu\Documents\GitHub\python-challenge\PyBank\Analysis\Financial Analysis.txt", "w")
#    export_file.write("Financial Analysis\n")
#    export_file.write("-------------------------------\n")
#    export_file.write(f"Total Months: {len(months)}\n")
#    export_file.write(f"Total: ${sum(total_list)}\n")
#    export_file.write(f"Average Change: ${average}\n")
#    export_file.write(f"Greatest Increase in Profits: {increase_date} (${increase})\n")
#    export_file.write(f"Greatest Decrease in Profits: {decrease_date} (${decrease})\n")
#    export_file.close()
    

    return None

# Main executable
def main():
    '''
    Description: Main executtable function.
    '''
    # Open csv file using csv_path
    with open(csv_path, "r") as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ",")
        header = next(csvreader, None)

        # Pass csvreader into the Financial Analysis Function
        ElectionAnalysis(csvreader)

if __name__ == "__main__":
    main()
