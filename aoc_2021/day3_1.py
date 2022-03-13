common = [0]*12
avg = [0]*12
roundy = [0]*12
gamma_s = '0b'
epsilon_s = '0b'

num_lines=0
f = open("day3_1_data.txt")

for line in f:
    num_lines +=1
    bits = line.rstrip()
    bits = list(bits)
    #print(bits[11])
    #print(len(bits))
    for i in range(len(bits)):
       common[i] += int(bits[i])

for j in range(len(common)):
    avg[j]=common[j]/num_lines
    roundy[j] = round(avg[j])
    gamma_s += str(roundy[j])
    if(roundy[j]==0): epsilon_s += '1'
    else: epsilon_s += '0'

gamma = int(gamma_s,2)
epsilon = int(epsilon_s,2)
power = gamma*epsilon

print(gamma)
print(epsilon)
print(gamma_s)
print(epsilon_s)
print(power)