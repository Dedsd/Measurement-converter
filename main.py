class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def main():
    while True:
        converter()
        q = input("You would like to convert again? (y/n): ").lower()
        if q == 'y':
            pass
        else:
            break

print(color.RED + "Measurement converter" + color.END)


def converter():
    try:
        q1 = int(input("Enter the value that you want to convert: "))
    except:
        print(color.BOLD + "This is not a number, please try again" + color.END)
        return True
    q2 = input("Enter the measure of the value you entered before: ")
    if q2 == 'km':
        q3 = input("Enter the measurement you want to convert: ")
        if q3 == 'mi':
            a1 = (q1)*(0.62)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a1}{q3} {color.END}")
        elif q3 == 'm':
            a9 = (q1) * (1000)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a9}{q3} {color.END}")
        else:
            print("This value can't be converted")
    elif q2 == 'mi':
        q3 = input("Enter the measurement you want to convert: ")
        if q3 == 'km':
            a2 = (q1) * (1.61)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a2}{q3} {color.END}")
        elif q3 == 'm':
            a10 = (q1) * (1609.34)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a10}{q3} {color.END}")
        else:
            print("This value can't be converted")
    elif q2 == 'm':
        q3 = input("Enter the measurement you want to convert: ")
        if q3 == 'yd':
            a3 = (q1) * (1.09)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a3}{q3} {color.END}")
        elif q3 == 'ft':
            a5 = (q1) * (3.28)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a5}{q3} {color.END}")
        elif q3 == 'in':
            a7 = (q1) * (39.37)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a7}{q3} {color.END}")
        else:
            print("This value can't be converted")
    elif q2 == 'yd':
        q3 = input("Enter the measurement you want to convert: ")
        if q3 == 'm':
            a4 = (q1) * (0.91)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a4}{q3} {color.END}")
        else:
            print("This value can't be converted")
    elif q2 == 'ft':
        q3 = input("Enter the measurement you want to convert: ")
        if q3 == 'm':
            a6 = (q1) * (0.3)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a6}{q3} {color.END}")
        else:
            print("This value can't be converted")
    elif q2 == 'in':
        q3 = input("Enter the measurement you want to convert: ")
        if q3 == 'm':
            a8 = (q1) * (0.03)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a8}{q3} {color.END}")
        else:
            print("This value can't be converted")
    elif q2 == 'l':
        q3 = input("Enter the measurement you want to convert: ")
        if q3 == 'gal':
            a11 = (q1) * (0.26)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a11}{q3} {color.END}")
        elif q3 == 'oz':
            a12 = (q1) * (35.2)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a12}{q3} {color.END}")
        else:
            print("This value can't be converted")
    elif q2 == 'gal':
        q3 = input("Enter the measurement you want to convert: ")
        if q3 == 'l':
            a13 = (q1) * (4.55)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a13}{q3} {color.END}")
        elif q3 == 'oz':
            a14 = (q1) * (160)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a14}{q3} {color.END}")
        else:
            print("This value can't be converted")
    elif q2 == 'oz':
        q3 = input("Enter the measurement you want to convert: ")
        if q3 == 'l':
            a15 = (q1) * (0.03)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a15}{q3} {color.END}")
        elif q3 == 'gal':
            a16 = (q1) * (0.01)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a16}{q3} {color.END}")
        else:
            print("This value can't be converted")
    elif q2 == 'kg':
        q3 = input("Enter the measurement you want to convert: ")
        if q3 == 'lb':
            a17 = (q1) * (2.2)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a17}{q3} {color.END}")
        elif q3 == 'ounce':
            a18 = (q1) * (35.27)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a18}{q3} {color.END}")
        else:
            print("This value can't be converted")
    elif q2 == 'lb':
        q3 = input("Enter the measurement you want to convert: ")
        if q3 == 'kg':
            a19 = (q1) * (0.45)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a19}{q3} {color.END}")
        elif q3 == 'ounce':
            a20 = (q1) * (16)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a20}{q3} {color.END}")
        else:
            print("This value can't be converted")
    elif q2 == 'ounce':
        q3 = input("Enter the measurement you want to convert: ")
        if q3 == 'kg':
            a21 = (q1) * (0.03)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a21}{q3} {color.END}")
        elif q3 == 'lb':
            a22 = (q1) * (0.06)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a22}{q3} {color.END}")
        else:
            print("This value can't be converted")
    elif q2 == 'm^2':
        q3 = input("Enter the measurement you want to convert: ")
        if q3 == 'yr^2':
            a23 = (q1) * (1.2)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a23}{q3} {color.END}")
        elif q3 == 'ft^2':
            a24 = (q1) * (10.76)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a24}{q3} {color.END}")
        elif q3 == 'in^2':
            a25 = (q1) * (1550)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a25}{q3} {color.END}")
        else:
            print("This value can't be converted")
    elif q2 == 'yr^2':
        q3 = input("Enter the measurement you want to convert: ")
        if q3 == 'm^2':
            a26 = (q1) * (0.84)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a26}{q3} {color.END}")
        elif q3 == 'ft^2':
            a27 = (q1) * (9)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a27}{q3} {color.END}")
        elif q3 == 'in^2':
            a28 = (q1) * (1296)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a28}{q3} {color.END}")
        else:
            print("This value can't be converted")
    elif q2 == 'ft^2':
        q3 = input("Enter the measurement you want to convert: ")
        if q3 == 'm^2':
            a29 = (q1) * (0.09)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a29}{q3} {color.END}")
        elif q3 == 'yr^2':
            a30 = (q1) * (0.11)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a30}{q3} {color.END}")
        elif q3 == 'in^2':
            a31 = (q1) * (144)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a31}{q3} {color.END}")
        else:
            print("This value can't be converted")
    elif q2 == 'in^2':
        q3 = input("Enter the measurement you want to convert: ")
        if q3 == 'ft^2':
            a32 = (q1) * (0.01)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a32}{q3} {color.END}")
        else:
            print("This value can't be converted")
    elif q2 == 'km/h':
        q3 = input("Enter the measurement you want to convert: ")
        if q3 == 'mph':
            a33 = (q1) * (0.62)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a33}{q3} {color.END}")
        elif q3 == 'knot':
            a34 = (q1) * (0.54)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a34}{q3} {color.END}")
        else:
            print("This value can't be converted")
    elif q2 == 'mph':
        q3 = input("Enter the measurement you want to convert: ")
        if q3 == 'km/h':
            a35 = (q1) * (1.61)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a35}{q3} {color.END}")
        elif q3 == 'knot':
            a36 = (q1) * (0.87)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a36}{q3} {color.END}")
        else:
            print("This value can't be converted")
    elif q2 == 'knot':
        q3 = input("Enter the measurement you want to convert: ")
        if q3 == 'km/h':
            a37 = (q1) * (1.85)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a37}{q3} {color.END}")
        elif q3 == 'mph':
            a38 = (q1) * (1.15)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a38}{q3} {color.END}")
        else:
            print("This value can't be converted")
    elif q2 == 'km/s':
        q3 = input("Enter the measurement you want to convert: ")
        if q3 == 'km/h':
            a39 = (q1) * (3600)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a39}{q3} {color.END}")
        elif q3 == 'mph':
            a40 = (q1) * (2236.94)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a40}{q3} {color.END}")
        elif q3 == 'knot':
            a41 = (q1) * (1943.84)
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a41}{q3} {color.END}")
        else:
            print("This value can't be converted")
    else:
        print(color.BOLD + "A typo or a non-existent value, try again" + color.END)

if __name__ == "__main__":
    main()
