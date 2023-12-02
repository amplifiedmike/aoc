f = open("day2_1.txt", "r")
f2 = open("day2_test.txt","r")



def day2(line):
    #find game number
    space_ind=0
    char_game_number=""
    for index,char in enumerate(line):
        char_game_number= char_game_number+char
        if char==" ":
            space_ind = index
        if char==":":
            colon_ind=index
            game_num = line[space_ind:colon_ind]
            #print(game_num)
            break

    #find max red, green, blue
    lineSplit = line[colon_ind+1:].split()
    #print(lineSplit)
    red_max = 0
    green_max = 0
    blue_max = 0

    prev_element=""
    for element in lineSplit:
        if not(element.isdigit()):
            prev_element_int = int(prev_element)
            if element[:3]=='red':
                if prev_element_int > red_max:
                    red_max = prev_element_int
            elif element[:4]=='blue':
                if prev_element_int > blue_max:
                    blue_max = prev_element_int
            elif element[:5]=='green':
                if prev_element_int > green_max:
                    green_max = prev_element_int
        prev_element = element

    rgb_max = [red_max,green_max,blue_max]
    return game_num, rgb_max

MAXR = 12
MAXG = 13
MAXB = 14

testSUM=0 #part1
possible_games=[] #part1
powerSUM=0 #part2
for line in f2:
    game_num,rgb_max = day2(line)
    if ((rgb_max[0]<=MAXR) and (rgb_max[1]<=MAXG) and (rgb_max[2]<=MAXB)):
        testSUM= testSUM + int(game_num)
        possible_games.append(game_num)
    powerSUM=powerSUM + rgb_max[0]*rgb_max[1]*rgb_max[2]

print("Test Part 1")
print(testSUM) 
#print(possible_games)
print("\nTest Part 2")
print(powerSUM)


SUM=0 #part2
possible_games=[] #part1
powerSUM=0 #part2
possible_games=[]
for line in f:
    game_num,rgb_max = day2(line)
    if ((rgb_max[0]<=MAXR) and (rgb_max[1]<=MAXG) and (rgb_max[2]<=MAXB)):
        SUM= SUM + int(game_num)
        possible_games.append(game_num)
    powerSUM=powerSUM + rgb_max[0]*rgb_max[1]*rgb_max[2]
print("\nPart 1")
print(SUM) 
#print(possible_games)
print("\nPart 2")  
print(powerSUM)