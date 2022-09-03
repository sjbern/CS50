def main():
    fraction = input("Fraction: ") #accept user input as string
    ans = convert(fraction) #convert user string input into two integers, return x and y
    gauge(ans) #if else statements to determine fullness

def convert(fraction):
    x, y = fraction.split('/')
    ans = round((int(x)/int(y))*100)
    return ans

def gauge(ans):
    while True:
        try:
            if ans <= 1:
                    print("E")
                    break
            elif 100 >= ans >= 99:
                    print("F")
                    break
            elif 1 < ans < 99:
                    print(ans,'%',sep='')
                    break
            elif ans > 100:
                    pass
        except (ValueError,ZeroDivisionError):
            pass

if __name__ == "__main__":
    main()