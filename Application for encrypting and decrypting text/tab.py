'''
#tablica
#       1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26
arr = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
print()
def switch(n):
    while n < 26:
        for i in arr:
            if i == arr[0]:
                print(end = "|")
            print(i, end = "|")
        arr.append(arr[0])
        arr.remove(arr[0])
        print()
        n+=1
switch(0)
print()
'''

def crypt(m, k):
    k *= len(m) // len(k) + 1
    c = ''
    
    for i, j in enumerate(m):
        gg = (ord(j) + ord(k[i]))
        c += chr(gg % 26 + 65)
    return c


 
def decrypt(c, k):
    d = ''
    
    for i, j in enumerate(c):
        gg = (ord(j) - ord(k[i]))
        d += chr(gg % 26 + 65)
    return d


'''
def res(choice, txt, key):
    choice = input('choice c or d: ')

    txt = input()
    key = input()

    if choice == 'c':
        res = (crypt(txt, key))
    elif choice == 'd':
        res = (decrypt(txt, key))
    else:
        res = ('ты еблан смени раскладку')
'''
