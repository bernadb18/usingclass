class Animals:
    def __init__(self, name , type):
        self.name = name
        self.type = type
        
    def Talk(self):
         print(f"{self.name} {self.type}")
        
class dog(Animals):
    def Talk(self):
         print(f"{self.name} the {self.type} says Woof!")
              
class cat(Animals):
    def Talk(self):
         print(f"{self.name} the {self.type}says Meow!")
    
def animelspeak(animals):
     animals.Talk()


dog1 = dog("Buddy", "Dog")
cat2 = cat("Whiskers", "Cat")
animelspeak(cat2)
animelspeak(dog1)
