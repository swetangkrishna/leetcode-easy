s = "luffy is still joydoy123   45  "
#t = s[::-1]

val = s.split(' ')
for i in range(len(val)):
    if val[len(val)-i-1]:
        print(len(val[len(val)-i-1]))
        break