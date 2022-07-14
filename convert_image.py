from PIL import Image

from config import desktop


def scale_pil_image(im, w, h):
    new_h = int(h * 540 / w / 2.2)
    new_w = 540
    resize_img = im.resize((new_w, new_h))

    pixels = list(resize_img.getdata())
    width, height = resize_img.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    return pixels


def create_txt_image(img, name):
    alpha = ['@', '#', 'S', '%', '?', '*', '+', ':', ',', '.']
    text_image = ''

    for string in range(len(img)):
        for column in range(len(img[0])):
            color = img[string][column]
            symbol = alpha[int(color//28.33333333333333)]
            text_image += symbol
        text_image += '\n'
    text_image = text_image[: -1]

    with open(f'{desktop}\\{name}.txt', 'w', encoding='utf-8') as f:
        f.write(text_image)
    return text_image


def main(path, name):
    im = Image.open(path).convert('L')
    h = im.height
    w = im.width

    res_pil_img = scale_pil_image(im, w, h)

    return create_txt_image(res_pil_img, name)
