s='10010'
i=0
decimalvalue=0
while(s!=''):
     
    decimalvalue+=int(s[-1])*2**i
    print("decimal value",decimalvalue)
    i=i+1
    s=s[:-1]
    print(s)
print(decimalvalue)    