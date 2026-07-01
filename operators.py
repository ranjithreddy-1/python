Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#arithmetic
a=2
b=4
print(a+b)
6
print(a-b)
-2
print(a*b)
8
print(a//b)
0
print(a/b)
0.5
print(a**b)
16
#assignment
a=3
b=5
print(a+=b)
SyntaxError: invalid syntax
a+b
8
a+=b
a
8
a-=2
a
6
a//=2
a
3
a/=2
a
1.5
a*=3
a
4.5
a%=6
a
4.5
a**=4
a
410.0625
#comparision
a=4
b=8
a<b
True
b>a
True
a>b
False
b<a
False
a=8
b=8
a==b
True
a!=b
False
#logical
a=5
b=7
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a<b or b>a
True
a>=b or a<=b
True
a!=b or a==b
True
not True
False
not False
True
#identify
a=4
type(a) is int
True
type(a) is not int
False
a=5.6
type(a) is float
True
type(a) is not float
False
#membership
a=3,4,5,6,7,8,9,10
8 in a
True
20 in a
False
20 not in a
True
#bitwise
a=2
b=4
a&b
0
a=5
b=7
a&b
5
bin(2)
'0b10'
bin(4)
'0b100'
bin(5)
'0b101'
bin(7)
'0b111'
a=3
b=5
a|b
7
>>> a=4
>>> b=8
>>> a|b
12
>>> a=2
>>> -(a+1)
-3
>>> ~a
-3
>>> a=5
>>> ~a
-6
>>> a=9
>>> ~a
-10
>>> b=-11
>>> ~b
10
>>> c=-15
>>> ~c
14
>>> a=6
>>> b=9
>>> a^b
15
>>> a=5
>>> b=7
>>> a^b
2
>>> a=3
>>> a<<2
12
>>> bin(3)
'0b11'
>>> a=5
>>> a<<3
40
>>> a=4
>>> a>>2
1
>>> bin(4)
'0b100'
>>> a=9
>>> a>>3
1
