def findingExtraCharacterInSameString(str1,str2):
    
    for i,j in str1,str2:
        if(str1[i]==str2[j]):
            pass
        else:
            print(str1,str2)


str1 = "Anshoo"
str2 = "Anshoom"
findingExtraCharacterInSameString(str1,str2)            