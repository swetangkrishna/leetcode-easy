n = 5
val = [[1]]

for j in range(n-1):
    temp = [0] + val[-1] + [0]
    list = []
    for i in range(len(val[-1])+1):
        list.append(temp[i]+temp[i+1])
    val.append(list)

print(val)