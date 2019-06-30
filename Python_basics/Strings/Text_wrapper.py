"""
import textwrap:
1. textwrap.wrap() 
The wrap() function wraps a single paragraph in text (a string) so that every line is width characters long at most. 
It returns a list of output lines.
>>> import textwrap
>>> string = "This is a very very very very very long string."
>>> print textwrap.wrap(string,8)
['This is', 'a very', 'very', 'very', 'very', 'very', 'long', 'string.'] 
textwrap.fill() 
The fill() function wraps a single paragraph in text and returns a single string containing the wrapped paragraph.

>>> import textwrap
>>> string = "This is a very very very very very long string."
>>> print textwrap.fill(string,8)
This is
a very
very
very
very
very
long
string.

TASK:
You are given a string  and width . 
Your task is to wrap the string into a paragraph of width .

Input Format

The first line contains a string, . 
The second line contains the width, .

Constraints

Output Format

Print the text wrapped paragraph.

Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ



"""
import textwrap

def wrap(string, max_width):
    result = textwrap.fill(string,max_width)
    return result

if __name__ == '__main__':
    string, max_width = "ABCDEFGHIJKLIMNOQRSTUVWXYZ",4
    result = wrap(string, max_width)
    print(result) 