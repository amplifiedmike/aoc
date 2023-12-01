f = open("day1_1.txt", "r")
#part 1, just numbers

# first_last=[]
# index=0
# for line in f:
#     num_array=[]
#     for char in line:
#         if char.isdigit():
#             num_array.append(char)
#     first_last.append(int(num_array[0]+num_array[-1]))

#     index= index +1
# #print(first_last)
# sum = 0
# for num in first_last:
#     sum = sum + num
# print(sum)

###
#part 2, numbers and spelled numbers
test_string = "tvbrkhlxdsnine65"
test_array = ["two1nine","eightwothree","abcone2threexyz","xtwone3four","4nineeightseven2","zoneight234","7pqrstsixteen"]
first_last=[]
index=0
word_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for line in f:
#for line in test_array:
    #line = test_string #testing only
    num_array_char=[]
    appended_chars=""
    for character in line:
        if character.isdigit():
            num_array_char.append(character)
            appended_chars=""
        else:
            appended_chars = appended_chars + character
            word_index = 1
            for written_nums in word_list:
                written_num_len = len(written_nums)
                appended_char_sub_list = appended_chars[-written_num_len:]
                if appended_char_sub_list == written_nums:
                    num_array_char.append(str(word_index))
                    break
                word_index = word_index+1
    #print(line)
    first_last.append(int(num_array_char[0]+num_array_char[-1]))
    print(line + "  " + str(first_last[index]))
    index= index +1



print(first_last[0])
print(first_last[-1])
sum = 0
for num in first_last:
    sum = sum + num
print(sum)
#print(index)
#print(len(first_last))