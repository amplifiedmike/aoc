def get_data(filename):
    listy=[]
    draws =[]
    card = []
    f = open(filename)
    for line in f:
        listy.append(line.rstrip())  
    draws=listy[0].split(",").copy()
    listy = listy[2:]
    for i in range(len(listy)):
        listy[i]=listy[i].replace("  "," ")
        listy[i]=listy[i].split()
    listy[:] = [x for x in listy if x] #remove empty elements
    for i in range(len(listy)//5):
        card.append(listy[(i*5):(5+i*5)])
    return draws,card
    
def stamp_cards(cards,num):
    print('stamp num ' + str(num))
    for card_num,card in enumerate(cards):
        for idxy, rows in enumerate(card):
            for idxx,element in enumerate(rows):
                if(element == num): 
                    cards[card_num][idxy][idxx]=""
                    print(cards[card_num])
    #print(cards)
    return

def check_win(cards):
    #horiz
    for card_no,card in enumerate(cards):
        for idxy in range(5):
            horiz_win=True
            for idxx in range(5):
                #if element is a number, set the win condition to false
                if(cards[card_no][idxy][idxx]): 
                    horiz_win=False
            if(horiz_win):
                win_card = card_no
                break
        if(horiz_win): break
    #if(horiz_win): print(card[card_no])
    #vert
    if(horiz_win):
        print("winning card is: " + str(win_card))
        return True, win_card
    else:
        for card_no,card in enumerate(cards):
            #print(card_no)
            for idxx in range(5):
                vert_win=True
                for idxy in range(5):
                    #if element is a number, set the win condition to false
                    if(cards[card_no][idxy][idxx]): 
                        vert_win=False
                if(vert_win):
                    win_card = card_no
                    break
            if(vert_win):break
        #if(vert_win): print(card[card_no])
    if(vert_win):
        print("winning card is: " + str(win_card))
        return True, win_card
    return False, 0

def sum(card):
    sum=0
    for row in card:
        for element in row:
            if(element):sum += int(element)
    return sum

def bingo(filename):
    nums, cards = get_data(filename)
    #print(nums)
    #print(cards)
    for i in range(len(nums)):
        stamp_cards(cards,nums[i])
        win_check,win_card = check_win(cards)
        if(win_check):
            print(cards[win_card])
            break
    #print(str(cards) + str(nums[i]))
    sums = sum(cards[win_card])
    score = sums*int(nums[i])
    print(nums[i])
    print(sums)
    print(score)

bingo('day4_1_data.txt')
#bingo('day4_test.txt')
#bingo('day4_test2.txt')


