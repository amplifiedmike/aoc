def get_data(filename):
    f = open(filename)
    listy=[]
    code=[]
    for line in f:
        line = line.split("| ")
        code.append(line[0][:-1])
        listy.append(line[1].replace("\n",""))
    for idx,element in enumerate(code):
        code[idx] = element.split(" ")
    for idx,row in enumerate(code):
        code[idx] = sorted(code[idx],key=len)
        for index,word in enumerate(row):
            code[idx][index] = sorted(code[idx][index])
    return code, listy
    
def decode(code):
    #    0
    #  1   2
    #    3
    #  4   5
    #    6
    #line: sorted by length
    sevseg = ["", "", "", "", "","", ""]
    nums= ["", "", "", "", "","", "","","",""]
    nums[1] = code[0]
    nums[7] = code[1]
    nums[4] = code[2]
    nums[6] = code[8]
    nums[8] = code[9]
    code_rm=[code[3],code[4],code[5],code[6],code[7]]
    print(code_rm)
    #9 has more one seg than 4
    for word in code_rm:
        for letters in word:
            if(nums[4][0] != letters):
                if(nums[4][1] != letters):
                    break
            nums[9] = word
    code_rm.remove(nums[9])
    print(code_rm)

    #3 has more one seg than 9
    for word in code_rm:
        for letters in word:
            if(nums[4][0] != letters):
                if(nums[4][1] != letters):
                    break
            nums[9] = word
    code_rm.remove(nums[9])
    print(code_rm)
    
        
    #for letter in nums[]
    #sevseg[0] = 
    
    return


code, output = get_data('day8_test.txt')
#code, output = get_data('day8_data.txt')
print(code[0])
#for line in code:
decode(code[0])
