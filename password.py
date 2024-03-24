import math
import string

def IsValidPassword(pwd):
    
    SpecialSym =['!', '@', '#', '$', '&', '_']
    val = True
    i = 0
    points = 0

    if len(pwd) < 8:
        print('length should be at least 8.')
        val = False

    if not any(char.isdigit() for char in pwd):
        val = False
    else:
        i += 1

    if not any(char.isupper() for char in pwd):
        val = False
    else:
        i += 1

    if not any(char.islower() for char in pwd):
        val = False
    else:
        i += 1

    if not any(char in SpecialSym for char in pwd):
        val = False
    else:
        i += 1

    if (i>=3):
        val = True
        if len(pwd) >= 8:
            points = math.ceil(len(pwd)/4) - 1
            if i == 4:
                points *= 2

    return val, points


def main():
    while True:
        pwd = input('Enter a password:\n')
        evaluation, points = IsValidPassword(pwd)
        if (evaluation):
            print("Password is valid!")
            break
        else:
            print("Your password does not contain information from at least 3/4 categories! Try again! \n")
    
    print(f"Password length is {len(pwd)}, and power is: {int(points)}.")
            
if __name__ == '__main__':
    main()

