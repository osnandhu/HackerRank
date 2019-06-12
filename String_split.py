"""
1. s.split(" ") -> split when you come across a blank space, returns a list of strings
2. "-".join(s) -> join the words of the string with "-": Note: input: list of strings


Task:
Task 
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Input Format 
The first line contains a string consisting of space separated words.

Output Format 
Print the formatted string as explained above.

Sample Input

this is a string   
Sample Output

this-is-a-string
"""
def split_and_join(line):
    a = line.split(" ")
    a = "-".join(a)
    return(a)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
