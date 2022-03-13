def get_data(filename):
    f = open(filename)
    fish = f.readline().rstrip().split(",")
    fish = list(map(int,fish))
    #print(fish)
    return fish

def bin(fish,bin):
    for element in fish:
        bin[element]+=1
    return

def update(binn):
    fish0 = binn[0]
    binn.pop(0)
    binn.append(fish0)
    binn[6] += fish0
    #print(binn)
    return

bin_ls=[0,0,0,0,0,0,0,0,0]
fish = get_data('day6_test.txt')
fish = get_data('day6_data.txt')
#fish = sorted(fish)
print("fish start " + str(fish))

bin(fish,bin_ls)
print(bin_ls)
day = 0
while (day<80):
    update(bin_ls)
    day+=1
sum = sum(bin_ls)
print(sum)

