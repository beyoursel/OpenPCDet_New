import pytesseract
from PIL import Image
def demo():
    # 打开要识别的图片
    image = Image.open('/media/taole/ssd1/letaotao/ocr_picutre/screenshot-20231228-110255.png')
    # 使用pytesseract调用image_to_string方法进行识别，传入要识别的图片，lang='chi_sim'是设置为中文识别，
    text = pytesseract.image_to_string(image, lang='chi_sim')
    # 输入所识别的文字
    print(text)

if __name__ == '__main__':
    demo()

# tesseract test.png 1 -l eng


