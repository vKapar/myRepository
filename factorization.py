import math

def Elaxisto_Koino_Pollaplasio(a, b):
    if a > b:
        greater = a
    else:
        greater = b
    while(True):
        if((greater % a == 0) and (greater % b == 0)):
            ekp = greater
            break
        greater += 1
    return ekp

def Megistos_koinos_Dieretis(a, b):
    if a > b:
        smaller = b
    else:
        smaller = a
    for i in range(1, smaller+1):
        if((a % i == 0) and (b % i == 0)):
            mkd = i
    return mkd

def paragontes(n):
    result=dict()
    c = 2
    while(n > 1):
        if(n % c == 0):
            if c not in result:
                result[c]=0
            
            n/=c
            result[c]+=1
        else:
            c += 1
        
    print(result)

def main():
    n1, n2 = map(int, input("Dwse duo thetikous akeraious: ").split())
    print(f'= {int(n1)}', paragontes(n1))
    print(f'= {int(n2)}', paragontes(n2))
    print(f"EKP:{int(n1),int(n2)} = ", Elaxisto_Koino_Pollaplasio(n1, n2))
    print(f"MKD:{int(n1),int(n2)} = ", Megistos_koinos_Dieretis(n1, n2))

if  __name__ == '__main__':
    main()
