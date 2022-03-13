def find_common(oxy,listy,bit_pos):
    list_len = len(listy)
    list_sum = 0
    for element in listy:
        #print(element)
        #print(element[bit_pos])
        list_sum += int(element[bit_pos])
    common = list_sum/list_len
    #print(common)
    if common >0.5: common_f = 1
    elif common <0.5: common_f = 0
    elif common == 0.5: common_f = 1
    
    if(not oxy):
        if common_f == 1: common_f=0
        else: common_f=1
    #print(common_f)
    return common_f

def make_new_list(oxy,listy,bit_pos):
    new_list=[]
    common = find_common(oxy,listy,bit_pos)
    print('common is '+str(common))
    for element in listy:
        if element[bit_pos] == str(common): new_list.append(element)
    return(new_list)

test_list = ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']
numbers = []
numbers_c = []
numbers_m = []
test_list2 = test_list.copy()

f = open("day3_1_data.txt")
for line in f:
    numbers.append(line.rstrip())

numbers_o = numbers.copy()
numbers_c = numbers.copy()

#O2
index = 0
while(len(numbers_o)>1):
    numbers_o = make_new_list(True,numbers_o,index)
    index +=1
    #print(index)
    #print(numbers)
    #print(numbers[0])
o2 = '0b' + numbers_o[0]
#print(int(o2,2))
print('O2 level is '+ str(int(o2,2)))

#CO2
index = 0
#print(numbers_c)
while(len(numbers_c)>1):
    numbers_c = make_new_list(False,numbers_c,index)
    index +=1
    #print(index)
    print(numbers_c)
    #print(numbers[0])
co2 = '0b' + numbers_c[0]
print(int(o2,2))
print('CO2 level is '+ str(int(co2,2)))
print('life support is '+ str(int(o2,2)*int(co2,2)))



