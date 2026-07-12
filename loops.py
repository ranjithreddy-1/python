#loops
#for,while,range,pass,continue,break
#for loop
'''a=[10,20,30,40,50]
for i in a:
    print(i)'''

'''a=[10,20,30,40,50]
for i in a:
    print(a)'''

'''a=[10,20,30,40,50]
for i in a:
    print(i,end=",")'''#[10,20,30,40,50]

'''a=[10,20,30,40,50]
for i in a:
    print(i)
print(type(a))
print(type(i))'''
      
'''a=(1,2,3,4,5)
for i in a:
    print(i)
print(type(a))
print(type(i))'''
      
'''d={"year":2026,"month":"july","date":10}
for i in d:
    print(i)
for i in d.keys()
      print(i)
      print(type(a))
      print(type(i))
for i in d.values():
      print(i)
      print(type(a))
      print(type(i))
for i in d.items():
      print(i)
      print(type(a))
      print(type(i))'''

'''a="codegnan"
for i in a:
    print(i)'''#codegnan vertical print 

'''a=["python","java","html"."css"]
   for i in a:
       print(i)
print(type(a))
print(type(i))'''

'''a=[1,2,3,4]
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a=[True,False]
for i in a:
    print(i)'''

'''a=[5+8j,2+6j]
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''fruits=["apple","banana","mango"]'''
#["APPLE","BANANA","MANGO"]
'''fruits=["apple","banana","mango"]
b=[]
for i in fruits:
    b.append(i.upper())
print(b)'''

'''a=["apple","banana","mango"]
b=str(a)
print(b.upper())'''

'''a=[10,20,30,40,50,"code"]
for i in a[-1]:
    a.append(i)
print(a)'''

'''a.extend("code")
print(a)'''

'''a=[2,3,5,6,7]
#[2,3,4,5,6,7]
a.insert(4)
print(a)'''

'''b=(5,6,7,8,9,10)
#(5,6,7,8,9)
c=list(b)
c.pop(5)
d=tuple(c)
print(d)'''

'''e=[7,9,2,0,1,4,9,3,20]
#[0,1,2,3,4,7,9,9,20]
e.sort()
print(e)'''

#while loop
'''a=10
while a>1:
    print(a)'''

'''a=10
while a>1:
    print(a)
    a=a-1'''

'''a=10
while a>1:
    a=a-1
    print(a)'''

'''a=10
while a>1:
    a=a-1
print(a)'''#1

'''a=20
while a>5:
    a=a-1
print(a)'''#5

'''a=30
while a>2:
    print(a)
    a+=1'''# 30 to infinity

'''a=30
while a>2:
    print(a)
    a-=1'''# 30 to 2
'''a=5
while a>25:
    print(a)
    a=a-1'''

'''while True:
    age=int(input("enter the age: "))
    if age>=18:
       print("eligible for vote")
    else:
       print("not eligible")'''

#range -the range function returns sequence of numbers and conditions implememnted by one by one start deault 0
#start-stop-step

'''for i in range(10):
    print(i)'''#0-9
'''for i in range(5,15):
    print(i)'''#5-14
'''for i in range(30,45):
    print(i,end=",")'''#30-44 in a single line
'''for i in range(2,20,2):
    print(i,end=",")'''#2-18
'''for i in range(5,50,5):
    print(i,end=",")'''#5-45
'''for i in range(0,30,3):
    print(i,end=",")'''#0,3,6,9,12,15,18,21,24,27,30

'''while True:
   marks=int(input("enter marks: "))
   if marks in range(91,101):
    print("grade=A")
   elif marks in range(81,91):
    print("grade=B")
   elif marks in range(71,81):
    print("grade=C")
   elif marks in range(51-71):
    print("grade=d")
   else:
    print("fail,study well")'''

#break-used to terminate th loop
#continue-used to skip the current iteration and rest of the code is continued
#pass-pass is a null statement it does nothing but syntaxically used-acts as placeholder

'''a=20
while a>5:
    print(a)
    a=a-1
    if a==10:
        break'''#20-11
'''a=30
while a>2:
    a=a-1
    if a==20:
        break
    print(a)'''#30-21

'''for i in range(40,65):
    if i=55:
        break
    print(i)'''#40-54

'''a="python"
if a=="h":
    break
print(a)'''#error

'''a="python"
for i in a:
    if i=="h":
        break
    print(i)'''#pyt

'''a=15
while a>3:
    print(a)
    a=a-1
    if a==11:
        continue'''#15-3
'''a=15
while a>3:
    a=a-1
    if a==11:
        continue
    print(a)'''#prints 15-3 but skips the 11

'''for i in range(18):
    if i==14:
        continue
    print(i)'''#skips the 14 continues the loop

'''a="python"
for i in a:
    if i=="h":
        continue
    print(i)'''#pyton(h is skipped)

'''a=20
while a>4:
    print(a)
    a=a-1
    if a==10:
        pass'''

for i in range(25):
  if i==10:
    pass
  print(i)
    
    








