l = [3,4,7,1,2,8,0,9]
maximum = max(l)
for x in range(maximum):
    strs=''
    for item in l:
        if(maximum-x<=item):
            strs+='*'
        else:
            strs+=' '
    print(strs)    
             
    
      
           