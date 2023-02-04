celsius = 36.50

"""val =[]
val.append("%.5f" % (celsius+273.15))
val.append("%.5f" % ((celsius*1.80)+32.00))
print(val)"""

val = []
val.append((celsius+273.15))
val.append(((celsius*1.80)+32.00))
print(val)

#or 
print(f'[{(celsius+273.15)}, {((celsius*1.80)+32.00)}]')