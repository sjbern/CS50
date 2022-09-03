import re
import sys
#no other libraries!

def main():
    print(count(input("Text: ")))

def count(s):
    sent = re.findall(r'\bum\b',s, re.IGNORECASE)
    return len(sent)

if __name__ == "__main__":
    main()