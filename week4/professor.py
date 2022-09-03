import random, sys

def main():
    level = get_level()
    score = game(level)
    print('Score: ', score)

def get_level():
    while True:
        try: 
            level = int(input("Level: "))
            if 0 < level and level <=3:
                break
        except:
            pass
    return level

def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x,y

def round(x,y):
    loss = 1
    while loss <= 3:
        try:
            ans = int(input(f"{x} + {y} = "))
            if ans == (x + y):
                return True
            else:
                loss += 1
                print('EEE')
        except:
            loss += 1
            print("EEE")
    print(f'{x} + {y} = {x+y}')  
    return False 

def game(level):
    turn = 1
    score = 0
    while turn <= 10:
        x, y = generate_integer(level)
        if round(x,y) == True:
            score += 1
        turn += 1
    return score

if __name__ == "__main__":
    main()