f = open("advent4.txt", "r")
data = f.read() 
lst = data.split("\n") 
f.close() 


"""lst = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
"Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
"Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
"Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
"Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
"Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]"""

numbers = []
keys = []

for i in lst:
    temp = []
    temp2 = []
    counter = 0
    score = 0
    nexts = 0
    ans = False
    for j in i:
        counter += 1 
        if j == "|":
            ans = True
        
        if nexts != 0:
            nexts -= 1
            continue


        if ans == False:
            try:
                ntemp = int(i[counter])
                nexts = 1
                try: 
                    x = int(i[counter+1])
                    ntemp = ntemp*10
                    ntemp += x
                    temp.append(ntemp)  
                    nexts = 2             
                except:
                    temp.append(ntemp)
            except:
                pass
        
        if ans == True:
            try:
                ntemp = int(i[counter])
                nexts = 1
                try: 
                    x = int(i[counter+1])
                    ntemp = ntemp*10
                    ntemp += x
                    temp2.append(ntemp)  
                    nexts = 2           
                except:
                    temp2.append(ntemp)
            except:
                pass
    numbers.append(temp[1:])
    keys.append(temp2)


def scoreCard(n, k, ind):
    score = 0
    for i in n[ind]:
        if i in k[ind]:
            score += 1
    return score


def cards(n, k, ind, ourCards):
    try:
        ourCards[ind] = ourCards[ind] + 1
    except:
        ourCards.append(1)
    score = scoreCard(n,k,ind)
    if score == 0:
        return ourCards
    for l in range(1, score+1):
        if ind+l < len(n):
            cards(n,k,ind+l,ourCards)
    return ourCards

print(cards(numbers, keys, 0, []))

def listadd(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

total = 0

for i in range(len(numbers)):
    total += listadd(cards(numbers, keys, i, []))

print(total)

