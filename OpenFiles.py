f = open("test.txt")
line = f.readlines(100)
for word in line:
    for char in word:
       if char == '\n':
           
           word[word.__len__()-1] = ' '
    print(word)       