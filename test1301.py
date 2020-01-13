Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> int 1
SyntaxError: invalid syntax
>>> a = 5
>>> a
5
>>> a1 = 10
>>> a1
10
>>> a + a1
15
>>> a > a!
SyntaxError: invalid syntax
>>> a > a1
False
>>> b = 10
>>> a < b
True
>>> a,b,c=1,5,10
>>> a
1
>>> b
5
>>> c
10
>>> a, b, c = 5, 15, 20
>>> a
5
>>> b
15
>>> c
20
>>> a > b
False
>>> a > b or b > a
True
>>> a > b and b > a
False
>>> c > b and b > a
True
>>> sex = "man"
>>> sex = 'man"s
SyntaxError: EOL while scanning string literal
>>> sex = "man's"
>>> sex = '''man and girl
sda
ok
'''
>>> sex
'man and girl\nsda\nok\n'
>>> sex = "man and
SyntaxError: EOL while scanning string literal
>>> sex
'man and girl\nsda\nok\n'
>>> sex = '''1

2
3
23
23
23
214
12
4124
213
12
						   dsaasdsad
			***'''
>>> sex
'1\n\n2\n3\n23\n23\n23\n214\n12\n4124\n213\n12\n\t\t\t\t\t\t   dsaasdsad\n\t\t\t***'
>>> print(sex)
1

2
3
23
23
23
214
12
4124
213
12
						   dsaasdsad
			***
>>> sex = "man"
>>> sex === "man"
SyntaxError: invalid syntax
>>> sex == "man"
True
>>> sex = "mony"
>>> sex == "mony"
True
>>> "man" == "women"
False
>>> if sex == "man"
SyntaxError: invalid syntax
>>> if sex == "man" :
	print (you man)
	
SyntaxError: invalid syntax
>>> if sex == "man" :
	print ("man")

	
>>> type(10)
<class 'int'>
>>> type("cooke")
<class 'str'>
>>> type (10)
<class 'int'>
>>> type(10.1)
<class 'float'>
>>> type(10.1d)
SyntaxError: invalid syntax
>>> ein (1)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    ein (1)
NameError: name 'ein' is not defined
>>> ein = 1
>>> type (ein)
<class 'int'>
>>> zwei = "2"
>>> type (zwei)
<class 'str'>
>>> drei = 3.5
>>> type (drei)
<class 'float'>
>>> ein > zwei
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    ein > zwei
TypeError: '>' not supported between instances of 'int' and 'str'
>>> ein > drei
False
>>> eine < drei
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    eine < drei
NameError: name 'eine' is not defined
>>> ein < drei
True
>>> ein == drei
False
>>> ein = drei
>>> type (ein)
<class 'float'>
>>> ein = 1
>>> true
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    true
NameError: name 'true' is not defined
>>> True
True
>>> False
False
>>> 