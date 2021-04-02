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
    total_vote = 0

    # Going trhough each row in election_csv
    for row in election_csv:
        if row[2] not in election_dict.keys():
            election_dict[row[2]] = 1
        else:
            election_dict[row[2]] += 1
        total_vote += 1

    for key in election_dict.keys():
        dict_keys.append(key)
        percentage.append(round(election_dict[key]/total_vote*100, 3))
    
    print(percentage[0])
    
    
    # Printing result to terminal
#    print("Financial Analysis")
#    print("-------------------------------")
#    print(f"Total Months: {len(months)}")
#    print(f"Total: ${sum(total_list)}")
#    print(f"Average Change: ${average}")
#    print(f"Greatest Increase in Profits: {increase_date} (${increase})")
#    print(f"Greatest Decrease in Profits: {decrease_date} (${decrease})")

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
