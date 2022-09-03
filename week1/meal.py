def convert(time):
    hours, minutes = time.split(":")
    new_time = float(minutes) / 60
    return float(hours) + new_time

user_time = input("What time is it? ")
time = convert(user_time)

if 7.0 <= time <= 8.0:
    print("Breakfast time")

elif 12.0 <= time <= 13.0:
    print("Lunch time")

elif 12.0 <= time <= 19.0:
    print("Dinner time")

