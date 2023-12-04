f = open("day4_1.txt", "r")
f2 = open("day4_test.txt","r")

def day4(line):
    line_split = line.split()
    #print(line_split)
    second_set_flag = 0
    winning_numbers = []
    card_numbers = []
    for stringy in line_split[2:]:
        if stringy.isdigit() and not second_set_flag:
            winning_numbers.append(stringy)
        elif stringy.isdigit() and second_set_flag:
            card_numbers.append(stringy)
        elif stringy == "|":
            second_set_flag=1
        else:
            print("\nnot sure what happened\n")
    #print(winning_numbers)
    #print(card_numbers)

    #check for winning numbers
    score = 0
    matches = 0
    for number in winning_numbers:
        for card_nums in card_numbers:
            if number == card_nums:
                matches += 1
                if score == 0: score = 1
                else: score = score *2
    return score,matches

file = f

#part 1
# score = 0
# for line in file:
#     line_score, matches = day4(line)
#     score = score + line_score
# print(score)

#part2
part2_score = 0
processing = [1]*202
total_scores = []
ind = 0
for line in file:
    ind += 1
    line_score,matches = day4(line)
    for x in range(matches):
        processing[ind+x] += 1*processing[ind-1]
    total_scores.append(line_score*processing[ind-1])
    part2_score += line_score*processing[ind-1]
print(processing)
print(total_scores)
total_scores2=0
for num in processing:
    total_scores2+=num
#print(part2_score)
print(total_scores2)

