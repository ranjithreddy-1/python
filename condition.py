#conditions
#if-condition by using comparision operators
#<,>,<=,>=,!=,==

'''a=2
b=4
if a<b:
    print("true")'''

'''a=2
b=4
if a>b:
    print("true")'''

'''a=12
b=14
if a<=b:
    print("true")'''

'''a=20
b=40
if b>=a:
    print("true")'''

'''a=7
b=9
if a!=b:
    print("not equal")'''

'''a=2
b=10
if a==b:
    print("equal")'''

'''a=8
b=8
if a==b:
    print("true")'''

'''a=int(input("a value"))
b=int(input("b value"))
if a<b:
    print("less")'''

'''a=int(input("a value"))
if a<10:
    print("less")'''

'''a="python"
if a=="java"
    print("true")'''

'''a=input("data")
if a=="java":
    print("true")'''

#if condition by using logical operators
#and,or,not

'''a=4
b=9
if a<b and b>a:
    print("less")'''

'''a=4
b=9
if a<=b and b>=a:
    print("less")'''

'''a=4
b=9
if a!=b and a==b:
    print("less")'''

'''a=4
b=9
if a==b and a!==b:
    print("less")'''

'''a=4
b=9
if a<b or b>a:
    print("less")'''

'''a=4
b=9
if a<=b or b>==a:
    print("less")'''

'''a=4
b=9
if a!==b or a==b:
    print("less")'''

'''a=4
b=9
if a==b or a!==b:
    print("less")'''

'''a=13
b=15
if not a<b or b>a:
    print("less")'''

'''a=13
b=15
if not a<b and b>a:
    print("less")'''

'''a=13
b=15
if not a<b:
    print("less")'''

'''a=13
b=15
if not a>b:
    print("less")'''

'''a=int(input())
b=int(input())
if a<b amd b>a:
    print("less")'''

#if condition by using identify operators
#is,is not

'''a=5
if type(a) is int:
    print("it is int")'''

'''a=6
if type(a) is not int:
    print("false")'''

'''a=int(input("a value"))
if type(a) is int:
    print("it is int")'''

'''a=3.14
if type(a) is float:
    print("it is float")'''

'''a=3.14
if type(a) is not float:
    print("false")'''

'''a=float(input("a value"))
if type(a) is float:
    print("it is float")'''

'''a="python"
if type(a) is str:
    print("it is str")'''

'''a="python"
if type(a) is not str:
    print("false")'''

'''a=input("enter a")
if type(a) is str:
    print("it is str")'''

#if-condition by using membership operator

'''a=2,3,4,5,6,7,8,9,10
if 10 in a:
    print("true")'''

'''a=2,3,4,5,6,7,8,9,20
if 20 in a :
    print("true")'''

'''a=2,3,4,5,6,7,8,9,10
if 20 not in a:
    print("true")'''

'''a=int(input("enter the value"))
if 30 in a:
    print("true")'''#error

'''a=2,3,4,5,6,7,8,9,10
a=int(input("a value"))
if b in a :
    print("true")'''

#if-else condition using comparision operators
'''a=3
b=6
if a<b:
    print("true")
else:
    print("false")'''

'''a=3
b=6
if a>b:
    print("true")
else:
    print("false")'''

'''a=3
b=6
if a!=b:
    print("not equal")
else:
    print("true")'''

#if-else condition by using logical operator
'''a=5
b=10
if a<b and b>a:
    print("less")
else:
    print("true")'''

'''a=5
b=10
if a<b or b>a:
    print("less")
else:
    print("true")'''

'''a=5
b=10
if not a<b and b>a:
    print("less")
print("true")'''

#if-else condition using identify operator
'''a=5
if type(a) is int:
    print("true")
else:
    print("false")'''

'''a=4.8
if type(a) is not int:
    print("true")
else:
    print("false")'''

'''a="messi"
if type(a) is str:
    print("it is str")
else:
    print("false")'''

#if-else condition using membership operator
'''a=2,3,4,5,6,7,8,9
if 2 in (a):
    print("true")
else:
    print("false")'''

'''a=2,3,4,5,6,7,8,9
if 1 not in(a):
    print("false")
    
else:
    print("true")'''

#if-elif-else condition by using comparision operator
'''a=8
b=10
if a<b:
    print("less")
elif:
    print("greater")
else:
    print("true")'''

'''a=8
b=10
if a==b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")'''

'''a=13
b=16
if a>b:
    print("less")
elif:
    print("greater")
elif a!=b:
    print("not equal")
else:
    print("true")'''

#if-elif-else condition by using logical operator
'''a=5
b=8
if a<b and b>a:
    print("less")
elif a>b:
    print("high")
else:
    print("true")'''

'''a=5
b=8
if a<b or b>a:
    print("less")
elif a==b:
    print("equal")
else:
    print("true")'''

'''a=5
b=8
if not a>b and b<a:
    print("less")
elif b>a:
    print("high")
else:
    print("true")'''

#if-elif-else condition using by identify operator

'''a=4
if type(a) is int:
    print("int")
elif type(a) is str:
    print("str")
else:
    print("true")'''

'''a=5.9
if type(a) is not int:
    print("true")
if type(a) is not float:
    print("true")
else:
    print("true")'''


#multiple-if condition
'''a=20
b=40
if a<b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print("not equal")'''


'''a=20
b=40
if a<b:
    print("less")
elif b>a:
    print("greater")
else a!=b:
    print("not equal")'''

#logical operator
'''a=20
b=40
if a<b and b>a:
    print("less")
if a>b and b<a:
    print("high")
if a!=b:
    print("not equal")'''

'''a=20
b=40
if a<b or b>a:
    print("less")
if a>b or b<a:
    print("high")
if a!=b:
    print("true")'''

'''a=20
b=40
if not a<b and b>a:
    print("less")
if a>b and b<a:
    print("high")
if a==b:
    print("true")'''

#nested-if
'''a=4
b=6
if a<b:
    print("less")
    if b>a:
        print("greater")'''#2 conditions execute

'''a=4
b=6
if a>b:
    print("high")
    if a<b:
        print("low")'''# if the first if condition is false then it ignores second and print empty

'''a=15
b=17
if a>b:
    print("less")
    if b>a:
        print("greater")
else:
    print("true")'''#only the else will executes ,the if condition is wrong

'''a=4
b=6
if a<b:
    print("less")
    if b==a:
        print("greater")
    else:
        print("true")'''

'''a=9
b=11
if a<b:
    print("less")
    if b>a:
        print("greater")
    else:
        print("true")
else:
    print("false")'''

a=4
b=6
if a<b:
    print("less")
    if b==a:
        print("greater")
    elif a>=b:
        print("not equal")
    else:
        print("equal")
         

    
    
    


    























    


    


