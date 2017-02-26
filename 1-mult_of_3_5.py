#Find the sum of all the multiples of 3 or 5 below 1000.

mult_3 = []
mult_5 = []
for i in range(1000):
    if i % 3 == 0:
        mult_3.append(i)
    elif i % 5 == 0:
        mult_5.append(i)
    else:
        pass

print sum(mult_3) + sum(mult_5)
