# Example by NTLDev

import CRS
from PIL import Image
from CRS import Tools

Window = CRS.Win(120, 29, "Window1") # standart windows console is 120, 30 but y (30) is recomended to be 29.
ImgTool = Tools.Image(Image.open("Image1.png"))
img = ImgTool.retImage(Window)
xsch = -1
for x in img:
    xsch += 1
    sch = -1
    for y in x:
        sch += 1
        Window.edit_rgb(sch, xsch, y)

Window.print()