m = int(input("Enter number of rows \n"))
n = int(input("Enter number of columns \n"))
l = []
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

for i in range(0,m-1):
    for j in range(0,n-1):
        l.append(int(input("Enter a number \n")))
    arr.append(l[i])
print(arr)
