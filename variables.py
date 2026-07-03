Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#variables
print(3+8)
11
a=10
print(a)
10
b=20
print(b)
20
x=40
print(X)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined. Did you mean: 'x'?
print(x)
40
a3=80
print(a3)
80
b123=30
print(b123)
30
@=60
SyntaxError: invalid syntax
print(@)
SyntaxError: invalid syntax
_=50
print(_)
50
if=20
SyntaxError: invalid syntax
a=4;b=5
print(a+b)
9
a,b=2,3
print(a,b)
2 3
a=2,3,4
print(a)
(2, 3, 4)
a=b=c=10
print(a,b,c)
10 10 10
a,b,c=(2,3,4)
print(a,b,c)
2 3 4
first_name="ranjith"
print(first_name)
ranjith
firstname="ramu"
print(firstname)
ramu
fname="abhishekh"
lname="sharma"
print(fname+lname)
abhishekhsharma
print(fname+" "+lname)
abhishekh sharma
print(fname,lname)
abhishekh sharma
name="ishan"
print(name)
ishan
city="jharkhand"
print(city)
jharkhand
a=5
print(a)
5
del a
print(a)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined. Did you mean: 'a3'?
name="raju"
print(name)
raju
NAME="raju"
print("NAME")
NAME
print(NAME)
raju
#datatypes
a=10
type(a)
<class 'int'>
b=3.6
type(a)
<class 'int'>
type(b)
<class 'float'>
c="python"
type(c)
<class 'str'>
d="codegnan"
type(d)
<class 'str'>
e=5+9j
type(e)
<class 'complex'>
g=4j+7
type(g)
<class 'complex'>
h=3j
type(h)
<class 'complex'>
a=True
type(a)
<class 'bool'>
b=False
type(b)
<class 'bool'>
c="True"
type(c)
<class 'str'>
#datatype conversions
#int()
int(9)
9
int(8.9)
8
int("pooja")
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    int("pooja")
ValueError: invalid literal for int() with base 10: 'pooja'
int(6+9j)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    int(6+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#float
float(6)
6.0
float(3.4)
3.4
float("python")
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    float("python")
ValueError: could not convert string to float: 'python'
float(3+6j)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    float(3+6j)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> float(True)
1.0
>>> float(False)
0.0
>>> #str
>>> str(9)
'9'
>>> str(5.9)
'5.9'
>>> str("hi")
'hi'
>>> str(6+9j)
'(6+9j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> #complex
>>> complex(7)
(7+0j)
>>> complex(6.6)
(6.6+0j)
>>> complex("hello")
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    complex("hello")
ValueError: complex() arg is a malformed string
>>> complex(4+8j)
(4+8j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #bool
>>> bool(4)
True
>>> bool(6.8)
True
>>> bool("java")
True
>>> bool(7+9j)
True
>>> bool(True)
True
>>> bool(False)
False
