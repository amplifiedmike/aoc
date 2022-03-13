f = open("day2_1_data.txt")
horiz = 0
depth = 0
for line in f:
    a = line.split()
    a[1]=int(a[1].rstrip())
    if(a[0]=='forward'):
        horiz += a[1]
    elif(a[0]=='up'):
        depth -= a[1]
    elif(a[0]=='down'):
        depth += a[1]
    else:
        print('huh?')
        #nothing?

print(horiz)
print(depth)
mult = horiz*depth
print(mult)
