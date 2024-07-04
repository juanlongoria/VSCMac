def read_steps_file(file_path):
    with open(file_path, 'r') as file:
        steps = [int(line.strip()) for line in file]
    return steps

def calculate_monthly_averages(steps):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    monthly_averages = []
    
    start_day = 0
    for days in days_in_month:
        month_steps = steps[start_day:start_day + days]
        monthly_average = sum(month_steps) / days
        monthly_averages.append(monthly_average)
        start_day += days
    
    return monthly_averages

def display_monthly_averages(monthly_averages):
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    
    for month, average in zip(months, monthly_averages):
        print(f"{month}: {average:.2f} steps")

# Main function to run the program
def main():
    file_path = '/Users/juanlongoria/Code/VSCMac/steps.txt'  # The path to your file
    steps = read_steps_file(file_path)
    monthly_averages = calculate_monthly_averages(steps)
    display_monthly_averages(monthly_averages)

if __name__ == "__main__":
    main()

#Show the code completed