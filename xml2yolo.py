import os
import xml.etree.ElementTree as ET

# 用于将voc格式xml标注文件转换为yolo格式txt标注文件
def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h


classes = ['K']  # 修改转换后的标签（自己修改）


def convert_annotation(image_name):  # 转换这一张图片的坐标表示方式（格式）,即读取xml文件的内容，计算后存放在txt文件中。
    in_file = open('E:\centernet-pytorch-main\VOCdevkit\VOC2007\Annotations\\' + image_name[:-3] + 'xml')  # xml文件夹目录（自己修改）
    out_file = open('E:\centernet-pytorch-main\VOCdevkit\VOC2007\yoloannot\\' + image_name[:-3] + 'txt', 'w')  # 生成txt的目录（自己修改）
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes:
            print("{}在class没有定义".format(cls))
            continue
        cls_id = classes.index(cls)  # 保存cls类在classes中的索引
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


wd = os.getcwd()

if __name__ == '__main__':
    img_path = 'E:\centernet-pytorch-main\VOCdevkit\VOC2007\JPEGImages'  # 图片所在的目录（自己修改)
    files = os.listdir(img_path)
    for file in files:
        convert_annotation(file)
