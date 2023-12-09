f = open("day8_1.txt", "r")
f2 = open("day8_test.txt","r")

dir_dict = {}
def day8(file):
    inst = file.readline()
    #change LR to 0 and 1
    inst = inst.replace('L','0')
    inst = inst.replace('R','1')
    inst = inst[:-1]
    file.readline()
    
    #put all elements into dict
    for line in file:
        lineSplit = line.split()
        dir_dict[lineSplit[0]] = [lineSplit[2][1:4],lineSplit[3][0:3]]
    
    node = 'AAA'
    last_node = 'ZZZ'
    
    print("first node, last node: ")
    print(node)
    print(last_node)
    print("\n")
    
    # part 1 - parse through instructions
    count = 0
    
    while node != last_node:
        for directions in inst:
            LR = int(directions)
            #print('start node and dir: ')
            #print(node)
            #print(LR)
            node = dir_dict[node][LR]
            #print('next node: ')
            #print(node)
            #print("\n")
            count += 1
                 
    print(node)
    print(count)

    #part2
    
        

day8(f)