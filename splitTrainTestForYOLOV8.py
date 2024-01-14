import cv2,os,random,shutil

newdataset_root_file='/home/kingargroo/seed/yolov8'
img_root_file='/home/kingargroo/seed/rice'
label_root_file='/home/kingargroo/seed/ricelabel/label3'

#create new files
os.makedirs(newdataset_root_file+'/train')
os.makedirs(newdataset_root_file+'/test')
os.makedirs(newdataset_root_file+'/train'+'/images')
os.makedirs(newdataset_root_file+'/train'+'/labels')
os.makedirs(newdataset_root_file+'/test'+'/images')
os.makedirs(newdataset_root_file+'/test'+'/labels')

#spilt the iamge and labels according to idx
img_list=os.listdir(img_root_file)
label_list=os.listdir(label_root_file)
img_num=len(img_list)
random_numbers = [random.randint(0, img_num-1) for _ in range(img_num)]
train_ratio=0.85
train_num=int(train_ratio*img_num)
train_id=random_numbers[:train_num]
test_id=random_numbers[train_num::]
train_img_list=[img_list[id] for id in train_id]
test_img_list=[img_list[id] for id in test_id]
train_label_list=[label_list[id] for id in train_id]
test_label_list=[label_list[id] for id in test_id]

for img_name,label_name in zip(train_img_list,train_label_list):
    img_raw_path=os.path.join(img_root_file,img_name)
    label_raw_path=os.path.join(label_root_file,label_name)
    shutil.copy(img_raw_path,newdataset_root_file+'/train/images')
    shutil.copy(label_raw_path, newdataset_root_file+'/train/labels')

for img_name,label_name in zip(test_img_list,test_label_list):
    img_raw_path=os.path.join(img_root_file,img_name)
    label_raw_path=os.path.join(label_root_file,label_name)
    shutil.copy(img_raw_path,newdataset_root_file+'/test/images')
    shutil.copy(label_raw_path, newdataset_root_file+'/test/labels')
