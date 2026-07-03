Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]

a=[3,5.6,"python",9+7j,True,False]
print(a)
[3, 5.6, 'python', (9+7j), True, False]
type(a)
<class 'list'>
b=9
type(b)
<class 'int'>
c=[9]
type(c)
<class 'list'>
a=["python","java","c"]
a.append("javascript")
a
['python', 'java', 'c', 'javascript']
a.append("ai","ml")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.append("ai","ml")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["ai","ml"])
a
['python', 'java', 'c', 'javascript', ['ai', 'ml']]
#extend()
a=["java","html","css"]
a.extend(["js","c"])
a
['java', 'html', 'css', 'js', 'c']
#insert()
b=["apple","banana","mango"]
b.insert(1,"grapes")
b
['apple', 'grapes', 'banana', 'mango']
a=["kiwi","mango","apple","dragon","berry"]
#sort()
a.sort()
a
['apple', 'berry', 'dragon', 'kiwi', 'mango']
b=[9,5,7,0,3,4,10]
b.sort()
b
[0, 3, 4, 5, 7, 9, 10]
#reverse()
a=["c","java","html","css"]
a.reverse()
a
['css', 'html', 'java', 'c']
b=[12,23,54,43,21]
b.reverse()
b
[21, 43, 54, 23, 12]
>>> a=["black","white","orange","green","red"]
>>> #pop()
>>> a.pop()
'red'
>>> a
['black', 'white', 'orange', 'green']
>>> a.pop(2)
'orange'
>>> a
['black', 'white', 'green']
>>> #remove()
>>> a.remove()
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    a.remove()
TypeError: list.remove() takes exactly one argument (0 given)
>>> a.remove(1)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    a.remove(1)
ValueError: list.remove(x): x not in list
>>> a.remove("white")
>>> a
['black', 'green']
>>> a=["pooja","priya","sweety","cutie"]
>>> a.copy()
['pooja', 'priya', 'sweety', 'cutie']
>>> b=a.copy()
>>> b
['pooja', 'priya', 'sweety', 'cutie']
>>> a.clear()
>>> a
[]
>>> b=[]
>>> b.append("hi")
>>> b
['hi']
>>> a=["hi","hello","how"]
>>> len(a)
3
>>> b="hello"
>>> len(b)
5
>>> c=["hello"]
>>> len(c)
1
