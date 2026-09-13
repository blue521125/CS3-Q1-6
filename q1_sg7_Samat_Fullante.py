class Glassware:
    def __init__(self, kindofglassware, number):
        self.kindofglassware = kindofglassware
        self.number = str(number)
        print(f"{self.kindofglassware} {self.number} created")

    def __del__(self):
        print(self.kindofglassware, self.number, "is gone")


class Beaker(Glassware):
    def __init__(self,number):
        super().__init__("Beaker", number)

    def __del__(self):
        super().__del__()


class Tray:
    def __init__(self, num_beakers=5):
        print("Tray is created")
        self.beakers = [Beaker(i) for i in range(1,num_beakers+1)]

    def holdUp(self):
        print("Tray is holding up")

    def __del__(self):
        print("Tray is gone")
        del self.beakers

tray = Tray()
tray.holdUp()
del tray
