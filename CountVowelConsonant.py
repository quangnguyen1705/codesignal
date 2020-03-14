'''
Created on Mar 14, 2020

@author: fredericknguyen

test case 1 s: "a"=>1
test case 2 s: "abcde" =>8
s: "" =>0,
s: "oqaawtnkqo" => 16
s: "aiauaia" =>7

s: "dsnhpbpfkmqbclwy"=>32

s: "qrkwwqawbxgaasksrfpacpwhfobgfh"=>55

s: "fpwbqfvucwepocdapglyxwnqwlegsqxhxlfkmfaz"=>74
s: "teilziwavjyjykgccxkdzsalpkvnxoynpfpowgmhfvozwdbems"=> 91

'''

s ="abcde"
#26 chars
def countVowelConsonant(s):
    return len(s)*2-len(s.findall('[aeiou]',s))
#44 chars
#return sum(i in 'aeuio' or 2 for i in str(vars())) - 82

#45 chars
#return sum(2 - (s in "aeiou") for s in str(vars())) - 81

# 47
#return sum(e in "aeiou" or 2 for e in eval(dir()[0])[0])
countVowelConsonant(s)