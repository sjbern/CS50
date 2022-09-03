names = []
while True:
    try:
        x = input()
        names.append(str(x))
    except EOFError:
        break

if len(names) > 2:
    print(f'Adieu, adieu, to {", ".join(names[:-1])}, and {names[-1]}')
elif len(names) == 2:
    print(f'Adieu, adieu, to {"".join(names[0])} and {names[1]}')
elif len(names) == 1:
    print(f'Adieu, adieu, to {"".join(names)}')
