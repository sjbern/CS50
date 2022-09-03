def main():
    greeting = str(input("Type Greeting Here: ")).lower().strip()
    word = "hello"
    value(greeting)


def value(greeting): #accepts string as input, then returns dollar value of result
    greeting = greeting.lower().strip()
    if 'hello' in greeting:
        return 0
    elif greeting.startswith('h'): 
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
