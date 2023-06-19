def add_time(Time, added_time, date=""):
    weekdate = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Split time and halves
    time, halve = Time.split()
    
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
    if minute + added_minute > 60:
        minute -= 60
        hour += 1
    
    # Calculate the updated hour
    hour = hour + (added_hour % 12)
    
    # Calculate the added halves
    k = k + (added_hour // 12)
    
    # Get the halve
    if k % 2 == 0:
        halve = "PM"
    else:
        halve = "AM"
    
    # Format the time string
    new_time = f"{hour}:{minute:02d} {halve}"
    
    print(new_time)


def time_split(clock):
    hour, minute = clock.split(":")
    return hour, minute


add_time("12:00 PM", "10:23")
add_time("12:20 AM","20:12")
