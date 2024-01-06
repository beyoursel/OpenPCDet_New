#!/usr/bin/env python3
# copy from https://aistudio.baidu.com/aistudio/projectdetail/5665249
from paddleocr import PaddleOCR, draw_ocr
import sys
import getopt
from PIL import Image


# 执行ocr并写入txt文件
def exe_ocr(img_path,file_txt = "result.txt",img_result = "result.jpg"):
    # Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
    # 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
    ocr = PaddleOCR(use_angle_cls=False, lang="ch")  # need to run only once to download and load model into memory
    result = ocr.ocr(img_path, cls=False)
    res = result[0]    # 因为只有一张图片，所以结果只有1个，直接取出
    boxes = []    # 检测框坐标
    txt = ""    # 检测识别结果

    for line in res:
        #print(line[1][0])
        txt += line[1][0]+"\n"    # 取出文本
        boxes.append(line[0])    # 取出检测框

    with open(file_txt, 'w')as f:    # 以w方式打开，没有就创建，有就覆盖
        f.write(txt)

    image = Image.open(img_path).convert('RGB')    # 读取原图片
    im_show = draw_ocr(image, boxes)    # 画检测框
    im_show = Image.fromarray(im_show)    # 转换
    im_show.save(img_result)    # 保存


# 主函数
def main(argv):

    img_path = ""    # 图片路径
    file_txt = "result.txt"    # 输出的文本文件路径
    img_result = "result.jpg"    # 检测结果图片路径

    # 解析参数
    # "hi:o:": 短格式分析串, h 后面没有冒号, 表示后面不带参数; i 和 o 后面带有冒号, 表示后面带参数
    # ["help", "input_file=", "output_file="]: 长格式分析串列表, help后面没有等号, 表示后面不带参数; input_file和output_file后面带冒号, 表示后面带参数
    # 返回值包括 `opts` 和 `args`, opts 是以元组为元素的列表, 每个元组的形式为: (选项, 附加参数)，如: ('-i', 'test.png');
    # args是个列表，其中的元素是那些不含'-'或'--'的参数
    opts, args = getopt.getopt(argv[1:], "hi:o:", ["help", "input_file=", "output_file="])

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('python3 ocr.py -i <input_file.png> -o <output_file.txt>')
            print('or: python3 ocr.py --input_file=<input_file.png> --output_file=<output_file.txt>')
            sys.exit()
        elif opt in ("-i", "--input_file"):
            img_path = arg
        elif opt in ("-o", "--output_file"):
            file_txt = arg

    if img_path == "":
        #print("必须指定一个图片文件")
        sys.exit()

    img_result = file_txt[:file_txt.rindex('.')+1]+"jpg"

    #print('输入图片文件为：', img_path)
    #print('输出txt文件为: ', file_txt)
    #print('输出result文件为: ', img_result)

    exe_ocr(img_path,file_txt,img_result)

if __name__ == '__main__':
    main(sys.argv)