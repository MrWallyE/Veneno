# -*- coding: utf-8 -*-
from PIL import Image
import argparse


def get_char(r,g,b,alpha=256):   
    if alpha == 0:
    	return " "
    gary = (2126 * r + 7152 * g + 722 * b) / 10000    #由公式:gary / 256 == x / len(ascii_cahr)
    ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
    x = int((gary / (alpha + 1.0)) * len(ascii_char))

    return ascii_char[x]


    def write_file(out_file_name,content):
    	with open(out_file_name,"w") as f:
    		f.write(content)


def main(file_name="test.jpg",width=80,height=80,out_file_name="out_file"):
	text = ""
	im = Image.open(file_name)
	im = im.resize((width,height), Image,NEAREST)
	for i in xrange(height):
	    for j in xrange(width):
	        content = im.getpixel((j,i))
	        text += get_char(*content)
	    text += "\n"
	print text
	write_file(out_file_name,text)


#命令行输入参数处理
def parse_param():
	parser = argparse.ArgumentParser()    #参数解析
	parser.add_argument("input_file")    #输入文件
	parser.add_argument("out_file")    #输出文件
    

    parser.add_argument('--width', type = int, default = 50)    #输出字符画宽
    parser.add_argument('--height', type = int, default = 80)     #输出字符画高


    args = parser.parse_args()
    width, height, in_file, out_file = args.width, args.height, args.input_file, args.out_file
    return width, height, in_file, out_file


if __name__ == '__main__':
	width, height, in_f, out_f = parse_param()
	main(file_name="ascii_dora.png", width=width, height=height, out_file=out_f)