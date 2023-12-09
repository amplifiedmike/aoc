f = open("day9_1.txt", "r")
f2 = open("day9_test.txt","r")

def diff_line(line):
    prev_num = line[0]
    diff=[]
    same_num = [0,'']
    for num in line[1:]:
        difference = num-prev_num
        diff.append(difference)
        prev_num=num
    prev_diff = diff[0]
    for num in diff[1:]:
        if prev_diff != num:
            same_num[0] = 0
            break
        same_num[0] = 1
        same_num[1] = num
    print(diff)
    return same_num,diff

def complete_line(line_array):
    last_element = line_array[-1][-1]
    new_line_array=[]
    for line in reversed(line_array[:-1]):
        line.append(line[-1]+last_element)
        last_element = line[-1]
        new_line_array.append(line)
    print('new line array')
    print(new_line_array)
    return new_line_array

def complete_line_backwards(line_array):
    print(line_array)
    for line in line_array:
        line = line.reverse()
    print(line_array)
    last_element = line_array[-1][-1]
    new_line_array=[]
    for line in reversed(line_array[:-1]):
        line.append(line[-1]-last_element)
        last_element = line[-1]
        new_line_array.append(line)
    print('new line array')
    print(new_line_array)
    return new_line_array

def day9(line):
    print('start')
    line = line.split()
    line_int=[]
    for i in line:
        line_int.append(int(i))
    print('start line')
    print(line_int)
    same_num,diff_temp=diff_line(line_int)
    diffs = []
    diffs.append(diff_temp)
    same_nums = []
    same_nums.append(same_num)
    ind = 0
    while not same_num[0]:
        #print(ind)
        #print(diffs)
        same_num,diff_temp = diff_line(diffs[ind])
        diffs.append(diff_temp)
        same_nums.append(same_num)
        ind += 1
    line_to_complete = []
    line_to_complete.append(line_int)
    for line in diffs:
        line_to_complete.append(line)
    #print(line_to_complete)
    #ans = complete_line(line_to_complete)
    #print('end line')
    #print(ans)

    print('line to complete backwards')
    ans = complete_line_backwards(line_to_complete)
    print(ans)
    print('\n')
    return ans

file = f
sum = 0
for line in file:
    print('next line\n')
    ans = day9(line)
    sum += ans[-1][-1]
print('sum: ')
print(sum)
