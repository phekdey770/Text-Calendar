import calendar
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def print_full_calendar(year):
    # Create a TextCalendar instance with Sunday as the first day of the week
    cal = calendar.TextCalendar(firstweekday=6)
    
    # Loop through all months
    for month in range(1, 13):
        print(f"+{'-' * 20}+")
        print(f"|{calendar.month_name[month].center(18)}")
        print(f"+{'-' * 20}+")
        
        # Print the days header (Sun, Mon, Tue, etc.)
        print("Su Mo Tu We Th Fr Sa")
        
        # Print the month's calendar
        month_cal = cal.monthdayscalendar(year, month)
        for week in month_cal:
            for i, day in enumerate(week):
                if day == 0:  # Day outside the current month
                    print("  ", end=" ")
                elif i == 0:  # Sunday
                    print(Fore.RED + f"{day:2}", end=" ")
                elif i == 6:  # Saturday
                    print(Fore.LIGHTYELLOW_EX + f"{day:2}", end=" ")
                else:  # Weekday (Monday to Friday)
                    print(Fore.WHITE + f"{day:2}", end=" ")
            print()
        
        # Print a blank line to separate months
        print()
        print()

# Show full calendar for 2024
print_full_calendar(2024)
