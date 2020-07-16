from threading import *

class EvenNumbers:
    
    def even(self):
        
        print("Printing Even Numbers: ")  
        for i in range(1,101):
            if i%2==0:
                print(i)
            else:
                pass


class OddNumbers:
    
    def odd(self):
        
        print("Printing Odd Numbers: ")  
        for i in range(1,101):
            if i%2!=0:
                print(i)
            else:
                pass



e = EvenNumbers()
o = OddNumbers()


t1 = Thread(target = e.even())
t2 = Thread(target = o.odd())

t1.start()
t2.start()


print("Printing 1 to 100 :")
for i in range(1,101):
    print(i)



