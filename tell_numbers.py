def rounding_numbers(n, places):
    num = ''
    n = float(n)
    
    if (n <= 999.999) and (n >= -999.999):
        num = float(format(round(n, places)))
    else:
        return n
    
    num1 = int(num)
    num2 = float(num)
    
    if (num1 % num2 == 0):
        return num1
    else:
        return num2
    
    return num

def speak_number(num, n):
    nnn = ''
    num = str(num)
    int_side = num
    dec_side = ''
    
    for i in range(0, len(num)):
        if num[i] == '.':
            int_side = num[:i]
            dec_side = num[i + 1:]
            break
    
    int_side = num
    
    for i in range(0, len(num)):
        if num[i] == '.':
            int_side = num[:i]
            dec_side = num[i + 1:]
    
    int_length = len(int_side)
    
    ones = ['Miden ', 'Ena ', 'Duo ', 'Tria ', 'Tessera ', 'Pente ', 'Eksi ', 'Efta ', 'Okto ', 'Ennia ']
    
    teens = ['Deka ', 'Enteka ', 'Dodeka ', 'Dekatria ', 'Dekatessera ', 'Dekapente ', 'Dekaeksi ', 'Dekaefta ', 'Dekaokto ',
             'Dekaennia ']
    decades = ['', '', 'Eikosi ', 'Trianta ', 'Saranta ', 'Peninta ', 'Eksinta ', 'Ebdominta ', 'Ogdonta ', 'Enneninta ']
    hundreds = ['' ,'Ekaton ', 'Diakosia ', 'Triakosia ', 'Tetrakosia ', 'Pentakosia ', 'Eksakosia ',
                'Eftakosia ', 'Oktakosia ', 'Enniakosia ']
    
    word = ''
    
    int_length = len(int_side)
    iD = int_length
    dec_length =  len(dec_side)
    dD = dec_length
    
    while iD > 0:
        if int_side == '':
            break
        if num == '0':
            word = 'zero'
            break
        elif iD > 1 and int_side[iD - 2] == '1':
            for i in range(0, 10):
                if int_side[iD - 1] == str(i):
                    word = teens[i] + word
        else:
            if iD > 0:
                for i in range(0, 10):
                    if int_side[iD - 1] == str(i):
                        word = ones[i] + word
            if iD > 1:
                for i in range(0, 10):
                    if int_side[iD - 2] == str(i):
                        word = decades[i] + word
            if iD > 2:
                for i in range(0, 10):
                    if int_side[iD - 3] == str(i):
                        word = hundreds[i] + word
        iD -= 3

    while dD > 0:
        word += 'Komma '
        break

    word1 = ''

    iD = int_length
    int_length = len(int_side)
    dD = dec_length
    dec_length = len(dec_side)
    
    while dD > 0:
        if dec_side == '':
            break
        if num == '0':
            word = 'zero'
            break
        elif dD > 1 and dec_side[dD - 2] == '1':
            for i in range(0, 10):
                if dec_side[dD - 1] == str(i):
                    word1 = teens[i] + word1
        else:
            if dD > 0:
                for i in range(0, 10):
                    if dec_side[dD - 1] == str(i):
                        word1 = ones[i] + word1
            if dD > 1:
                for i in range(0, 10):
                    if dec_side[dD - 2] == str(i):
                        word1 = decades[i] + word1
            if dD > 2:
                for i in range(0, 10):
                    if dec_side[dD - 3] == str(i):
                        word1 = hundreds[i] + word1
        dD -= 3
    
    newWord = word+word1
    
    if (float(num) < 0):
        print('MEION',newWord.upper())
    else:
        print(newWord.upper())

    
    return nnn

def main():
    while True:
        n = (input('Dwse enan arithmo h pata Enter gia na termatiseis to programma: '))
        
        while not n:
            exit()
        
        places = 3
        num = rounding_numbers(n, places)
        
        nn = float(n)
        if (nn>=-999.999) and (nn<=999.999):
            nnn=speak_number(num, n)
        else:
            print(n)
        
        continue
        break

if __name__ == '__main__':
    main()
