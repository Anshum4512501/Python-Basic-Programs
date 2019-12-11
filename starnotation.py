sample = [("Anshoo",25,"Anjali"),("Gate",12,['a','b','c','d']),("Arcadia","xtremesoftech",[1,12,"horse"])]

data1,*_,data2 = sample

print(data1)
print(data2)


records = [
 ('foo', 1, 2),
 ('bar', 'hello'),
 ('foo', 3, 4),
]


def do_foo(x, y):
   print('foo', x, y)
def do_bar(s):
   print('bar', s)
for tag, *args in records:
   print("tag is",tag)
   print("*arg is", *args)
   if tag == 'foo':
     do_foo(*args)
   elif tag == 'bar':
     do_bar(*args)
for tuples in records:
   print("tuples are ",tuples)
