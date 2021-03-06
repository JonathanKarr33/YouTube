import time
time1 = time.time()
for i in range(1000):
    answer = 1
    for j in range (10000):
        answer *= 1
time2 = time.time()
print("It took " + str(time2-time1) +" seconds")