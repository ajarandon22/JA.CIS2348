# Jarandon Adams - 1812590
import math

wallheight = float(input('Enter wall height (feet):\n'))
wallwidth = float(input('Enter wall width (feet):\n'))

area = wallwidth * wallheight
paintneeded = area / 350
paintcansneeded = math.ceil(paintneeded)

print("Wall area:", '{:.2f}'.format(area), "square feet")
print("Paint needed:", '{:.2f}'.format(paintneeded), "gallons")
print("Cans needed:", '{:.2f}'.format(paintcansneeded), "can(s)\n")

color_dict = {
    'red': 35,
    'blue': 25,
    'green': 23
}
paintcolor = input("Choose a color to paint the wall:\n")
print("Cost of purchasing", paintcolor, "paint: $" + str(color_dict[paintcolor]))

