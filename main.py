class Animals:
    def __init__(self, name , type , breed):
        self.name = name
        self.type = type
        self.breed = breed
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


dog1 = dog("Buddy", "Dog", "Golden Retriever")
cat2 = cat("Whiskers", "Cat", "Gray")
animelspeak(cat2)
animelspeak(dog1)