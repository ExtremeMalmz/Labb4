class Person:
    def __init__(self, name, alder, iByggnaden, vilketRumArDet):
        self.name = name
        self.alder = alder
        self.iByggnaden = iByggnaden
        self.vilketRumArDet = vilketRumArDet
    
    def gaInIEttRum(self):
        print("Wait a minute,this isnt a room its the planet of the apes!")

    def gaUtIEttRum(self):
        pass
    
    def gaInIByggnad(self):
        pass
    
    def garUtByggnad(self):
        pass
    
class Besokare(Person):
    def __init__(self,anledningTillBesok,name, alder, iByggnaden, vilketRumArDet):
        self.anledningTillBesok = anledningTillBesok
        super().__init__(name, alder, iByggnaden, vilketRumArDet)
         
    def fragaOmVagenTillRum(self):
        print("\nHelp! I want to get off the planet of the apes!")
        
besokare = Besokare("Visiting Astronaut","Charlton Heston",25,True,"Not the planet of the apes")
besokare.gaInIEttRum()
besokare.fragaOmVagenTillRum()