nums = [2,2,1]
max = []
num = 0
for i in nums:
    if (i in max):
        max.remove(i)
        num -=i
    else:
        max.append(i)
        num+=i


print(max)
print(num)
    