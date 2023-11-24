#pregunta 4

class HackerEarth:
    def __init__(self, HackNew = 1):
        
        self.HackNew = HackNew

    def set(self, HackNew):
        self.HackNew = HackNew
        return HackNew

Hack = HackerEarth()
print(Hack.set(Hack.HackNew + 1))