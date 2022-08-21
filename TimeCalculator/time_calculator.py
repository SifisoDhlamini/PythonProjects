def add_time(start, duration, day_of_week=None):
    time, midday = start.split()
    hrs, mins = map(int, time.split(':'))
    max_hrs = 24
    max_mins = 60
    if midday == "PM":
        hrs = hrs + 12

    d_hrs, d_mins = map(int, duration.split(':'))
    tot_mins = mins + d_mins
    add_hrs = tot_mins // max_mins
    d_hrs += add_hrs
    tot_hrs = d_hrs + hrs
    days = tot_hrs // max_hrs

    rem_mins = tot_mins % max_mins
    rem_hrs = tot_hrs % max_hrs

    new_midday = 'AM'
    if rem_hrs > 12:
        rem_hrs = rem_hrs % 12
        new_midday = 'PM'
    if rem_hrs == 12 and rem_mins > 0:
        new_midday = 'PM'
    if rem_hrs == 0:
        rem_hrs = 12
        new_midday = 'AM'

    appending = ""
    days_of_the_week = ['Monday', 'Tuesday', 'Wednesday',
                        'Thursday', 'Friday', 'Saturday', 'Sunday']
    if days == 0 and day_of_week:
        appending = f", {day_of_week}"
    elif days == 1 and day_of_week:
        appending = f", {days_of_the_week[(days_of_the_week.index(day_of_week.title()) + days) % 7]} (next day)"
    elif days == 1:
        appending = f" (next day)"
    elif days >= 1 and day_of_week:
        appending = f", {days_of_the_week[(days_of_the_week.index(day_of_week.title()) + days) % 7]} ({days} days later)"
    elif days > 1:
        appending = f" ({days} days later)"

    new_time = f"{rem_hrs}:{rem_mins:02d} {new_midday}{appending}"

    return new_time

def main():
    print(add_time("3:30 PM", "2:12"))  # expected = "5:42 PM"
    print(add_time("11:55 AM", "3:12"))  # expected = "3:07 PM"
    print(add_time("9:15 PM", "5:30"))  # expected = "2:45 AM (next day)"
    print(add_time("11:40 AM", "0:25")) # expected = "12:05 PM"
    print(add_time("2:59 AM", "24:00")) # expected = "2:59 AM (next day)"
    print(add_time("11:59 PM", "24:05")) # expected = "12:04 AM (2 days later)"
    print(add_time("8:16 PM", "466:02")) # expected = "6:18 AM (20 days later)"
    print(add_time("5:01 AM", "0:00")) # expected = "5:01 AM"
    print(add_time("3:30 PM", "2:12", "Monday")) # expected = "5:42 PM, Monday"
    print(add_time("2:59 AM", "24:00", "saturDay")) # expected = "2:59 AM, Sunday (next day)"
    print(add_time("11:59 PM", "24:05", "Wednesday")) # expected = "12:04 AM, Friday (2 days later)"
    print(add_time("8:16 PM", "466:02", "tuesday")) # expected = "6:18 AM, Monday (20 days later)"

    

if __name__ == '__main__':
    main()
