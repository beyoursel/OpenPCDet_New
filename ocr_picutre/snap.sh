#!/bin/env bash 
# copy from https://aistudio.baidu.com/aistudio/projectdetail/5665249

# 定义一个文件基本路径，假设用户名是 pi，临时文件放在主目录下的ocrtemp下
SCR="/home/taole/snap_pictures"

# 获取一个截图
# 这里用到了gnome-screenshot，需要先安装好：sudo apt install gnome-screenshot
gnome-screenshot -a -f ${SCR}.png

# 放大图片
# 如果觉得效果不好，可以尝试把图片放大
# 需要先安装一个软件包：sudo apt install imagemagick
# mogrify -modulate 100,0 -resize 400% ${SCR}.png 

# conda activate ocr

# OCR by paddleocr
# python3 /media/taole/ssd1/letaotao/ocr_picutre/ocr.py -i ${SCR}.png -o ${SCR}.txt

# 打开文件
# 调用系统默认程序分别打开：原始图片、检测结果、识别出来的文本
xdg-open ${SCR}.png
# xdg-open ${SCR}.jpg
# xdg-open ${SCR}.txt

# 把文本复制到剪切板
# 需要先安装软件包：sudo apt install xclip
# 由于ocr结果一般都会有各种问题，其实并不能直接使用
# cat ${SCR}.txt | xclip -selection clipboard
xclip -selection clipboard -t image/png -i ${SCR}.png

# 退出
exit