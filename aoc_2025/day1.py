f = open("d1.txt", "r")

dial = 50
numZeros = 0

# #part1
# for line in f:
#     dir = line[0]
#     num = int(line[1:])
#     if(dir == 'L'):
#         dial = (dial - num) % 100
#     elif(dir == 'R'):
#         dial = (dial + num) % 100
#     if dial == 0:
#         numZeros = numZeros + 1

# print(numZeros)


#part2
zeroCrossings = 0
wasDialZero = False

for line in f:
    dir = line[0]
    num = int(line[1:])

    #full rotations
    if num >= 100:
        r = num // 100
        zeroCrossings = zeroCrossings + r
        num = num % 100

    if(dir == 'L'):
        dial = (dial - num)
    elif(dir == 'R'):
        dial = (dial + num)
    

    if dial >= 100:
        zeroCrossings = zeroCrossings + dial//100
        dial = dial % 100
    elif dial < 0:
        if(not wasDialZero):
            zeroCrossings = zeroCrossings + abs(dial//100)
        dial = dial % 100
    elif dial == 0:
        zeroCrossings = zeroCrossings + 1
    
    if dial == 0: 
        wasDialZero = True
    else: 
        wasDialZero = False

    print(dir)
    print(num)
    print(dial)
    print(zeroCrossings)
    print("\n")
    