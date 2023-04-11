from PIL import Image, ImageOps
import numpy as np
import sys

def main():
    if len(sys.argv) < 2:
        print('Usage: py bitplanes.py image.jpg')
        return
    image = Image.open(sys.argv[1])
    image_arr = np.array(image)

    for i in range(0,8):
        mask = int('1' + '0' * i, 2)
        out_arr = image_arr & mask
        out_arr <<= (7-i)
        out_img = Image.fromarray(out_arr)
        out_img = ImageOps.autocontrast(out_img)
        out_img.save('bitplanes%i.png' % i)
    return

if __name__ == '__main__':
    main()