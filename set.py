Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#tuple()
a=(4,5,6,"preeti",8+9j,True,False)
print(a)
(4, 5, 6, 'preeti', (8+9j), True, False)
type(a)
<class 'tuple'>
len(a)
7
a.index(8+9j)
4
a.count(True)
1
#sets()
a={3,6.7,"python",8+9j,True,False}
print(a)
{False, True, 'python', 3, (8+9j), 6.7}
type(a)
<class 'set'>
b={6,9,3,5,3,6,10,9,20}
print(a)
{False, True, 'python', 3, (8+9j), 6.7}
print(b)
{3, 20, 5, 6, 9, 10}
a={2,3,4,5,6,7,8,9}
b={6,7,8,9}
b.issubset(a)
True
a.issubset(a)
True
a.issubset(b)
False
a={4,5,6,7,8,9}
b={6,7,8,9}
a.issuperset(b)
True
#union()
a={1,2,3,4,5,6}
b={5,6,7,8,9,10}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
#intersection()
a={3,4,5,6,7,8,9}
b={7,8,9,10,11,12}
a.intersection(b)
{8, 9, 7}
a={10,11,12,13,14,15,16}
b={6,7,8,12,13,14,15,16,17}
a.difference(b)
{10, 11}
b.difference(a)
{8, 17, 6, 7}
a={2,3,4,5,6,7,8,9}
b={5,6,7,8,9,10,11}
a.symmetric_difference(b)
{2, 3, 4, 10, 11}
b.symmetric_difference(a)
{2, 3, 4, 10, 11}
a={1,2,3,4,5}
b={4,5,6,7,8}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8}
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8}
a={1,3,5,7,8,9,10}
b={2,4,6,7,10,11,12}
a.intersection_update(b)
a
{10, 7}
b.intersection_update(a)
b
{10, 7}
a={2,3,4,5,6,7,8}
b={1,5,6,7,8,9,10}
a.difference_update(b)
a
{2, 3, 4}
b.difference_update(a)
b
{1, 5, 6, 7, 8, 9, 10}
a={2,3,4,5,6,7,8,9}
b={5,6,7,8,9,10,11}
a.symmetric_difference_update(b)
a
{2, 3, 4, 10, 11}
b.symmetric_difference_update(a)
b
{2, 3, 4, 5, 6, 7, 8, 9}
a={3,4,5,6,7,8}
a.add(10)
a
{3, 4, 5, 6, 7, 8, 10}
a.copy()
{3, 4, 5, 6, 7, 8, 10}
b=a.copy()
b
{3, 4, 5, 6, 7, 8, 10}
a.clear()
a
set()
c=set()
>>> c.add(30)
>>> c
{30}
>>> a={5,6,7,8,9}
>>> a.pop()
5
>>> a.remove(7)
>>> a
{6, 8, 9}
>>> a={2,3,4,5,6}
>>> a.discard(4)
>>> a
{2, 3, 5, 6}
>>> b={4,5,6,7}
>>> c={8,9,10,11}
>>> b.isjoint(a)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    b.isjoint(a)
AttributeError: 'set' object has no attribute 'isjoint'. Did you mean: 'isdisjoint'?
>>> b.isdisjoint(a)
False
>>> b.isdisjoint(c)
True
>>> a={4,5,6,7,8}
>>> len(a)
5
>>> a=[9,1,5,2,8,4,6,3,,7,0]
SyntaxError: invalid syntax
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> first=a[:5]
>>> second=a[5:]
>>> first.sort()
>>> first.reverse()
>>> second.reverse()first.reverse()
SyntaxError: invalid syntax
>>> 
>>> first=a[:5]
>>> second=a[5:]
>>> first.sort()
>>> first.reverse()
>>> second.sort()
>>> second.reverse()
>>> result=second+first
>>> print(result)
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
