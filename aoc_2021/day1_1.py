f = open("day1_1_data.txt")

inc_cnt = 0 #increase counter
first = int(str.strip(f.readline())) #strip newline chars from line

for line in f:
    second = line
    second = int(str.rstrip(second))
    if(second>first):
        inc_cnt+=1
    first = second
    
print(second) #make sure I got to the end of the file
print(inc_cnt)
