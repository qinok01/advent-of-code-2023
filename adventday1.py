add = 0
for i in x:
  count = 0
  counter = 0
  for j in i:
    counter += 1
    if ("one" in i[counter-3:counter]):
      if count == 0:
        u = 10
        count = 1
      k = 1

    if ("two" in i[counter-3:counter]):
      if count == 0:
        u = 20
        count = 1
      k = 2

    if ("three" in i[counter-5:counter]):
      if count == 0:
        u = 30
        count = 1
      k = 3
    if ("four" in i[counter-4:counter]):
      if count == 0:
        u = 40
        count = 1
      k = 4
    if ("five" in i[counter-4:counter]):
      if count == 0:
        u = 50
        count = 1
      k = 5
    if ("six" in i[counter-3:counter]):
      if count == 0:
        u = 60
        count = 1
      k = 6
    if ("seven" in i[counter-5:counter]):
      if count == 0:
        u = 70
        count = 1
      k = 7
    if ("eight" in i[counter - 5:counter]):
      if count == 0:
        u = 80
        count = 1
      k = 8
    if ("nine" in i[counter - 4:counter]):
      if count == 0:
        u = 90
        count = 1
      k = 9

    if counter > 6:
      p = counter - 4

    try:
      int(j)
      if (count == 0):
        u = int(j)*10
        count = 1
      k = int(j)
    except:
      continue

  add = add + u + k

print(add)