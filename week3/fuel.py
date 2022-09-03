def calc(x,y):
    return round((int(x)/int(y))*100)

def main():
    while True:
        try:
            fraction = input("Fraction: ")
            num, dom = fraction.split("/")
            ans = calc(num,dom)
            if ans <= 1.0:
                    print("E")
                    break
            elif 100.0 >= ans >= 99.0:
                    print("F")
                    break      
            elif 1.0 < ans < 99.0:
                    print(ans,'%',sep='')
                    break
            elif ans > 100:
                    pass

        except (ValueError,ZeroDivisionError):
            #do something?
            pass
                
main()


