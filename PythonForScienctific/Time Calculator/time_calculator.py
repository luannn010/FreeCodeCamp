def add_time(start_time, added_time, date=""):
    # Split time and halves
    time, halve = start_time.split()

    # Separate halves
    if halve == "AM":
        k = 1
    else:
        k = 2

    start_hour, start_min = time_split(time)
    added_hour, added_min = time_split(added_time)

    # Convert to integers
    start_hour = int(start_hour)
    added_hour = int(added_hour)
    start_min = int(start_min)
    added_min = int(added_min)

    # Add minutes and handle rollover
    new_min = (start_min + added_min)%60
    added_min_hour = (start_min + added_min)//60
    

    #new_hour
    new_hour = (start_hour + added_hour + added_min_hour -1)%12 +1


    #Add new halve
    halves = (start_hour + added_hour + added_min_hour)//12 + k
    if halves%2 == 0:
        new_halve = "PM"
    else:
        new_halve = "AM"


    # Add new day 
    # In case from AM to PM dont change the date
    if halves != 2:
        day = halves//2
    else:
        day = 0
    
    # Get the message
    if halves <=2:
        new_day = ""
    elif 3 <= halves <= 4:
        new_day = " (next day)"
    else:
        new_day = f" ({day} days later)"
    # Incase no date and with date
    if date != "":
        new_date = get_date(date, day)
        new_time = f"{new_hour}:{new_min:02d} {new_halve}, {new_date}{new_day}"
    else:
        new_time = f"{new_hour}:{new_min:02d} {new_halve}{new_day}"

    # Format the time string
    
    return new_time


def time_split(clock):
    hour, minute = clock.split(":")
    return hour, minute


def get_date(date, added_days):
    weekdates = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for i in range(len(weekdates)):
        if weekdates[i].lower() == date.lower():
            x = i

    x += added_days % len(weekdates)
    x %= len(weekdates)
    return weekdates[x]


