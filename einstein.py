def main(): 
    x = int(input("Mass: "))
    print("Joules: ",equation(x))

def equation(n):
    return n * 300000000**2

main()