import os
import pandas as pd
import numpy as np

label_list=os.listdir("/home/kingargroo/YOLOVISION/newspore/corn/label")
for label_name in label_list:
    label_path_name=os.path.join("//home/kingargroo/YOLOVISION/newspore/corn/label",label_name)
    
    txt_name = '/home/kingargroo/YOLOVISION/newspore/corn/label1/' + label_name.split(sep='.')[0] + '.txt'
    print(txt_name)
    txt_file = open(txt_name, 'a+')
    all_labels = pd.read_csv(label_path_name, header=None, sep=' ')
    all_labels = np.array(all_labels)

    for label in all_labels:
        print(label)
        
        cx,cy,w_,h_=label[1],label[2],label[3],label[4]
        output_str = '1' + ' ' + str(cx) + ' ' + str(cy) + ' ' + str(w_) + ' ' + str(h_) + '\n'
        txt_file.write(output_str)


