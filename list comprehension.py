#list comprehension
'''a=["codegnan","python","course"]
b=str(a)
print(b.upper())'''

'''a=["codegnan","python","course"]
for i in a:
    print(i.upper(),end=" ")'''

'''a=["codegnan","python","course"]
b=[]
for i in a:
    b.append(i.upper())
print(b)'''
#syntax
#a=[expr for var in collection/range]
'''a=["codegnan","python","course"]
a=[i.upper() for i in a]
print(a)'''

'''a=["vja","hyd","viz"]
b=[i.title() for i in a]
print(b)'''#["Vja","Hyd","Viz"}

'''a=[1,2,3,5,6,8,12,13]
b=[i*i for i in a]
print(b)'''

'''a=[1,2,3,5,6,8,12,13]
b=[i**2 for i in a]
print(b)'''

'''a=[1,2,3,5,6,8,12,13]
b=[pow(i,2) for i in a]
print(b)'''#[1,4,9,25,36,64,144,169]

#if-usage in list comprehension
'''a=[i for i in range(16) if i%2==0]
print(a)'''#even numbers up to 16

'''a=[i for i in range(16) if i%2==0]
print(a)'''#even numbers up to 16

'''a=[i for i in range(31)]
print(a)'''# prints 0-30

'''fruits=["apple","banana","grapes","kiwi","mango","dragon","berry"]
a=[i for i in fruits if "a"in i]
print(a)'''

#no -elif usage in list comprehension

#if-else usage in list comprehension

'''a=[i**2 if i%2==0 else i*5 for i in range(21)]
print(a)'''#range(21)->even numbers->squares,range(21)->odd numbers->multiply '5'

'''a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=[a[i]+b[i] for i in range(len(a))]
print(c)'''#[6,6,6,6,6]

'''a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=[a[i]+b[i] for i in range(5)]
print(c)'''


#ATM Application
while True:
  account=100000
  pwd=1234
  card=input("insert the card: ")
  if card=="c":
    print("welcomr ranjith")
    password=int(input("enter the password: "))
    if password==pwd:
        option=int(input('''choose the option
                            1.balance enq
                            2.withdraw'''))
        if option==1:
            print("your account balance is",account)
        elif option==2:
            money=int(input("enter the amount: "))
            print(money)
            balance=account-money
            print("remaining account balance is",balance)
        else:
            print("invalid option")
    else:
        print("incorrect password")
  else:
    print("invalid card")
            








