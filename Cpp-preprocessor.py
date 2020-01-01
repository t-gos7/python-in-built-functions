'''
Functionality: Pyhton 3 program to remove comments from a C or C++ source code 
Author: Tarit Goswami
Date: Jan, 2020

Description:
------------
This is an implementation of C/C++ preprocessor to remove comments. First, the source code will be
splitted by '\n' (newline) and then the comments are removed. There can be two types of comments
(i) a line comment // 
(ii) multiline comment or block comment /* */ 

The first effective comment takes precedence over others: if the string // occurs in a block comment, 
it is ignored. Similarly, if the string /* occurs in a line or block comment, it is also ignored. 

Limitation: 
-----------
The program can't handle a source code which has double-quote(" ") in it. As python will be 
confused about where the source code ended. 
'''
