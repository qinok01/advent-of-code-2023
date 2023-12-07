time = [40,     70,     98,     79]
record = [215,   1051,   2147,   1005]

counter = 0
total = 1 
for i in range(len(time)):
    for j in range(1,time[i]+1):
        if (time[i]-j) * (j) > record[i]:
            counter += 1
    total = total*counter
    counter = 0
print(total)