from datetime import date
import time

startTime = time.perf_counter()
ldates = []

d1 = date(2016,4,12)
d2 = date(2018,4,12)
d3 = date(2020,4,12)

ldates.append(d1)
ldates.append(d2)
ldates.append(d3)

ldates.sort()

time.sleep(3)  #sleep for 3 seconds

for i in ldates:
    print(i)
    
endTime = time.perf_counter()

print('Execution time:', endTime - startTime)
    
