"""
HARDEST  HARDEST HARDEST!!!!!!!!!!!!!!
You are given a function . You are also given lists. The list consists of elements.
You have to pick one element from each list so that the value from the equation below is maximized:
%
denotes the element picked from the list . Find the maximized value obtained.
denotes the modulo operator.
Note that you need to take exactly one element from each list, not necessarily the largest element. You
add the squares of the chosen elements and perform the modulo operation. The maximum value that you
can obtain, will be the answer to the problem.
Input Format
The first line contains space separated integers and .
The next lines each contains an integer followed by space separated integers denoting the
elements in the list.
Constraints
Output Format
Output a single integer denoting the value .
Sample Input
3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10
Sample Output
206
Explanation
Picking from the list, from the list and from the list gives the maximum value equal to
% = .
"""
from itertools import product

K,M = map(int,input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(max(results))
"""N = (list(map(int, input().split()))[1:] for _ in range(K))

why do you use [1:] in the above line . why not (list(map(int, input().split())) for _ in range(K))

can you explain. please

4|Add CommentParentPermalink

soorajrajonline 2 years ago
"The next lines each contains an integer Ni followed by Ni space separated integers denoting the elements in the list."

So the first number is the number of numbers. We don't need that.

For example: 5 5 7 8 9 10

5 is how many numbers there are in the list (5,7,8,9,10)
"""