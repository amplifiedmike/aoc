f = open("day7_1.txt", "r")
f2 = open("day7_test.txt","r")

def day7(file):
    print('start')
    fives = []
    fours = []
    full = []
    threes = []
    two_pair = []
    one_pair = []
    high = []

    for ind,line in enumerate(file):
        line = line.replace('A','E')
        line = line.replace('T','A')
        line = line.replace('J','B')
        line = line.replace('Q','C')
        line = line.replace('K','D')
        lineSplit = line.split()
        hand = lineSplit[0]
        bid = lineSplit[1]
        hand_char = sorted([i for i in hand])
        histogram=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for char in hand_char:
            if char.isdigit(): histogram[int(char)-1] += 1
            elif char == 'A': histogram[9] += 1
            elif char == 'B': histogram[10] += 1
            elif char == 'C': histogram[11] += 1
            elif char == 'D': histogram[12] += 1
            elif char == 'E': histogram[13] += 1
            else: print("how did you get here?")
        sorted_histo = sorted(histogram,reverse=True)
        for hist_ind,num in enumerate(sorted_histo):
            if num == 5: #five of a kind
                fives.append([ind,lineSplit])
                break
            elif num == 4: #four of a kind
                fours.append([ind,lineSplit])
                break
            elif num == 3: #three of a kind or full house
                if sorted_histo[hist_ind+1] == 2: #full house
                    full.append([ind,lineSplit])
                    break
                else:
                    threes.append([ind,lineSplit]) #three of a kind
                    break
            elif num == 2: #two pair or one pair
                if sorted_histo[hist_ind+1] == 2: #two pair  
                    two_pair.append([ind,lineSplit])
                    break
                else:
                    one_pair.append([ind,lineSplit])
                    break
            else:
                high.append([ind,lineSplit])
                break

    fives_sorted = fives.sort(reverse=True) 
    print(fives_sorted)           
                

        
    print(hand_char)
    print(bid)
        



day7(f2)