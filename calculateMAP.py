import torch
from torchmetrics.detection import MeanAveragePrecision
import pandas as pd
import numpy as np
import os
prediction_file='/home/kingargroo/seed/ablation1/test_result/cucumber_result'
groundtruth_file='/home/kingargroo/seed/ablation1/test_result/cucumber_label'
prediction_file_list=os.listdir(prediction_file)
groundtruth_file_list=os.listdir(groundtruth_file)
# each dict represent an image
preds = []
targets=[]
for pred_file,gt_file in zip(prediction_file_list,groundtruth_file_list):
    assert pred_file==gt_file
    pred_file_name,gt_file_name=os.path.join(prediction_file,pred_file),os.path.join(groundtruth_file,gt_file)
    pred_labels=np.array(pd.read_csv(pred_file_name,header=None,sep=' '))
    gt_labels=np.array(pd.read_csv(gt_file_name,header=None,sep=' '))
    num_gt=len(gt_labels)
    num_pred=len(pred_labels)
    pred_boxes=pred_labels[:,1:-1]
    pred_scores=pred_labels[:,-1]
    pred_boxes,pred_scores=torch.tensor(pred_boxes),torch.tensor(pred_scores)
    pred_label=torch.zeros((num_pred,),dtype=torch.int)
    preds.append(
        dict(
            boxes=pred_boxes,
            scores=pred_scores,
            labels=pred_label
        )
    )
    target_boxes=gt_labels[:,1::]

    target_scores=gt_labels[:,0]
    target_scores,target_boxes=torch.tensor(target_scores),torch.tensor(target_boxes)
    target_label=torch.zeros((num_gt,),dtype=torch.int)
    targets.append(
        dict(
            boxes=target_boxes,
            scores=target_scores,
            labels=target_label

        )
    )

mAP=MeanAveragePrecision(box_format='cxcywh',iou_type='bbox',max_detection_thresholds=[1500]*3)
mAP.update(preds=preds,target=targets)
mAP_dict=mAP.compute()
print(mAP_dict['map'])

