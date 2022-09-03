import random, emoji, time, sys, itertools

#change log
# - 

#todo
# - emoji support
# - deck quantity
# - cleanup var

#lists
vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']

deck = list(itertools.product(vals, suits))
balance = 1000


#functions
def user_hand():
    time.sleep(1)
    z = deck[x], deck[x+1]
    print(z)

def user_hit():
    time.sleep(1)
    print(deck[x], deck[x+1])
    print(deck[x+2])


def dealer_hand():
    time.sleep(1)
    print(deck[x+3])
    print(deck[x+4])


#new game loop
#print(f"Welcome to the crappiest blackjack game ever developed. Your starting balance is {balance} fake monies. ")
#time.sleep(3)
#whil = 0
#while whil < 3:
#    print("Press (S)tart to start a game, or press (Q)uit if you're afraid of losing to a computer.")
#    game = input().upper()
#    if game == 'Q':
#        sys.exit('See ya loser!')
#    elif game == 'S':
#        print("Awesome, dealer is shuffling")
#        whil = 3
#    else:
#        print("Invalid input, try again.")
#        whil += 1

while balance > 0:
    random.shuffle(deck)
    x=0
    print("Your hand:")
    hand1 = user_hand()
    print("Dealer's hand:")
    dhand = dealer_hand()
    print("What would you like to do? (H)it, (S)tay, (F)old, or Side (B)et")
    user = str(input('')).upper()   

    if user == 'H':
        user_hit()
        balance = balance -1000
    elif user == 'F':
        continue
