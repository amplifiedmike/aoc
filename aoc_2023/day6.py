import math

#[Ttotal,distance] want to beat distance

# Ttotal = t1 (hold button) + t2 (movement)
# V = t1 (mm/ms)
# distance = V*t2 = t1*t2 = t1*(Ttotal-t1)
# d < t1*T - t1^2
# t1^2 - T*t1 + d < 0 solve for t1

#t1 = (-T +/- sqrt(T^2 -4*1*d))/(2T)
#between the solution points will be the answer

def quadratic(a,b,c):
    discriminant = b*b - 4*a*c
    x2 = (-b + math.sqrt(discriminant))/(2*a)
    x1 = (-b - math.sqrt(discriminant))/(2*a)
    #rounding
    x2 = math.ceil(x2-1)
    x1 = math.floor(x1+1)
    return [x1,x2]

def day6(races):
    solutions=[]
    for race in races:
        T = race[0]
        d = race[1]
        solutions.append(quadratic(1,T*-1,d))
    print("part2 - num of solutions")
    print(solutions[0][1]-solutions[0][0])
    running_mult = 1
    for winning in solutions:
        num = winning[1]-winning[0]+1
        running_mult = running_mult*num
    print("part1 - running mult: ")
    print(running_mult)
    

f = [[51,222],[92,2031],[68,1126],[90,1225]]
ftest = [[7,9],[15,40],[30,200]]
f2test = [[71530,940200]]
f2 = [[51926890,222203111261225]]

day6(f2)


