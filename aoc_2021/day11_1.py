def get_data(filename):
    data=[]
    f=open(filename)
    for line in f:
        data.append(list(line.rstrip()))
    return data

def step_increase_level(data):
    for y,row in enumerate(data):
        for x,col in enumerate(row):
            data[y][x]=data[y][x]+1
    return data

def flash_increase_level(data,increases):
    

def flash(data):
    flashes = []
    for nrow in range(10):
        flashes.append([])
        for ncol in range(10):
            flashes.append(0)

    for y,row in enumerate(data):
        for x,col in enumerate(row):
            if (data[y][x]>9):
                flashes[y][x] = 1
    
    for y,row in enumerate(data):
        for x,col in enumerate(row):
            



def step(data):
    #increase level
    data=step_increase_level(data)
    #flash if over 9, bring down to 0
    data = flash(data)

data=get_data("day11_test.txt")
print(data)
