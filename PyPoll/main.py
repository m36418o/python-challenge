# Module Import
import csv # CSV module for csv read/write

# CSV file path
csv_path = r'C:\Users\huayu\Documents\GitHub\python-challenge\PyPoll\Resources\election_data.csv'

# Financial Analysis Function
def FinancialAnalysis(budget_csv):
    '''
    Parameters: 
        budget_csv (csvfile) - The csv data that will be taken in for analysis.
    Return: 
        None
    Description:
        This function will conduct the financial anlaysis based on the budget_csv file. 
    '''
    # Var init
    months = []
    changes = []
    total_list = []
    increase_date = ""
    decrease_date = ""
    increase = 0
    decrease = 0

    # Going trhough each row in budget_csv
    for row in budget_csv:
        total_list.append(int(row[1]))
        months.append(row[0])

    # Going through each item in the total_list
    for i in range(0,len(total_list) - 1):
        diff = total_list[i + 1] - total_list[i] # Calculate difference of profit between months
        changes.append(diff)
        # Conditional to check for max and min of differences
        if diff > increase: 
            increase = diff
            increase_date = months[i + 1]
        elif diff < decrease:
            decrease = diff
            decrease_date = months[i + 1]

    # Calculate average changes between months
    average = round(sum(changes)/len(changes),2)
    
    # Printing result to terminal
    print("Financial Analysis")
    print("-------------------------------")
    print(f"Total Months: {len(months)}")
    print(f"Total: ${sum(total_list)}")
    print(f"Average Change: ${average}")
    print(f"Greatest Increase in Profits: {increase_date} (${increase})")
    print(f"Greatest Decrease in Profits: {decrease_date} (${decrease})")

    # Export result to text file
    export_file = open(r"C:\Users\huayu\Documents\GitHub\python-challenge\PyBank\Analysis\Financial Analysis.txt", "w")
    export_file.write("Financial Analysis\n")
    export_file.write("-------------------------------\n")
    export_file.write(f"Total Months: {len(months)}\n")
    export_file.write(f"Total: ${sum(total_list)}\n")
    export_file.write(f"Average Change: ${average}\n")
    export_file.write(f"Greatest Increase in Profits: {increase_date} (${increase})\n")
    export_file.write(f"Greatest Decrease in Profits: {decrease_date} (${decrease})\n")
    export_file.close()

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
        FinancialAnalysis(csvreader)

if __name__ == "__main__":
    main()
