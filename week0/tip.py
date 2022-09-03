def main():
    dollars = dollars_to_float(input("How much was the meal? ")) or  0
    percent = percent_to_float(input("What percentage would you like to tip? ")) or 0
    tip = dollars * (percent/100)
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    dollas = d.replace('$','')
    return float(dollas)

def percent_to_float(p):
    percento = p.replace('%','')
    return float(percento)

main()