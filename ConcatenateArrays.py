'''
Created on Mar 14, 2020

@author: fredericknguyen
a: [2, 2, 1]
b: [10, 11]
Expected Output:
[2, 2, 1, 10, 11]

a: [1, 2]
b: [3, 1, 2]
Expected Output:
[1, 2, 3, 1, 2]


a: [1]
b: []
Expected Output:
[1]

a: [2, 10, 3, 9, 5, 11, 11]
b: [4, 8, 1, 13, 3, 1, 14]
Expected Output:
[2, 10, 3, 9, 5, 11, 11, 4, 8, 1, 13, 3, 1, 14]


a: [9, 6, 6, 9, 8, 14]
b: [3, 2, 2, 5, 3, 11, 12, 9, 7, 7]
Expected Output:
[9, 6, 6, 9, 8, 14, 3, 2, 2, 5, 3, 11, 12, 9, 7, 7]
'''

#26 chars
a,b = eval(dir()[0])
return a + b

