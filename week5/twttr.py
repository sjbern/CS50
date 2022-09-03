def main():
    user = input("Input: ")
    noVowels = shorten(user)
    print('Output: ' + noVowels)

def shorten(word):
    wordNoVowels = ""
    for letter in word:
        if not letter.lower() in ['a','e','i','o','u']:
            wordNoVowels += letter
    return wordNoVowels

if __name__ == "__main__":
    main()