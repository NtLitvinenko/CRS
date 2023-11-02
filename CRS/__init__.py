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
        
