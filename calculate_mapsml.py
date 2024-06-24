import argparse
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--anno_json', type=str, default='/home/kingargroo/seed/experiment_data/4/val.json', help='training model path')
    parser.add_argument('--pred_json', type=str, default='/home/kingargroo/yolov10/runs/detect/val3/predictions.json', help='data yaml path')

    return parser.parse_known_args()[0]


if __name__ == '__main__':
    opt = parse_opt()
    anno_json = opt.anno_json
    pred_json = opt.pred_json
    cat_id=0
    anno = COCO(anno_json)  # init annotations api
    pred = anno.loadRes(pred_json)  # init predictions api
    eval = COCOeval(anno, pred, 'bbox')
    eval.params.maxDets = [1,500,1500]
    eval.params.iouThrs = [0.5]
    eval.params.catIds = [cat_id]
    eval.evaluate()
    eval.accumulate()
    eval.summarize()
    
    
    # Load a model
model = YOLO("/home/kingargroo/corn/runs/detect/train100/weights/best.pt")

# Customize validation settings
#validation_results = model.val(data="/home/kingargroo/seed/experiment_data/wheat quality detection.v2i.yolov8/data.yaml",  batch=2, device="0",max_det=1500,split='test', save_json=True)
