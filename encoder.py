from PIL import Image
import numpy as np
import sys
import time
start_time = time.time()

def main():
    if len(sys.argv) < 4:
        print("Usage: py merge_test.py cover.jpg secret.jpg bit_depth")
        return
    
    bit_depth = int(sys.argv[3])
    if bit_depth < 1 or bit_depth > 7:
        print("bit_depth must be within 1 to 7")
        return
    
    # open images and convert to array of (r, g, b) values
    cover_img = Image.open(sys.argv[1]).convert("RGB")
    secret_img = Image.open(sys.argv[2]).convert("RGB")
    cover_arr = np.array(cover_img)
    secret_arr = np.array(secret_img)

    # OR cover_arr's least sig bits with secret_arr's most sig bits
    mask = int('1' * (8 - bit_depth) + '0' * bit_depth, 2)
    shift = 8 - bit_depth
    cover_arr &= mask
    cover_arr |= secret_arr >> shift

    output_img = Image.fromarray(cover_arr)
    output_img.save("output.png")
    print("Finished in %s seconds" % '{0:.5g}'.format(time.time() - start_time))

    return

if __name__ == '__main__':
    main()