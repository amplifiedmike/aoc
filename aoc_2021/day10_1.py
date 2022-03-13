def get_data(filename):
    f = open(filename)
    data=[]
    for line in f:
        data.append(line.rstrip())
    return data

def check_for_closed(line):
    print('orig line:')
    print(line)
    no_more_closed=False
    while(not no_more_closed):
        newline=line.replace("[]","")
        newline=newline.replace("()","")
        newline=newline.replace("{}","")
        newline=newline.replace("<>","")
        if(newline==line): no_more_closed = True
        line=newline
        print('newline: ')
        print(newline)
    return line


def corrupted(data):
    data_cor=[]
    for idx,line in enumerate(data):
        data_cor.append(check_for_closed(line))
    print('data corr: ')
    print(data_cor)
    return

data=get_data("day10_test.txt")
print(data)
data_cor = corrupted(data)