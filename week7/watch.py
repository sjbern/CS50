import re
import sys

def main():
    linkInput = input("HTML: ")
    if 'youtube' in linkInput:
        parse(linkInput)
        print(ans)
    else:
        sys.exit('None')


def parse(s):
    match = re.search("(?P<url>https?://[^\"]+)", s).group("url")
    if match and 'youtube' in match:
        ans = re.sub(r'^https?://(www\.)?youtube\.com/embed/', 'https://youtu.be/', match)
        return ans
    else:
        sys.exit('None')


if __name__ == "__main__":
    main()