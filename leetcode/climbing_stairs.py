"""from itertools import repeat
from itertools import permutations
n = 35
i = n
j = 0
count = 0
val = []

while(i>=0):
    n = n-(i)-(2*j)
    val.extend(repeat(1, i))
    val.extend(repeat(2, j))
    count += len(list(set(permutations(val))))
    val =[]
    i -= 2
    j += 1
    n = n+(i)+(j)
print(count)"""
n = 3
one = 1
two = 1
for i in range(n-1):
    temp = one
    one = one + two
    two = temp
    
print(one)



    