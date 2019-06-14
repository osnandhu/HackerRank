"""
Inbuilt string validators:
1. str.isalnum(): Return True ,if ALL CHARACTERS IN str belongs to alpha numericals (a-z)(A-Z)(0-9)
2. str.isupper(): True,if ALL CHARACTERS INstr is in caps
3. str.islower(): True, if ALL CHARACTERS INstr is in lowercase
4. str.isapha(): True if ALL CHARACTERS INstr is alphabet
5. str.isdigit(): True, if ALL CHARACTERS IN str is digit

TASK:
Input Format

A single line containing a string .

Constraints


Output Format

In the first line, print True if  has any alphanumeric characters. Otherwise, print False. 
In the second line, print True if  has any alphabetical characters. Otherwise, print False. 
In the third line, print True if  has any digits. Otherwise, print False. 
In the fourth line, print True if  has any lowercase characters. Otherwise, print False. 
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
"""
s = input("Enter a string")
# To evaluate whether any character of the string contains an uppercase/lowercase/etc- Note: any character of the string:
for test in ("isalnum","isalpha","isdigit","islower","isupper"):
    print(any(eval("c." + test + "()") for c in s ))

