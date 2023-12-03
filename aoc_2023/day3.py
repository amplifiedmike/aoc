f = open("day3_1.txt", "r")
f2 = open("day3_test.txt","r")
f3 = open("day3_test2.txt","r")

def day3(file):
    #find location of symbols and string of numbers
    symbols = [] #[symbol,x,y]
    parts = [] #number, x,Ystart,Yend,addedToList]
    good_parts=[]
    temp_part=""
    for x,line in enumerate(file):
        for y,char in enumerate(line):
            #check for symbol
            if ((not char.isdigit()) and not char=="." and not char=="\n"):
                symbols.append([char,x,y])
                if(temp_part!=""):
                    parts.append([temp_part,x,y-len(temp_part),y-1,0])
                    temp_part=""
            elif(char.isdigit()):
                temp_part += char
            elif(char=="." and temp_part!=""):
                parts.append([temp_part,x,y-len(temp_part),y-1,0])
                temp_part=""
        parts.append([temp_part,x,y-len(temp_part),y-1,0])
        temp_part=""
    
    #make copies for part 2
    symbols_pt2 = symbols.copy()
    parts_pt2 = parts.copy()

    #part1 - check parts near symbols
    for symbol in symbols:
        x1 = symbol[1]-1
        x2 = x1+2
        y = symbol[2]
        for ind,part in enumerate(parts):
            #check x in range
            if x1<=part[1] and x2>=part[1]:
                #check y in range and not flagged yet
                if (part[4]==0) and (y>= (part[2]-1)) and (y<= (part[3]+1)):
                    good_parts.append(part)
                    parts[ind][4]=1
    good_parts_sum=0
    for good_part in good_parts:
        good_parts_sum+=int(good_part[0])

    #part2 - find gears, ratios, and add
    sum_gear_ratios = 0
    temp_gear_pairs = []
    for symbol in symbols_pt2:
        if symbol[0]=="*":
            x1 = symbol[1]-1
            x2 = x1+2
            y = symbol[2]
            for ind,part in enumerate(parts_pt2):
                #check x in range
                if x1<=part[1] and x2>=part[1]:
                    #check y in range
                    if (y>= (part[2]-1)) and (y<= (part[3]+1)):
                        temp_gear_pairs.append(part)
                        print(temp_gear_pairs)
        if len(temp_gear_pairs)==2:
            gear_ratio = int(temp_gear_pairs[0][0])*int(temp_gear_pairs[1][0])
            sum_gear_ratios += gear_ratio
        temp_gear_pairs = []

    print("\nsymbols" + "\n")
    print(symbols)

    print("\nparts" + "\n")
    for part in parts:
        print(part[0])

    print("\ngood parts" + "\n")
    #for part in good_parts:
    #    print(part[0])
    print(good_parts_sum)

    print("\nPart2")
    print(sum_gear_ratios)
    return

#day3(f3)
#day3(f2)
day3(f)