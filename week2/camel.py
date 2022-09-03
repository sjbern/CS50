camel = str(input("camelCase: "))

for upper in camel:
    if upper.isupper():
        print("_" + upper.lower(), end='')

    else:
        print(upper, end="")
print()
