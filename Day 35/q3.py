class human:
    def __init__(self,name):
        self.name = name   #for call name
        print("Welcome to Human class")
    def work(self):
        print("You can work")
    def Think(self):
        print("You can think")

shakib = human("Shakib")
shakib.work()
print(shakib.name)