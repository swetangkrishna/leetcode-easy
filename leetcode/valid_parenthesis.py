s = "({[})"

dic = {
    ')':'(',
    '}':'{',
    ']':'['
}
val = []

for i in s:
    if i in dic:
        if val and val[-1] == dic[i]:
            val.pop()
        else:
            print('false')
            break
    else:
        val.append(i)
if not val:
    print('true')

    
    
