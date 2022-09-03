import re
import sys


def main():
    ans = validate(input("IPv4 Address: "))
    if ans == True:
        print('Valid')
    elif ans == False:
        print('Invalid')

def validate(ip):
    if re.search('^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$', ip):
        return True
    else:
        return False





if __name__ == "__main__":
    main()
