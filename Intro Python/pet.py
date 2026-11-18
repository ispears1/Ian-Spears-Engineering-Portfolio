class Pet:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        
    def setAge(self,age):
        self.age=age
    
    def setName(self, name):
        self.name=name
        
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def __str__(self):
        return "My name is {} and I am {} years old".format(self.name, self.age)
    
class Dog(Pet):
    def __init__(self, name, age):
        Pet.__init__(self,name,age)
        self.tricks = []
        
    def learnTrick(self, trick):
        self.tricks.append(trick)
        
    def getTricks(self):
        return self.tricks
    
    def __str__(self):
        return "I am a Dog\n" + Pet.__str__(self)
    
if __name__ == "__main__":
    p = Pet("Joffery", 10)
    p.setAge(11)
    print(p)
    d = Dog("Spike", 4)
    print(d)
    d.learnTrick("sit")
    d.setAge(5)
    print(d.getTricks())
