print("Sum of elements using star notation recursively")

elements = [1,3,2,4,5,6,6,2,3]

def sum(givenElements):
   head , *tail = givenElements
   print("head is",head)
   print("tail is",tail)
   return head + sum(tail) if tail else head

print(sum(elements))
