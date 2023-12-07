import numpy as np
f = open("advent55.txt", "r")
data = f.read() 
lst = data.split("\n") 
f.close() 

#destination source range
#range destination source

 
seeds = [43]
seedsTarget = [4188359137,  37519573,  3736161691,  172346126,  2590035450,  66446591,  209124047,  106578880,  1404892542,  30069991,  3014689843,  117426545,  2169439765,  226325492,  1511958436,  177344330,  1822605035,  51025110,  382778843,  823998526]
                                       #3730740516           2858545
                                        # 82281848   answer: 5421175    
                                        # 
seedsTarget = [79, 14, 55, 13]                       
#for i in range(2):
 #   seeds.append(seeds[0]+i)

lst.reverse()
print(lst)

counter = 0
maps = []
nodes = []
for i in lst:
    counter += 1 
    if "to" in i:
        maps.append(counter)
print(maps)
for i in seeds:
        x = True
        check = 1
        currentnode = i
        print(currentnode)
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

"""        for j in range(len(seedsTarget)//2):
            if nodes >= seedsTarget[2*j] and nodes < seedsTarget[2*j]+seedsTarget[2*j+1]:
                print(i)
                quit()"""
print(nodes) 