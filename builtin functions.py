#built-in functions
#print(dir())
#print(dir("___builtin___"))
'''a="codegnan"
print(a)

print(list(a))
print(tuple(a))
print(set(a))
#print(dict(a))

#fromkeys()
b=dict.fromkeys(a)
print(b)

c=dict.fromkeys(a,"pooja")
print(c)

c["d"]="sam"
print(c)'''
#eval()
'''while True:
   a=int(input("a value: "))
   b=int(input("b value: "))
   print(a+b)'''
'''while True:
   a=float(input("a value: "))
   b=floatt(input("b value: "))
   print(a+b)'''
'''while True:
   a=str(input("a value: "))
   b=str(input("b value: "))
   print(a+b)'''
'''while True:
   a=eval(input("a value: "))
   b=eval(input("b value: "))
   print(a+b)'''
#zip()-we can combine multiple collections into one collection
'''a=[10,20,30,40,50]
names=["teja","ram","tina","sony","abhi"]
print(a+names)

#b=zip(a,names)
#print(b)

c=list(zip(a,names))
print(c)
c=tuple(zip(a,names))
print(c)
c=set(zip(a,names))
print(c)
c=dict(zip(a,names))
print(c)'''

#enumerate()-we can give counter to the collection
'''names=["mythri","darshini","sarvani","srivarna","tejaswini"]
'for i in range(len(names)):
    print(i,names[i]'
b=dict(enumerate(names))
print(b)
b=dict(enumerate(names,100))
print(b)
c=set(enumerate(names))
print(c)
c=set(enumerate(names,10))
print(c)
d=list(enumerate(names))
print(d)
d=list(enumerate(names,20))
print(d)
e=tuple(enumerate(names))
print(e)
e=tuple(enumerate(names,50))
print(e)'''

#ASCII
#chr(),ord()
'''print(chr(65))
print(chr(90))
#print(chr("a"))-only int values is taken
print(chr(91))

#word()
print(ord("a"))
print(ord("z"))
#print(ord(56))-only str should be given'''
#print A-Z alphabets
'''for i in range(65,92):
    print(chr(i),end=" ")
for i in range(97,123):
    print(chr(i),end=" ")'''
'''name=input("enter name")
for i in name:
  print(i,ord(i))'''

#max(),min(),sum()

'''print(max(2,3,4,6,9,34,87,43))
print(min(89,66,44,7,2,67,89))
#print(sum(3,5))
a=2,3,4,5
print(sum(a)'''

#Marks Analysis Report
'''students=int(input("enter no of students: "))
marks=[]
for i in range(1,students+1):
    mark=int(input(f"enter the student {i} marks"))
    marks.append(mark)
for i in marks:
    print(i)
print("-------Marks Analysis Report----------")
print("total students",students)
print("highest marks",max(marks))
print("lowest marks",min(marks))
print("total marks",sum(marks))
print("average",sum(marks)/students)'''
#write a function to calculate 2*x+5 where x=5
'''def calc(x):
    print(2*x+5)
calc(5)'''
'''def f():
    x=int(input())
    print(2*x+5)
f()'''
#anonymous functions(nameless functions)
#anonymous functions are nameless functions and we use keyword called as lamda to create anynomous function
#syntax-->lambda arg:exp
'''a=lambda x:2*x+5
print(a(5))'''
'''a=int(input())
b=lambda x:2*x+5
print(b(a))'''
#take 2 arguements and multiply it
'''a=lambda x,y:x*y
print(a(2,4))
a=int(input())
b=int(input())
c=lambda a,b:a*b
print(c(a,b))'''

'''a="codegnan"
b=lambda a:a.upper()
print(b(a))
a=lambda a:a.upper()
print(a("codegnan"))'''

'''b="python course"
c=lambda a:a.title()
print(c(b))'''

#firstname+lastname=fullname
'''fname=input()
lname=input()
fullname=lambda fname,lname:(fname+" "+lname).title()
print(fullname(fname,lname))'''
'''fname,lname=[x for x in input("enter the names").split(",")]
fullname=lambda fname,lname:(fname+" "+lname).title()
print(fullname(fname,lname))'''

'''fname,lname=input().split(",")
fullname=lambda fname,lname:(fname+" "+lname).title()
print(fullname(fname,lname))'''

'''a=[10,20,23,25,67,45,80,90,97,85,100]
if a%2==0:
    print(a)'''
'''a=[10,20,23,25,67,45,80,90,97,85,100]
for i in a:
    if a%2==0:
        print(i)'''
'''a=[10,20,23,25,67,45,80,90,97,85,100]
b=list(filter(lambda x:x%2==0,a))
print(b)
a=[10,20,23,25,67,45,80,90,97,85,100]
b=list(filter(lambda x:x%2!=0,a))
print(b)'''

#[],(),{},set()
''''a=[]
print(type(a))
b=()
print(type(b))
c={}
print(type(c))
d=set()
print(type(d))'''

a=[[],(),set(),"",None,3,5.6,4+9j,"pooja",True,False]
b=list(filter(None(a)))
print(b)












    
