
f = open("advent5.txt", "r")
data = f.read() 
lst = data.split("\n") 
f.close() 
#destination source range
print(lst)

seeds = [4188359137, 2241460154, 37519573,  3736161691,  172346126,  2590035450,  66446591,  209124047,  106578880,  1404892542,  30069991,  3014689843,  117426545,  2169439765,  226325492,  1511958436,  177344330,  1822605035,  51025110,  382778843,  823998526]


counter = 0
maps = []
for i in lst:
    counter += 1 
    if i == "map:":
        maps.append(counter)
print(maps)
nodes = []

for i in seeds:
    x = True
    check = 2
    currentnode = i
    currentState = 0
    while x:
        try:
            if int(lst[check+1]) <= currentnode and (int(lst[check+1]) + int(lst[check+2])) > currentnode:
                currentnode = int(lst[check]) + currentnode - int(lst[check+1])
                currentState += 1
                if currentState > 6:
                    x = False
                    nodes.append(currentnode)
                    continue
                check = maps[currentState]
            else: 
                check += 3
        except:
                currentState += 1
                if currentState > 6:
                    x = False
                    nodes.append(currentnode)
                    continue
                check = maps[currentState]
    
print(nodes)