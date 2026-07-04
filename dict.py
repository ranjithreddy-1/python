Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dictionary()
a={"name":"ranjith","year":2026,"month":7}
print(a)
{'name': 'ranjith', 'year': 2026, 'month': 7}
type(a)
<class 'dict'>
b={"name","remo"}
type(b)
<class 'set'>
c={2027:7}
type(c)
<class 'dict'>
a={"year":2026,"month":"july","date":4}
a.update({"time":7}
         a
         
SyntaxError: '(' was never closed
a.update({"time":7})
         
a={"year":2026,"month":7,"date":4}
         
a.update({"time":7})
         
a
         
{'year': 2026, 'month': 7, 'date': 4, 'time': 7}
a.update({"name":"pooja"},{"city":"hyd"})
         
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a.update({"name":"pooja"},{"city":"hyd"})
TypeError: update expected at most 1 argument, got 2
a.update({"name":"pooja"})
         
a
         
{'year': 2026, 'month': 7, 'date': 4, 'time': 7, 'name': 'pooja'}
#setdefault()
         
a={"course":"python")
         
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
a={"course":"python"}
         
a.setdefault{"duration",4}
         
SyntaxError: invalid syntax
a.setdefault("duration",4)
         
4
a
         
{'course': 'python', 'duration': 4}
a={"color":"black","food":"biryani","icecream":"nuts"}
         
a["color"]
         
'black'
a.get("food")
         
'biryani'
a
         
{'color': 'black', 'food': 'biryani', 'icecream': 'nuts'}
a.get("biryani")
         
a
         
{'color': 'black', 'food': 'biryani', 'icecream': 'nuts'}
a={"month":7,"day":"sat","time":7}
         
a.keys()
         
dict_keys(['month', 'day', 'time'])
a.values()
         
dict_values([7, 'sat', 7])
a.items()
         
dict_items([('month', 7), ('day', 'sat'), ('time', 7)])
a={"city":"hyd","country":"india","state":"Telangana"}
         
a.pop()
         
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("city")
         
'hyd'
a
         
{'country': 'india', 'state': 'Telangana'}
a.popitem()
         
('state', 'Telangana')
a
         
{'country': 'india'}
a={"name":"rushi","mail":"rushi@codegnan.com"}
         
len(a)
         
2
a.copy()
         
{'name': 'rushi', 'mail': 'rushi@codegnan.com'}
a
         
{'name': 'rushi', 'mail': 'rushi@codegnan.com'}
a.clear()
         
a
         
{}
a={"name":"prajwal","year":2026,"name":"prajwal"}
         
print(a)
         
{'name': 'prajwal', 'year': 2026}
b={"name":"priya","year":2026,"name":"pranaya"}
         
b
         
{'name': 'pranaya', 'year': 2026}
a={"name1":"pooja","year":2026,"name2":"pooja"}
         
a
         
{'name1': 'pooja', 'year': 2026, 'name2': 'pooja'}
a={"idnos":[10,20,30],"name":["sweety","cutie","hearty"],"marks":[60,70,80]}
         
>>> a.keys()
...          
dict_keys(['idnos', 'name', 'marks'])
>>> a.values()
...          
dict_values([[10, 20, 30], ['sweety', 'cutie', 'hearty'], [60, 70, 80]])
>>> a.items()
...          
dict_items([('idnos', [10, 20, 30]), ('name', ['sweety', 'cutie', 'hearty']), ('marks', [60, 70, 80])])
>>> a={"year":2026,"month":7}
...          
>>> a.count("year")
...          
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    a.count("year")
AttributeError: 'dict' object has no attribute 'count'
>>> a.index("month")
...          
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a.index("month")
AttributeError: 'dict' object has no attribute 'index'
>>> a={"codegnan":"python","course"}
...          
SyntaxError: ':' expected after dictionary key
>>> a={"codegnan","python","course"}
...          
>>> #["CODEGNAN","PYTHON","COURSE"]
...          
>>> a=["codegnan","python","course"]
...          
>>> b=str(a)
...          
>>> b.upper()
...          
"['CODEGNAN', 'PYTHON', 'COURSE']"
>>> a=["codegnan","python","course"]
...          
>>> b=[]
...          
>>> b.append(a)
...          
>>> b
...          
[['codegnan', 'python', 'course']]
