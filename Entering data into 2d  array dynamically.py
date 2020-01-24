m = int(input("Enter number of rows \n"))
n = int(input("Enter number of columns \n"))

arr =[]
# while m >=0:
#     while n>=0:
#         l.append(int(input("Enter a number \n")))
#         n=n-1
#         if(n==0):
#             print("\n Enter another row")
#     arr.append(l)
#     m=m-1
#

for i in range(0,m):
    l = []
    for j in range(0,n):
        l.append(int(input("Enter a number \n")))
    print("You have entred this row",l)    
    arr.append(l)
print(arr)
