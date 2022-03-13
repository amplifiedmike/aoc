def format_string(stringy):
    return int(str.rstrip(stringy))

f = open("day1_1_data.txt")

inc_cnt = 0 #increase counter
a=[]
asum=0
bsum=0

for line in f:
    if (len(a)<4): #load in 3 values to array
        a.append(format_string(line))
        print(a)
    else:
        asum = sum(a[0:3])
        bsum = sum(a[1:])
        if(bsum>asum):
            inc_cnt += 1
        a.append(format_string(line))
        a.pop(0)

asum = sum(a[0:3])
bsum = sum(a[1:])

if(bsum>asum):
    inc_cnt += 1    
        
print(inc_cnt)



