n=int(input("Enter your number"))
print("n is",n)
arr=[]
def buildFirstLevelOutput(n):
    numberOfRows,numberOfColumns=2*n-1,2*n-1
    print(numberOfColumns,numberOfRows)
    
    for i in range(0,numberOfRows):
        l = []
        for j in range(0,numberOfColumns):
            if i==j and i==(numberOfColumns-1)/2:
                l.append(1)
            elif i==0 or j==0 or i==2*n-2 or j==2*n-2:
                l.append(n)
         
        arr.append(l)
      
buildFirstLevelOutput(n)
for row in arr:
    print(row)
def finalOutput(arr,numberOfColumns,numberOfRows):
    for i in range(0,numberOfRows):
        for j in range(0,numberOfColumns):
            if i==j and i==(numberOfColumns-1)/2:
                arr[i][j]=1
            elif i==0 or j==0 or i==2*n-2 or j==2*n-2:
                arr[i][j]=n
            

# arr = []
# def builArray(n):
#     l=[]
#     if n==1:
#         l.append(1)
#         arr.append(l)
#     else:
#         l.appned(n)    
























# buildFirstLevelOutput(n)        
# def buildFinalevelOutput(n):
#     if(n==3):
#         buildFirstLevelOutput(n)
#         return
#     else:
#         buildFinalevelOutput(n-1)    


