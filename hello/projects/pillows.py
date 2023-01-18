from PIL import Image

img = Image.open('883.jpg')
# print(img.size)
# print(img.format)
area = [100,100, 300, 575]
cropped_img = img.crop(area)

img.show()
cropped_img.show()

#combine images
# sister = Image.open("")
# girl = Image.open("")

# area = [100,100,300,500]
# sister.paste(girl, area)

# r,g,b = sister.split()
# sister.show()
# r.show()

# new_img = Image.merge("RBG", (r,b,g))
# new_img.show()

#awesome merge effect
# ade = Image.open("")
# r1, g1, b1 = sister.split()
# r2, g2, b2 = ade.split()
# new_img = Image.merge("RBG", (r1,b1,g1))
# new_img = Image.merge("RBG", (r2,b2,g2))
# new_img.show()

#basic transformstion
baby = Image.open("883.jpg")
# square_baby = baby.resize((250, 250))
# flip_baby = baby.transpose(Image.FLIP_LEFT_RIGHT)
# spin_baby = baby.transpose(Image.ROTATE_90)

# baby.show()
# square_baby.show()
# flip_baby.show()
# spin_baby.show()

black_white = baby.convert("L")
black_white.show()


