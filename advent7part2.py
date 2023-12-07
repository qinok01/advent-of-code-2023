f = open("advent7.txt", "r")
data = f.read() 
lst = data.split("\n") 
f.close() 
#destination source range


def getValue(x):
    cardsdict ={} 
    for i in range(1,15):
        cardsdict[i] = 0
    betList = []
    first = []
    temp = 0
    bet = 0
    value = 0
    p = True
    fvalue = 0
    for i in x:
        if p:
            try:
                cardsdict[int(i)] = cardsdict[int(i)] + 1
                first = [int(i)] + first
            except:
                if i == "K":
                    cardsdict[13] = cardsdict[13] + 1
                    first = [13] + first
                elif i == "T":
                    cardsdict[10] = cardsdict[10] + 1
                    first = [10] + first
                elif i == "A":
                    cardsdict[14] = cardsdict[14] + 1
                    first = [14] + first
                elif i == "J":
                    cardsdict[1] = cardsdict[1] + 1
                    first = [1] + first
                elif i == "Q":
                    cardsdict[12] = cardsdict[12] + 1
                    first = [12] + first
                else:
                    p = False
        else:
            betList = [int(i)]+betList

    for i in range(len(betList)):
        bet += betList[i]*(10**i)
    cardsdict["bet"] = bet

    jokes = cardsdict[1]

    for i in cardsdict:
        if cardsdict[i] == 0:
            continue
        elif i == "bet" or i == 1:
            continue
        elif cardsdict[i] == 1:
            continue
#            if i > value and i > temp:
#                temp = i
        elif cardsdict[i] == 2:
            value += 1000000
        elif cardsdict[i] == 3:
            value += 10000000
        elif cardsdict[i] == 4:
            value += 100000000
        elif cardsdict[i] == 5:
            value += 1000000000
        
    if jokes > 0 and jokes < 5:
        if value == 0:
            value = 10**jokes*100000
        else:
            value = 10**(len(str(value))-1 + jokes) + value - 10**(len(str(value))-1)
                

    if jokes == 5:
        value = 1000000000
    
    for i in range(len(first)):
        fvalue += first[i]*15**i
    cardsdict["value"] = value + fvalue
    return cardsdict

valuelst = []
for i in lst:
    valuelst.append((getValue(i)["value"], getValue(i)["bet"]))

print(valuelst)
list.sort(valuelst)

scores = 0
for i in range(len(valuelst)):
    scores += valuelst[i][1] * (i+1)
print(scores)