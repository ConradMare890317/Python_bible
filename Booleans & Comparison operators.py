Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> B = True
>>> C = False
>>> D = true
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    D = true
NameError: name 'true' is not defined
>>> D = True
>>> E = "True"
>>> type(E)
<class 'str'>
>>> type(B)
<class 'bool'>
>>> 2 > 3
False
>>> 2 < 3
True
>>> type(2<3)
<class 'bool'>
>>> 2 == 3
False
>>> 3 == 3
True
>>> 4 >= 3
True
>>> >, <, ==, !=, <=, >=