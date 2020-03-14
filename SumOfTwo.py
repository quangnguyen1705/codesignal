'''
Created on Mar 14, 2020

@author: fredericknguyen

test case 1 a: [1, 2, 3]
            b: [10, 20, 30, 40]
            v: 42 => true
test case 2 a: [1, 2, 3]
            b: [10, 20, 30, 40]
            v: 50 => false
test case 3: a: []
b: [1, 2, 3, 4]
v: 4 => false
test case 4: a: [10, 1, 5, 3, 8]
b: [100, 6, 3, 1, 5]
v: 4=> true
test case 5: a: [1, 4, 3, 6, 10, 1, 0, 1, 6, 5]
b: [9, 5, 6, 9, 0, 1, 2, 1, 6, 10]
v: 8 => true
test case 6: a: [3, 2, 3, 7, 5, 0, 3, 0, 4, 2]
b: [6, 8, 2, 9, 7, 10, 3, 8, 6, 0]
v: 2 => true
test case 7:a: [4, 6, 4, 2, 9, 6, 6, 2, 9, 2]
b: [3, 4, 5, 1, 4, 10, 9, 9, 6, 4]
v: 5=> true
test case 8: a: [6, 10, 25, 13, 20, 21, 11, 10, 18, 21]
b: [21, 10, 6, 0, 29, 25, 1, 17, 19, 25]
v: 37 => true

test case 9:    a: [22, 26, 6, 22, 17, 11, 9, 22, 7, 12]
                b: [14, 25, 22, 27, 22, 30, 6, 26, 30, 27]
                v: 56 => true
test case 10:   a: [17, 72, 18, 72, 73, 15, 83, 90, 8, 18]
                b: [100, 27, 33, 51, 2, 71, 76, 19, 16, 43]
                v: 37 => true
test case 11 :  a: [75, 38, 10, 57, 67, 39, 26, 14, 53, 80]
                b: [3, 19, 28, 92, 92, 47, 98, 30, 71, 21]
                v: 61 = > true
test case 12 a: [1, 2, 3]
             b: []
             v: 1 => false
'''
#119
def sumOfTwo(a, b, v):
    t = set();
    for i in range(0,len(a),1):
        t.add(v-a[i])
    for j in range(0,len(b),1):
        if b[j] in t:
            return  True
    return False

#43
#sumOfTwo = lambda a, b, v: {*a} - {v-i for i in b} < {*a}

#sumOfTwo = lambda a, b, v: any({v-i for i in a} & {*b})