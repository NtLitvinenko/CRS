# Example by NTLDev

import CRS

Window = CRS.Win(120, 29) # standart windows console is 120, 30 but y (30) is recomended to be 29.

while True:
    Window.print()
    Window.edit_rgb(random.randint(0, 120), random.randint(0,29), (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
    time.sleep(0.25)
