from abc import abstractmethod, ABC
class TouchScreenLaptop(ABC):
    
    @abstractmethod
    def scroll(self):
        pass
    
    @abstractmethod
    def click(self):
        pass
    
    
class HP(TouchScreenLaptop):
    
    
    @abstractmethod
    def scroll(self):
        print("Scrolling in HP")
    
        
        
class Dell(TouchScreenLaptop):
    
    
    @abstractmethod
    def scroll(self):
        print("Scrolling in Dell")
    

class HPNoteBook(HP):
    
    
    def scroll(self):
        print("Scrolling in HPNoteBook")
    
    
    def click(self):
        print("clicking in HPNoteBook")    
        
        
class DellNoteBook(Dell):
    
    
    def scroll(self):
        print("Scrolling in DellNoteBook")
    

    def click(self):
        print("clicking in DellNoteBook")
        
        
        
laptop1 = HPNoteBook()
laptop1.click()
laptop1.scroll()

print("\n*******************************************\n")

laptop2 = DellNoteBook()
laptop2.click()
laptop2.scroll()


        