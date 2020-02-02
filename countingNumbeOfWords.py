def countNumberOfWords(wordList,word):
    
    count,j = 0,len(wordList)
    for item in wordList :
        j = j-1
        if item==word:
            count = count+1
        if j == 0:
             break
    print(word , count)

wordList = ["Anshoo","Amit","Anshoo","Anjali","Pransu","Vivek","Anshoo","Amit","Vivek","Anjali"]
print("Word list is : ", wordList)
word = input("\n What do you want to search  in word list ? \n")  

countNumberOfWords(wordList,word)