def get_data(filename):

    f = open(filename)
    data=[]
    for row in f:
        data.append(row.rstrip())
    for idx,line in enumerate(data):
        data[idx] = list(line)
    return data

def get_neighbors(point,lenx,leny):
    listy=[]
    print('lenx: ')
    print(lenx)
    print('leny: ')
    print(leny)
    #x+1
    np1 = [point[0],point[1]+1]
    #print(np1)
    if((np1[0]>=0) & (np1[1]>=0) & (np1[0]<leny) & (np1[1]<lenx)): listy.append(np1)
    #y+1
    np2 = [point[0]+1,point[1]]
    #print(np2)
    if((np2[0]>=0) & (np2[1]>=0) & (np2[0]<leny) & (np2[1]<lenx)): listy.append(np2)
    #x-1
    np3 = [point[0],point[1]-1]
    #print(np3)
    if((np3[0]>=0) & (np3[1]>=0) & (np3[0]<leny) & (np3[1]<lenx)): listy.append(np3)
    #y-1
    np4 = [point[0]-1,point[1]]
    #print(np4)
    if((np4[0]>=0) & (np4[1]>=0) & (np4[0]<leny) & (np4[1]<lenx)): listy.append(np4)
    #print(listy)
    return listy

def is_low(data,center,neis):
    y = center[0]
    x = center[1]
    for point in neis:
        if data[y][x] >= data[point[0]][point[1]]:
            return False
    return True

def risk_level(data):
    risk = 0
    print('risk: '+str(risk))
    lenx = len(data[0])
    leny = len(data)
    for y,row in enumerate(data):
        for x,col in enumerate(row):
            point=[y,x]
            print('point is: ')
            print(point)
            nei = get_neighbors(point,lenx,leny)
            print('neis: ')
            print(nei)
            if(is_low(data,point,nei)):
                risk += (1+int(data[point[0]][point[1]]))
                print('risk: '+str(risk))
            #print(data[y][x])
    return risk

#data = get_data('day9_test.txt')
data = get_data('day9_data.txt')
risk = risk_level(data)
print(risk)
