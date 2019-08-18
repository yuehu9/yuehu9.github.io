
from PIL import Image
import glob

for filename in glob.glob('../images/gallery/*.JPG'):
    img = Image.open(filename)
    m, n = img.size
    img = img.resize((m//2, n//2), Image.ANTIALIAS)
    img.save(filename, optimize=True, quality=85)
