#function ia a block of used to perform several operations.python is inbuilt function print,you can make your function also these are called user defined points
#function block begin with the keyword def and followed by the function name parentheis().
'''a=10
b=20
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)'''
'''a=100
b=200
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)'''
'''a=100
b=200
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)'''

'''def calculate(a,b):
    print("the sum is",a+b)
    print("the diff is",a-b)
    print("the product is",a*b)
calculate(10,20)
calculte(100,200)
calculate(1000,2000)'''

'''def calculate(a,b):
    print("the power is",a**b)
    print("the mod is",a%b)
    print("the division is",a//b)
calculate(3,4)
calculate(4,2)
calculate(12,2)'''

'''def add(a,b):
    print(a+b)
add(4,6)'''

'''def add():
    a=int(input("a value: "))
    b=int(input("b value: "))
    print(a+b)
add()'''
'''while True:
 def add():
    a=int(input("a value: "))
    b=int(input("b value: "))
    print(a+b)
 add()'''

'''def fullname():
    fname=input("first name: ")
    lname=input("last name: ")
    print((fname+" "+lname).title())
fullname()'''

#print and return
#print-print just shows human user input in the console
#return-return is used to terminate the function and gives back a value from the function

'''def mul(a,b):
    print(a*b)
mul(4,6)'''

'''def mul(a,b):
    return a*b
print(mul(7,3))'''

#print vs return
'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(2,3)'''
'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return c,d,e
print(cal(2,3))'''
#spilbill()
'''def spilbill():
    a=int(input("enter the total members: "))
    b=int(input("enter the total bill: "))
    print("per head bill is",b//a)
spilbill()'''
'''def spilbill():
    a=int(input("enter the total members: "))
    b=int(input("enter the total bill: "))
    c=b//a
    print("per head bill is {}".format(c))
    print(f"per head bill is {c}") 
spilbill()'''

'''def splitbill():
    a=int(input("enter the total numbers: "))
    b=int(input("enter the total bill: "))
    print("per head bill is {}".format(b//a))
    print(f"per head bill is {b//a}")
splitbill()'''

'''while True:
 def cal():
    a=int(input("a value: "))
    b=int(input("b value: "))
    option=int(input(choose the option
                        1.add
                        2.sub
                        3.mul))
    if option==1:
        print(a+b)
    elif option==2:
        print(a-b)
    else:
        print(a*b)
 cal()'''


'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a=int(input("a value: "))
    b=int(input("b value: "))
    option=int(input(choose the option
                        1 add
                        2 sub
                        3 mul))
    if option==1:
        add()
    elif option==2:
       sub()
    elif option==3:
        mul()'''

#keyword and positional arguements
'''def Details(id,name,mailid):
    id=10
    name="ranjith"
    mailid="ranjith@codegnan.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")'''

'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id=20,name="bhanu",mailid="b@gmail.com")
Details(id=30,name="nayana",mailid="n@gmail.com")
Details(40,"chetaan","c@gmail.com")
Details("h@gmail.com",50,"harika")'''

#default arguements
'''def Grocery(item,price):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("rice",1500)'''

'''def Grocery(item="sugar",price=1000):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery()'''

'''def Grocery(item,price=1000):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("dal")'''

'''def Grocery(item="ghee",price):
    #non default arguement follows def arg
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery(500)'''

#cake_name,price,quantity

'''def bakery(cake_name,price,quantity):
    print("cake_name is %s" %cake_name)
    print("price is %.2f" %price)
    print("quantity is %.2f" %quantity)
print("choclate cake",1500,1)'''

#* arguements(* is used to unpack elements)
'''a=[10,20,30,40,50]
print(a)
print(*a)'''#10 20 30 40 50
''''b=(5,6,7,8,9)
print(b)
print(*b)'''#5 6 7 8 9
'''c={2,3,4,5,6}
print(c)
print(*c)'''
'''d={"name":"ranjith","year":2026,"month":"july"}
print(d)
print(*d)'''#only keys name year month


'''a,b,c=1,2,3
print(a)
print(b)
print(c)'''
'''a,b,*c=2,3,4,5,6,7,8,9,10,11
print(a)
print(b)
print(*c)'''#2 and 3 for a,b and remaining without commas

'''a,b,c="codegnan"
print(a)
print(b)
print(c)'''
'''a,b,c="c","b","a"
print(a)
print(b)
print(c)'''
'''a,b,*c="codgnan"
print(a)
print(b)
print(*c)'''#c and o for a,b remaining without commas

#variable length arguements
#are automatically store in tuples and we use * arguements
'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7,8)
b=[2,3,4,5,6,7]
check(*b)
c={7,8,9,10}
check(*c)
d={"year":2026,"month":"july"}
print(*d)'''#every data type is store in tuple only

'''def check1(*a):
    d=1#creating a variable
    print(a)
    print(type(a))
    for i in a:
        d=d+i
        print(d)
check1()
check1(2,3,4,5,6)
check1(2,3,4,5,2.3,4.3)
check1(2,3,4,5,4.2,2.5,"rohit")'''

'''def check1(*a):
    d=1#creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
          d=d+i
          print(d)
check1()
check1(2,3,4,5,6)
check1(2,3,4,5,2.3,4.3)
check1(2,3,4,5,4.2,2.5,"rohit",5+9j,True,False)'''

#kwargs(**)
'''def details(**a):
    print(a)
    print(type(a))
details()
d={"names":["harsha","teja","hani"],
   "marks":[60,70,80],"status":["p","a","p"]}
details(**d )'''
    
'''def details(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
details()
d={"names":["harsha","teja","hani"],
   "marks":[60,70,80],"status":["p","a","p"]}
details(**d)'''
#both * and ** usage
def final(*a,**b):
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("key is",i)
        print("value is",j)
final()
data=[1,2,3,4,5.6,3.4]
final(*data)
d={"names":["harsha","teja","hani"],
   "marks":[60,70,80],"status":["p","a","p"]}
final(**d)
final(*data,**d)
















    






                        













