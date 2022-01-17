from multiprocessing import Pool
import time
#import os
#print(os.cpu_count())
def multiplication(n):
    answer = 1
    for i in range(1000):
        answer *= i
    return answer
time1 = time.time()
if __name__ == "__main__": 
    p=Pool()
    result=p.map(multiplication,range(10000))
    p.close()
    p.join()
    time2 = time.time()
    print("It took " + str(time2-time1) +" seconds")