months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    user = input("Date: ")
    try:
        month, day, year = user.split('/')
        if (0 < int(month) < 13) and (0 < int(day) < 32):
            year = year.replace(' ','')
            month = month.replace(' ','')
            day = day.replace(' ','')
            break
        elif (0 >= int(month) or int(month) >= 13):
            print("Error, month does not exist")
        elif (0 >= int(day) or int(day) >= 32):
            print("Error, day does not exist")
    except: #this is here to capture inputs that do not meet integer formats, like month names
        try:
            month1, day1, year = user.split(' ')
            for _ in range(len(months)):
                if month1 == months[_]:
                    month = _ + 1
            day = day1.replace(",","")
            if (0 < int(month) < 13) and (0 < int(day) < 32):
                break
        except:
            pass


print(f"{year}-{int(month):02}-{int(day):02}")