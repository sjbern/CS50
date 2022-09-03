balance = 50
list = [5, 10, 25]

while balance > 0:
    print("Amount due: ", balance)
    coin = int(input("Insert coin: "))
    if coin in list:
        balance -= coin

while balance == 0:
    print("Change owed: 0")
    break

while balance < 0:
    print("Change owed:", balance*-1)
    break

if coin not in list:
    print("Amount due: 50")