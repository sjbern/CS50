response = str(input("Type Greeting Here: ")).lower().strip()
word = "hello"

def loser():
    print ("$0")

def partial():
    print ("$20")

def winner():
    print ("$100")
    
if word in response:
    loser()

elif response.startswith('h'): 
    partial()

else:
    winner()
