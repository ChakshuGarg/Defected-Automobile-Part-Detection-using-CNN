from PIL import Image
import glob

def ResizeImage(DirPath):
   for filepath in glob.iglob(DirPath):
       basewidth = 500
       img = Image.open(filepath)
       wpercent = (basewidth/float(img.size[0]))
       hsize = int((float(img.size[1])*float(wpercent)))
       img = img.resize((basewidth,hsize), Image.ANTIALIAS)
       img.save(filepath)



