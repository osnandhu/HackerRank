"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.

Constraints

Output Format

Print the runner-up score.
"""
n = int(input())
arr = list(map(int, input().split()))
#print(arr)

list_sorted = []
for i in arr:
    if(i not in list_sorted):
        list_sorted.append(i)
list_sorted.sort(reverse = True)
print(list_sorted[1])
