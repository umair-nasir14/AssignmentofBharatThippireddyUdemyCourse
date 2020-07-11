class Patient():
    
    def __init__(self):
        self.__id=123
        self.__name="Umair"
        self.__ssn=1
    
    
    def setid(self,id):
        self.__id=id
    
    def getid(self):
        return self.__id
    
    def setname(self,name):
        self.__name=name
    
    def getname(self):
        return self.__name
    
    def setssn(self,ssn):
        self.__ssn=ssn
    
    def getssn(self):
        return self.__ssn
    

p = Patient()


p.setid(108)
print(p.getid())

p.setname("Umair")
print(p.getname())   
    
p.setssn(3630230768049)
print(p.getssn())        
        