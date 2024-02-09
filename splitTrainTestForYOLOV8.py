import cv2,os,random,shutil

newdataset_root_file='/home/kingargroo/seed/yolov8'
img_root_file='/home/kingargroo/seed/rice'
label_root_file='/home/kingargroo/seed/ricelabel/label2'

#create new files
os.makedirs(newdataset_root_file+'/train')
os.makedirs(newdataset_root_file+'/val')
os.makedirs(newdataset_root_file+'/train'+'/images')
os.makedirs(newdataset_root_file+'/train'+'/labels')
os.makedirs(newdataset_root_file+'/val'+'/images')
os.makedirs(newdataset_root_file+'/val'+'/labels')

#spilt the iamge and labels according to idx
img_list=os.listdir(img_root_file)
label_list=os.listdir(label_root_file)
img_num=len(img_list)
random_numbers = [random.randint(0, img_num-1) for _ in range(img_num)]
train_ratio=0.85
train_num=int(train_ratio*img_num)
train_id=random_numbers[:train_num]
test_id=random_numbers[train_num::]
train_img_list, test_img_list = [], []
train_label_list, test_label_list = [], []

for id in train_id:
    train_img_list.append(img_list[id])
    name = img_list[id].split(".")[0]
    label_name = name + '.txt'
    train_label_list.append(label_name)
for id_ in test_id:
    test_img_list.append(img_list[id_])
    name = img_list[id_].split(".")[0]
    label_name = name + '.txt'
    test_label_list.append(label_name)

assert len(train_img_list) == len(train_label_list)
assert len(test_img_list) == len(test_label_list)

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
