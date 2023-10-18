# CRS - New innovation project
CRS is Console Render System.<br>
CRS is needed to create COLORED games and projects in CONSOLE.<br>
For start you need: Python >= 3.3

Example code:

```
Window = Win(209, 49) # standart windows console is 120, 30 but y (30) is recomended to be 29.

while True:
    Window.print()
    Window.edit_rgb(random.randint(0, 209), random.randint(0,48), (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
    time.sleep(0.25)
```
