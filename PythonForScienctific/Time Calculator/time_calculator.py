def add_time(start_time, added_time, date=""):
    weekdate = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Split time and halves
    time, halve = start_time.split()
    
    # Separate halves
    if halve == "AM":
        k = 1
    else:
        k = 2
    
    hour, minute = time_split(time)
    added_hour, added_minute = time_split(added_time)
    
    hour = int(hour)
    added_hour = int(added_hour)
    minute = int(minute)
    added_minute = int(added_minute)
    
    # Add 1 hour when minutes exceed 60
    minute += added_minute
    if minute >= 60:
        minute -= 60
        hour += 1
    
    # Calculate the updated hour
    hour += added_hour % 12 -12
    
    # Calculate the added halves
    added_halve = k + (added_hour // 12)
    

    if added_halve == 2:
        day = ""
    elif added_halve == 3 or added_halve == 4:
        day = "next day"
    else:
        added_day = (added_halve - 2)//2
        day = f"{added_day} days later"
    
    # Get the halve
    if added_halve % 2 == 0:
        halve = "PM"
    else:
        halve = "AM"
    
    # Format the time string
    new_time = f"{hour}:{minute:02d} {halve}"
    if date:
        new_time += f", {date}"
    if day:
        new_time += f" ({day})"
    
    print(new_time)


def time_split(clock):
    hour, minute = clock.split(":")
    return hour, minute


add_time("12:00 PM", "13:23")
add_time("12:20 AM", "20:12")
