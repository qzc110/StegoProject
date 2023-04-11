from PIL import Image
import numpy as np
import sys
import time
start_time = time.time()

def main():
    if len(sys.argv) < 3:
        print("Please use the following format: py decoder.py secret.jpg bit_depth")
        return
    
    bit_depth = int(sys.argv[2])
    if bit_depth < 1 or bit_depth > 7:
        print("bit_depth must be within 1 to 7")
        return
    
    # open image and convert to array of (r, g, b) values
    secret_img = Image.open(sys.argv[1]).convert("RGB")
    secret_arr = np.array(secret_img)

    # zero out most sig bits and shift left
    mask = int('0' * (8 - bit_depth) + '1' * bit_depth, 2)
    shift = 8 - bit_depth
    secret_arr &= mask
    secret_arr <<= shift

    output_img = Image.fromarray(secret_arr)
    output_img.save("image_decode.png")
    print("Finished in %s seconds" % '{0:.5g}'.format(time.time() - start_time))

    return

if __name__ == '__main__':
    main()