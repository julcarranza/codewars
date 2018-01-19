ef b2d(a):
    d = 0
    for  i, b in enumerate(a): d += int(b)*(-2)**i
    return d

def d2b(n):
    bin, i = [], 0
    while (n - b2d(bin)) != 0 and i < 16:
        if (n - b2d(bin)) % ( (-2)**(i+1)) != 0:
            bin.append(1)
        else:
            bin.append(0)
        i +=1
    if len(bin)<1: bin =[0]
    bin.reverse()
    return ''.join(str(v) for v in bin)

def skrzat(base, number):
    if base == 'b':
        a = list(number)
        a.reverse()
        text = "From binary: "+ str(number) + " is " + str(b2d(a))
    elif base == 'd':
        text = "From decimal: "+ str(number) + " is " + str(d2b(number))
    return text
    
print skrzat('b', '0')
print skrzat('b', '1001101')
print skrzat('b', '0111111')
print skrzat('b', '101001000100001')
print skrzat('b', '010010001000010')
print skrzat('b', '100110100110100')
print skrzat('d', 89)
print skrzat('d', -137)
print skrzat('d', 137)
print skrzat('d', 8191)
print skrzat('d', -10000)
print skrzat('d', 21000)
print skrzat('d', 0)

