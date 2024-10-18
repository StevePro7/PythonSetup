from datetime import datetime

# 1. Getting the Current Date and Time
now = datetime.now()
print(f"Current date and time: {now}")

# 3. Formatting Dates and Times
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted date and time: {formatted}")

# 4. Parsing Dates and Times from Strings
date_string = "2023-01-01 15:00:00"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(f"Parsed date and time: {parsed_date}")

# 9. Getting the Weekday
weekday = now.strftime("%A")
print(f"Today is: {weekday}")
