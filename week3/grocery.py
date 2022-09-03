dict = {}

#loop that cycles inputs until ctrld is inputted
while True:
    try:
        item = input().upper()
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1
    except EOFError:# this command breaks user out of input loop
        for key in sorted(dict.keys()):
            print(dict[key], key.upper())
        break



#when ctrld inputted, output dictionary with quantities
