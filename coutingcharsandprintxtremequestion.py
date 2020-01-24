# string = 'c:\\new'
# print(string)
string2  = "asasasasddassffddssasdd"
l=[]

def countCharacter(c):
    count=0
    for item in string2:
        
        if(c==item):
            count=count+1
    return count

 
def findUniqueOccurances(s):
    for item in s:
        if item in l:
            pass
        else:
            l.append(item)

def finalString(s):
    string=''
    findUniqueOccurances(string2)
    for item in l:
        print(countCharacter(item))
        string+=item+str(countCharacter(item))
    print(string)    
finalString(string2)