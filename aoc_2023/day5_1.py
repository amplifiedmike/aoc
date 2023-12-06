import time
f = open("day5_1.txt", "r")
f2 = open("day5_test.txt","r")


def into_arrays(file):
    #put values into arrays first
    first_line_flag = 1
    #first line is seeds
    seeds=[]
    lineSplit = file.readline().split()
    for seed in lineSplit[1:]:
                seeds.append(seed)

    array_names = ["seed-to-soil", "soil-to-fertilizer","fertilizer-to-water","water-to-light","light-to-temperature","temperature-to-humidity","humidity-to-location"]
    table_array=[[],[],[],[],[],[],[]]
    array_ind = 0
    for line in file:
        lineSplit = line.split()
        if line == "\n":
            #do nothing
            pass
        elif lineSplit[0].isdigit():
            temp_table=[]
            for num in lineSplit:
                temp_table.append(num)
            table_array[array_ind].append(temp_table) 
        else:
            for ind,names in enumerate(array_names):
                if lineSplit[0] == names:
                    array_ind = ind
                    break
    #for i in range(7):
    #    print(table_array[i])

    #table_array = [dest source range]
    return seeds, table_array

def day5(seeds,table_array):
    full_seed_map = []
    for seed_ind,seed in enumerate(seeds):
        single_seed_map=[]
        single_seed_map.append(int(seeds[seed_ind]))
        for map_ind, map in enumerate(table_array):
            found_it_flag=0
            start = single_seed_map[map_ind]
            for element in map:
                source = int(element[1])
                dest = int(element[0])
                range = int(element[2])
                #in range of element's condition?
                if (start >= source) and (start<= source + range):
                    end = start+ (dest - source)
                    single_seed_map.append(end)
                    found_it_flag = 1
                    break
            if(found_it_flag == 0): single_seed_map.append(start)
            #print(single_seed_map)
        full_seed_map.append(single_seed_map) 
    #print(full_seed_map)        
    #print(seeds)
    #print(table_array[1])

    lowest=10000000000000
    for seeds in full_seed_map:
        if seeds[-1]<lowest:
            lowest = seeds[-1]

    print(lowest)     

file = f
t0 = time.perf_counter()
seeds, table_array = into_arrays(file)
#part1
day5(seeds,table_array)
#part2
t1 = time.perf_counter()
print("time for part 1: " + str(t1-t0))

lowest = int(table_array[6][0][0])
print(lowest)
lowest_line = []
for ind,line in enumerate(table_array[6]):
     if int(line[0])<lowest: 
        lowest = int(line[0])
        lowest_line = line
new_ranges = [[],[],[],[],[],[],[]]
new_ranges[6].append(lowest_line[0])
new_ranges[6].append(lowest_line[1])
new_ranges[6].append(lowest_line[2])
print(new_ranges)

for i in range(5,-1,-1):
    for line in table_array[i]:
        range = new_ranges[i+1]
        
        map_dest = line[0]
        map_src = line[1]
        map_range = line[2]
        map_big = map_dest+map_range
        map_small = map_dest

        new_range_src = range[1]
        new_range_range = range[2]
        new_range_big = new_range_src+new_range_range
        new_range_small = new_range_src
        
        if (map_big<new_range_small) or (map_small>new_range_big):
            pass
        else:
            new_ranges[i].append(line)

print(new_ranges)

        



