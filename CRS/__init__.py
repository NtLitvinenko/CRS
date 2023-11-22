def print_rgb(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

class Win:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self.Win = [["█" for _ in range(x)] for _ in range(y)]

    def edit_rgb(self, x, y, rgb=(255, 255, 255), symbol="█"):
        self.Win[y][x] = print_rgb(rgb[0], rgb[1], rgb[2], symbol)

    def print(self):
        for i in range(self.y):
            for j in range(self.x):
                if j != self.x - 1:
                    print(self.Win[i][j], end="")
                else:
                    print(self.Win[i][j])
    def __repr__(self):
        return f"Win(x={self.x}, y={self.y}, name='{self.name}')"

class Sprite:
    def __init__(self):
        pass

    def UpdateSymbols(self, SpriteSymbols):
        """

        :param SpriteSymbols: List like [['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]
        Update symbols of Sprite
        """
        self.SpriteSymbols = SpriteSymbols
    def Render(self, Display1, StartsFrom=0, StartsX=0):
        """
        :param Display1: CRS' Window
        :param StartsFrom: Left corner of sprite (y)
        :param StartsX: Left corner of sprite (x)
        :return:
        Return nothing if all good
        """
        if StartsFrom + len(self.SpriteSymbols) > Display1.y or StartsX + len(self.SpriteSymbols[0]) > Display1.x:
            return
        YC = -1
        self.SFY = StartsFrom
        self.SFX = StartsX
        self.LY = len(self.SpriteSymbols)
        self.LX = len(self.SpriteSymbols[0])
        for i in self.SpriteSymbols:
            YC += 1
            XC = -1
            for j in i:
                XC += 1
                Display1.lst[YC + StartsFrom][XC + StartsX] = self.SpriteSymbols[YC][XC]

    def Clear(self, Display1, SFN):
        for i in range(self.LY):
            for j in range(self.LX):
                Display1.lst[self.SFY + i][self.SFX + j] = SFN
