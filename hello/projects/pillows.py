from PIL import Image

img = Image.open('883.jpg')
# print(img.size)
# print(img.format)
area = [100,100, 300, 575]
cropped_img = img.crop(area)

img.show()
cropped_img.show()

#combine images
sister = Image.open("")
girl = Image.open("")

area = [100,100,300,500]
sister.paste(girl, area)

r,g,b = sister.split()
sister.show()
r.show()

new_img = Image.merge("RBG", (r,b,g))
new_img.show()

#awesome merge effect
ade = Image.open("")
r1, g1, b1 = sister.split()
r2, g2, b2 = ade.split()
new_img = Image.merge("RBG", (r1,b1,g1))
new_img = Image.merge("RBG", (r2,b2,g2))
new_img.show()
