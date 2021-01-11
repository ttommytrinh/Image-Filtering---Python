# importing PIL.Image library and os library
from PIL import Image 
import os
import random

# Deletes old created images if they exist
images = ["combinedFilters.jpg","invert.jpg","pixelsss.jpg","change.jpg","grey.jpg"]
for i in images:
  if os.path.exists(i):
    os.remove(i)

# Adds two blank lines before any output
print("\n\n")

# Opens image - upload a Local File into repl.it
img = Image.open('image.jpg')

# Rescale image size down, if original is too large
width = img.width
height = img.height
mwidth = width // 1000
mheight = height // 1000
if mwidth > mheight:
  scale = mwidth
else:
  scale = mheight
if scale != 0:
  img = img.resize( (width // scale, height // scale) )

#Greyscale
def grey():
  pixels = img.getdata()
  new_pixels = []
  for p in pixels:
    new_pixels.append(p)
  location = 0
  while location < len(new_pixels):
    p = new_pixels[location]
    # Splits color into red, green and blue components
    r = p[0]
    g = p[1]
    b = p[2]
    # Perform pixel manipulation and stores results
    # to a new red, green and blue components
    newr = (r + g + b) // 3
    newg = (r + g + b) // 3
    newb = (r + g + b) // 3
    new_pixels[location] = (newr, newg, newb)
    location = location + 1
  newImage = Image.new("RGB", img.size)
  # Assigns the pixel values to newImage
  newImage.putdata(new_pixels)
  return newImage


#Invert
def invert():
  pixels = img.getdata()
  new_pixels = []
  for p in pixels:
    new_pixels.append(p)
  location = 0
  while location < len(new_pixels):
    p = new_pixels[location]
    r = p[0]
    g = p[1]
    b = p[2]
    newr = 255 - r
    newg = 255 - g
    newb = 255 - b
    rand = random.randint(0,99)
    if rand < 80:
      new_pixels[location] = (newr, newg, newb)
    else:
      new_pixels[location] = (r, g, b)
    location = location + 1
  newImage = Image.new("RGB", img.size)
  newImage.putdata(new_pixels)
  return newImage

#Pixelate
def pixelsss():
  pixels = img.getdata()
  new_pixels = []
  for p in pixels:
    new_pixels.append(p)

  pixelate = int(input("Enter pixelation level from 1 to 5: "))
  for i in range((img.width * img.height) // (pixelate * 4)):
    p = new_pixels[pixelate*4*i]
    for j in range(pixelate*4):
      new_pixels[pixelate * 4 * i + j] = p

  newImage = Image.new("RGB", img.size)
  newImage.putdata(new_pixels)
  return newImage

def change():
  pixels = img.getdata()
  new_pixels = []
  for p in pixels:
    new_pixels.append(p)

  red = int(input("R) Enter a number from 0 - 255: "))
  green = int(input("G) Enter a number from 0 - 255: "))
  blue = int(input("B) Enter a number from 0 - 255: "))
  
  location = 0
  while location < len(new_pixels):
    p = new_pixels[location]
    r = p[0]
    g = p[1]
    b = p[2]
    if r + red > 255:
      newr = 255
    else:
      newr = r + red
    if g + green > 255:
      newg = 255
    else:
      newg = g + green
    if b + blue > 255:
      newb = 255
    else:
      newb = b + blue
    new_pixels[location] = (newr, newg, newb)
    location = location + 1

  newImage = Image.new("RGB", img.size)
  newImage.putdata(new_pixels)
  return newImage

# Creates the four filter images
a = grey()
a.save("grey.jpg")
b = invert()
b.save("invert.jpg")
c = pixelsss()
c.save("pixelsss.jpg")
d = change()
d.save("change.jpg")

# Image filter names for use below
f1 = "invert"
f2 = "pixelsss"
f3 = "change"

# Apply multiple filters through prompts with the user
answer = input("\nWhich filter do you want me to apply?\n grey\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")
while answer != "grey" and answer != f1 and answer != f2 and answer != f3 and answer != "none":
  answer = input("\nIncorrect filter, please enter:\n grey\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")

while answer == "grey" or answer == f1 or answer == f2 or answer == f3:
  if answer == "grey":
   img = grey()
  elif answer == f1:
   img = invert()
  elif answer == f2:
   img = pixelsss()
  elif answer == f3:
   img = change()
  else:
    break
  print("Filter \"" + answer + "\" applied...")
  answer = input("\nWhich filter do you want me to apply next?\n grey\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")
  while answer != f1 and answer != f2 and answer != f3 and answer != "grey" and answer != "none":
    answer = input("\nIncorrect filter, please enter:\n grey\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")
print("Image being created...Done")


# Create the combined filter image
img.save("combinedFilters.jpg")