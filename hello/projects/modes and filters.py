from PIL import Image
from PIL import ImageFilter

baby = Image.open("883.jpg")
blur = baby.filter(ImageFilter.BLUR)
detail = baby.filter(ImageFilter.DETAIL)
edges = baby.filter(ImageFilter.FIND_EDGES)

blur.show()
detail.show()
edges.show()