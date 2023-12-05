f = open("day5_1.txt", "r")
f2 = open("day5_test.txt","r")

def into_arrays(file):
    print('start')
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
    return seeds, table_array

def mapping(table):
    map = []
    for items in table:
        rangey = items[2]
        source = items[1]
        dest = items[0]
        for i in range(int(rangey)):
             map.append([int(source)+i,int(dest)+i])
    #print(map)
    return map
            
file = f
seeds, table_array = into_arrays(file)
seed_soil = mapping(table_array[0])
soil_fert = mapping(table_array[1])
fert_water = mapping(table_array[2])
water_light = mapping(table_array[3])
light_temp = mapping(table_array[4])
temp_humid = mapping(table_array[5])
humid_location = mapping(table_array[6])
full_map = [seed_soil,soil_fert,fert_water,water_light,light_temp,temp_humid,humid_location]

full_seed_map = []
for seed_ind,seed in enumerate(seeds):
    single_seed_map=[]
    single_seed_map.append(int(seeds[seed_ind]))
    for map_ind, map in enumerate(full_map):
        found_it_flag=0
        for element in map:
            source = element[0]
            dest = element[1]
            if single_seed_map[map_ind] == source:
                single_seed_map.append(dest)
                found_it_flag = 1
        if(found_it_flag == 0): single_seed_map.append(single_seed_map[map_ind])
        #print(single_seed_map)
    full_seed_map.append(single_seed_map) 
print(full_seed_map)        
#print(seeds)
#print(table_array[1])

lowest=10000000000000
for seeds in full_seed_map:
     if seeds[-1]<lowest:
          lowest = seeds[-1]

print(lowest)



