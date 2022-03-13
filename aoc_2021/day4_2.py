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
    
def stamp_card(card,num):
    #print('stamp num ' + str(num))
    for idxy, rows in enumerate(card):
        for idxx,element in enumerate(rows):
            if(element == num): 
                card[idxy][idxx]=""
    #print(cards)
    return

def check_win(card):
    #horiz
    for idxy in range(5):
        horiz_win=True
        for idxx in range(5):
            #if element is a number, set the win condition to false
            if(card[idxy][idxx]): 
                horiz_win=False
        if(horiz_win):break
    #if(horiz_win): print(card[card_no])
    #vert
    if(horiz_win):
        return True
    else:
        for idxx in range(5):
            vert_win=True
            for idxy in range(5):
                #if element is a number, set the win condition to false
                if(card[idxy][idxx]): 
                    vert_win=False
            if(vert_win):break
    if(vert_win):
        return True
    return False

def sum(card):
    sum=0
    for row in card:
        for element in row:
            if(element):sum += int(element)
    return sum

def bingo(filename):
    winning_cards=[]
    nums, cards = get_data(filename)
    #print(nums)
    #print(cards)
    for i in range(len(nums)):
        for card_no,card in enumerate(cards):
            if(card_no not in winning_cards):
                stamp_card(card,nums[i])
                win_check = check_win(card)
                if(win_check):
                    winning_cards.append(card_no)
        if(len(winning_cards) == len(cards)): break
    print('last card to win is ' + str(winning_cards[-1]))
    sums = sum(cards[winning_cards[-1]])
    score = sums*int(nums[i])
    print(nums[i])
    print(sums)
    print(score)

bingo('day4_1_data.txt')
#bingo('day4_test.txt')
#bingo('day4_test2.txt')


