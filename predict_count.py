import cv2
import os
import numpy as np
from ultralytics import YOLO

model = YOLO('/home/kingargroo/seed/ablation1/runs/detect/train16/weights/best.pt')
img_path = '/home/kingargroo/seed/validate3'
img_list = os.listdir(img_path)
label_file_root = '/home/kingargroo/seed/validate2'


pre_class=0
for img_name in img_list:

    img_name_=img_path+'/'+img_name
    img_title = img_name.split('.')[0]
    img=cv2.imread(img_name_)
    txt_name=label_file_root+'/'+str(img_title)+'.txt'
    results = model(img, stream=True)
    txt_file=open(txt_name,'a+')
   

    for result in results:
        boxes = result.boxes
        
        box_data = []
        for box in boxes:
            score=box.conf[0].cpu().numpy()
            xc, yc, w, h = box.xywhn[0]
            xc, yc, w, h =xc.cpu().numpy(), yc.cpu().numpy(), w.cpu().numpy(), h.cpu().numpy()
            box_data.append([xc, yc, w, h, score])
        box_data = np.array(box_data)
        indices = cv2.dnn.NMSBoxes(box_data[:, :4].tolist(), box_data[:, 4].tolist(), score_threshold=0.5, nms_threshold=0.3)

        for i in indices:
            
            #output_str = f"{pre_class} {box_data[i][0]} {box_data[i][1]} {box_data[i][2]} {box_data[i][3]}\n"
            output_str = str(pre_class) + ' ' + str(box_data[i][0]) + ' ' + str(box_data[i][1]) + ' ' + str(box_data[i][2]) + ' ' + str(box_data[i][3]) + '\n'
            txt_file.write(output_str)
