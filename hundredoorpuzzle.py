# There are 100 doors in a row, all doors are initially closed. A person walks through all doors multiple times and toggle (if open then close, if close then open) them in following way:
# In first walk, the person toggles every door

# In second walk, the person toggles every second door, i.e., 2nd, 4th, 6th, 8th, …



# In third walk, the person toggles every third door, i.e. 3rd, 6th, 9th, …

# ………
# ……….

# In 100th walk, the person toggles 100th door.

# Which doors are open in the end?
doors=['c' for i in range(1,100)]
count=0
def toggle(doors,iteration):
    count=iteration-1
    while(count<len(doors)):
        if(doors[count]=='o'):
            doors[count]='c'
            count=count+iteration
        elif(doors[count]=='c'):
            doors[count]='o'
            count=count+iteration
     

for iteration in range(1,101):
    toggle(doors,iteration)
print("Final Out put",doors,len(doors))

openedDoorsAre = []
countInDoors=0
while(countInDoors<len(doors)):
    if(doors[countInDoors]=='o'):
        openedDoorsAre.append(countInDoors+1)
        countInDoors=countInDoors+1
    else:
        countInDoors=countInDoors+1   
print("Opened doors are ",openedDoorsAre)        

