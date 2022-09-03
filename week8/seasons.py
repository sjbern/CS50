from datetime import date, datetime
import re, sys, inflect

def main():
    userInput = input('Date of Birth: ')
    if validate(userInput) is False:
        sys.exit('Invalid')
    calculate(userInput)




def validate(userInput):
    if re.search(r'^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$', userInput):
        return True
    return False

def calculate(userInput): #takes user input and calculates difference, returns str
    strToday = str(date.today())
    deltaMin = (datetime.strptime(strToday, "%Y-%m-%d")) - (datetime.strptime(userInput, "%Y-%m-%d"))
    difInDays = str(deltaMin).split()
    days = (int(difInDays[0]) * 1440)
    p = inflect.engine()
    ans = (p.number_to_words(days, andword="") + ' minutes').capitalize()
    print(ans)
    return ans

if __name__ == "__main__":
    main()