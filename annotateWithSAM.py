from ultralytics import SAM
import cv2,os
import numpy as np


# Load a model
model = SAM("./sam2_b.pt")

all_img_list="/home/kingargroo/YOLOVISION/soybeanrust/image"
all_label_save_path="/home/kingargroo/YOLOVISION/soybeanrust/label"

for path in os.listdir(all_img_list):

    img_path=os.path.join(all_img_list,path)
    img=cv2.imread(img_path)

    imgh,imgw=img.shape[0:2]
    img_title=path.split('.')[0]
    txt_name = all_label_save_path +'/' +img_title + '.txt'
    txt_file = open(txt_name, 'a+')

    results = model(img)
    for result in results:
        masks=result.masks
        boxes=[]
        for mask in masks:
            for seg in mask.xy:
                segment = np.array(seg, dtype=np.int32)
                x, y, w, h = cv2.boundingRect(segment)

                if w*h>3000 or w*h<10:
                   continue
                xn,yn,wn,hn=(x+w/2)/imgw,(y+h/2)/imgh,w/imgw,h/imgh
                output_str = '0' + ' ' + str(xn) + ' ' + str(yn) + ' ' + str(wn) + ' ' + str(hn) + '\n'
                txt_file.write(output_str)


