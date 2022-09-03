text = input("Input: ")
output = print("Output: ", end="")

for vowel in text:
    if not vowel.lower() in ['a','e','i','o','u']:
        print(vowel, end="")

print()