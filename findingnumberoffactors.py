def findingnumberoffactors(number):
    factorList = []	
    for i in range(1,number+1):
       	if(number%i==0):
            factorList = factorList + [i]

    return factorList

print(findingnumberoffactors(16)) 
