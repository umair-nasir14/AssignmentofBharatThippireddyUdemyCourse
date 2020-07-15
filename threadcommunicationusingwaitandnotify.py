from threading import *
from time import sleep

class Producer:
    
    def __init__(self):
        self.products = []
        self.c = Condition()
    
    def produce(self):
        self.c.acquire()
        for i in range(1,5):
            self.products.append("iPhone" + str(i))
            sleep(1)
            print("Current products are: ", self.products)
        self.c.notify()
        self.c.release()
        
class Consumer:
    
    def __init__(self,isproduct):
        
        self.isproduct = isproduct
        
    def consume(self):
        self.isproduct.c.acquire()
        self.c.wait(timeout=0)
        self.c.release()
            
        print("Orders shipped are: ",self.isproduct.products)
        

p = Producer()
c = Consumer(p)

t1 = Thread(target=p.produce())
t2 = Thread(target=c.consume())
        