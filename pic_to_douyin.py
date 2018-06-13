import numpy as np

from PIL import Image


def convert(file_in, file_out, offset):
    # Open image
    img_raw = Image.open(file_in)
    img_raw.putalpha(255)

    # Covert image to array
    array_raw = np.array(img_raw)

    # Create R image by marking GB zero
    array_r = np.copy(array_raw)
    array_r[:, :, 1:3] = 0
    img_r = Image.fromarray(array_r)

    # Create GB image by marking R zero
    array_gb = np.copy(array_raw)
    array_gb[:, :, 0] = 0
    img_gb = Image.fromarray(array_gb)

    # Create images for R and GB separately
    canvas_r = Image.new("RGB", img_raw.size, color=(0,0,0))
    canvas_r.paste(img_r, offset, img_r)

    canvas_gb = Image.new("RGB", img_raw.size, color=(0,0,0))
    canvas_gb.paste(img_gb, (0, 0), img_gb)

    result_array = np.array(canvas_r) + np.array(canvas_gb)
    result = Image.fromarray(result_array)
    result.save(file_out)


if __name__ == '__main__':
    convert('me.jpg', 'me_douyin.jpg', (15, 15))
