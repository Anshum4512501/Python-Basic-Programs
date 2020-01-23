# s = input("Enter a string that you want to search in \n")
def countChar(c,s):
    count,j = 0,len(s)
    for i in s :
        j = j-1
        if i==c:
            count = count+1
        if j == 0:
             break
    print(c , count)
# c = input("Enter a character that you need to search\n")
# countChar(c)