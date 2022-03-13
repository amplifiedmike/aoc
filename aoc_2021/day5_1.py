def get_xy(filename):
    x_start=[]
    y_start=[]
    x_end=[]
    y_end=[]
    X=[]
    Y=[]
    f = open(filename)
    for line in f:
        line = line.rstrip()
        line = line.split(",")
        x_start.append(int(line[0]))
        y_start.append(int(line[1].split(" -> ")[0]))
        x_end.append(int(line[1].split(" -> ")[1]))
        y_end.append(int(line[-1]))
    #print(x_start)
    #print(y_start)
    #print(x_end)
    #print(y_end)
    X.append(x_start)
    X.append(x_end)
    Y.append(y_start)
    Y.append(y_end)
    return X,Y

def get_lines(x,y):
    hx1=[]
    hy1=[]
    hx2=[]
    hy2=[]
    vx1=[]
    vy1=[]
    vx2=[]
    vy2=[]
    dx1=[]
    dy1=[]
    dx2=[]
    dy2=[]
    for i in range(len(x[0])):
        if(x[0][i] == x[1][i]):#vert line
            vx1.append(x[0][i])
            vx2.append(x[1][i])
            vy1.append(y[0][i])
            vy2.append(y[1][i])
        elif(y[0][i] == y[1][i]):#horiz line
            hx1.append(x[0][i])
            hx2.append(x[1][i])
            hy1.append(y[0][i])
            hy2.append(y[1][i])
        else: #diag line
            dx1.append(x[0][i])
            dx2.append(x[1][i])
            dy1.append(y[0][i])
            dy2.append(y[1][i])
    h=[hx1,hx2,hy1,hy2]
    v=[vx1,vx2,vy1,vy2]
    d=[dx1,dx2,dy1,dy2]
    return h,v,d

def print_hits(hits,enable):
    if(enable):
        for i in range(len(hits[0])):
            print(hits[i])
        print('\n')
    return

def mark_hits(h, v, d, hits, small):
    #format of line h=[hx1,hx2,hy1,hy2]
    for i in range(len(h[0])):
        y = h[2][i]
        x1 = h[0][i]
        x2 = h[1][i]
        if(x1>x2):
            temp = x1
            x1=x2
            x2=temp
        leng = x2-x1
        #print(str(x1)+" "+str(x2)+" "+str(y)+" "+str(y))
        for i in range(leng+1):
            #print(i)
            hits[x1+i][y] += 1
        print_hits(hits,small)
    i=0
    for i in range(len(v[0])):
        x = v[0][i]
        y1 = v[2][i]
        y2 = v[3][i]
        if(y1>y2):
            temp = y1
            y1=y2
            y2=temp
        leng = y2-y1
        #print(str(x)+" "+str(x)+" "+str(y1)+" "+str(y2))
        for i in range(leng+1):
            #print(i)
            hits[x][y1+i] += 1
        print_hits(hits,small)

    for i in range(len(d[0])):
        x1 = d[0][i]
        x2 = d[1][i]
        y1 = d[2][i]
        y2 = d[3][i]
        if(x1>x2):
            temp = x1
            x1=x2
            x2=temp
            temp = y1
            y1=y2
            y2=temp

        
        while(x1 <= x2):
            hits[x1][y1] += 1
            x1 +=1
            if(y2>y1): y1 +=1
            else: y1 -=1
    return

def sum_hits(hits):
    sum=0
    for i in range(len(hits[0])):
        for j in range(len(hits[1])):
            if int(hits[i][j]) >= 2: sum+=1
    return sum

def generate_hit_mat(sizex,sizey):
    hits=[[0 for i in range(sizex)] for j in range(sizey)]
    return hits

def day5(filename,small):
    if(small):
        hits=generate_hit_mat(10,10)
    else:
        hits=generate_hit_mat(1000,1000)
    x,y = get_xy(filename)
    h,v,d = get_lines(x,y)
    if(small):
        print(h)
        print(v)
        print(d)
        print_hits(hits,small)
    mark_hits(h,v,d,hits,small)
    score = sum_hits(hits)
    print(score) 
    return


day5("day5_data.txt",False) 
#day5("day5_test.txt",True) 