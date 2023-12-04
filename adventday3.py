f = open("gameredgreenblue.txt", "r")
data = f.read() 
lst = data.split("\n") 
f.close() 



'''
advent question 2 part 1
count = 1
total = 0
for i in lst: 
    counter = 0
    r = 0
    b = 0
    g = 0
    for j in i:
        counter += 1
        if counter > 3:
            if "red" in i[counter - 3:counter]:
                rtemp = int(i[counter-5])
                r = max(r, rtemp)
                try: 
                    rtemp += int(i[counter-6])*10
                    r = max(r, rtemp)
                except:
                    pass
            if "green" in i[counter - 5:counter]:
                gtemp = int(i[counter-7])
                g = max(g, gtemp)
                try: 
                    gtemp += int(i[counter-8])*10
                    g = max(g, gtemp)
                except:
                    pass

            if "blue" in i[counter - 4:counter]:
                btemp = int(i[counter-6])
                b = max(b, btemp)
                try: 
                    btemp += int(i[counter-7])*10
                    b = max(b, btemp)
                except:
                    pass
    if r < 13 and g < 14 and b < 15:
        total += count
        print(count)
    count += 1 
'''


#question 2 part 2
total = 0
for i in lst: 
    counter = 0
    r = 0
    b = 0
    g = 0
    for j in i:
        counter += 1
        if counter > 3:
            if "red" in i[counter - 3:counter]:
                rtemp = int(i[counter-5])
                r = max(r, rtemp)
                try: 
                    rtemp += int(i[counter-6])*10
                    r = max(r, rtemp)
                except:
                    pass
            if "green" in i[counter - 5:counter]:
                gtemp = int(i[counter-7])
                g = max(g, gtemp)
                try: 
                    gtemp += int(i[counter-8])*10
                    g = max(g, gtemp)
                except:
                    pass

            if "blue" in i[counter - 4:counter]:
                btemp = int(i[counter-6])
                b = max(b, btemp)
                try: 
                    btemp += int(i[counter-7])*10
                    b = max(b, btemp)
                except:
                    pass
    total += r*g*b
    
print(total)

                



                

