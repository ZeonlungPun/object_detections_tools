import motmetrics as mm
import numpy as np

ts_file='/home/kingargroo/YOLOVISION/fishdataset/bot_sort.txt'
gt_file='/home/kingargroo/YOLOVISION/fishdataset/work/train/fish1/gt/gt.txt'
#讀入gt文件
gt = mm.io.loadtxt(gt_file, fmt="mot15-2D", min_confidence=1)
#讀入自己的跟蹤結果
ts = mm.io.loadtxt(ts_file, fmt="mot15-2D")
# 根據GT和自己的结果，生成accumulator，distth是距離閾值
acc=mm.utils.compare_to_groundtruth(gt, ts, 'iou', distth=0.5)
#創建度量器
mh = mm.metrics.create()

# mh模塊中有内置的显示格式
summary = mh.compute_many([acc, acc.events.loc[0:1]],
                          metrics=mm.metrics.motchallenge_metrics,
                          names=['full', 'part'])

strsummary = mm.io.render_summary(
    summary,
    formatters=mh.formatters,
    namemap=mm.io.motchallenge_metric_names
)
print(strsummary)