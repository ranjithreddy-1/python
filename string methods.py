Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #string methods
>>> #len()
>>> a="python"
>>> len(a)
6
>>> b="python course"
>>> len(b)
13
>>> c=""
>>> len(c)
0
>>> d=" "
>>> len(d)
1
>>> #count
>>> a="twinkle twinkle little star"
>>> a.count("twinkle")
2
>>> a.count("t")
5
>>> a.count("k")
2
>>> a.count(" ")
3
>>> #find a string
>>> a="python"
>>> a[2]
't'
>>> a.find("t")
2
>>> a.find("n")
5
>>> b="hello"
>>> b.find("l")
2
>>> b[2:4]
'll'
>>> a.find("m")
-1
>>> #escape sequences
>>> #\n->new line
>>> #\t->tab space
>>> a="name\nmobileno\tmailid\ncollege\tbranch"
>>> print(a)
name
mobileno	mailid
college	branch
b="name:ranjith\nmobileno:1232345632\tmailid:ranjith@codegnan.com\ncollege:xyz\nbranch:cse"
print(a)
name
mobileno	mailid
college	branch
print(b)
name:ranjith
mobileno:1232345632	mailid:ranjith@codegnan.com
college:xyz
branch:cse
#replace()
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
b="i love java"
b.replace("java","python")
'i love python'
#upper
a="hello"
a.upper()
'HELLO'
#lower()
b="HI"
b.lower()
'hi'
c="python"
c.upper()
'PYTHON'
c[0].upper()
'P'
c.capitalize()
'Python'
d="python course"
d.title()
'Python Course'
e="i am in class"
e.capitalize()
'I am in class'
e.title()
'I Am In Class'
a="python"
a.isupper()
False
a.islower()
True
a.isalpha()
True
b="python course"
b.isalpha()
False
d=1234
d.isdigit()
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    d.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
e="1234"
e.isdigit()
True
f="ranjith"
f.isalnum()
True
g="ranjith1234"
g,isalnum()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    g,isalnum()
NameError: name 'isalnum' is not defined
g.isalnum()
True
a="java"
a.startswith("j")
True
a.endswith("a")
True
#strip()
#lsstrip(),rsstrip()
a="       ranjith       "
a.strip()
'ranjith'
a.lsstrip()
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    a.lsstrip()
AttributeError: 'str' object has no attribute 'lsstrip'. Did you mean: 'lstrip'?
a.lstrip()
'ranjith       '
a.rstrip()
'       ranjith'
#split()
a="python java c css html"
a.split()
['python', 'java', 'c', 'css', 'html']
b="i am in class room"
b.split()
['i', 'am', 'in', 'class', 'room']
#join()
b="vja","viz","hyd"
"".join(b)
'vjavizhyd'
" ",join(b)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    " ",join(b)
NameError: name 'join' is not defined
" ".join(b)
'vja viz hyd'
"k",join(b)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    "k",join(b)
NameError: name 'join' is not defined
"k".join(b)
'vjakvizkhyd'
c="python"
"k".join(b)
'vjakvizkhyd'
"k".join(c)
'pkyktkhkokn'
