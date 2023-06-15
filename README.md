# scripts

Various script to support Traffix development procceses.


# Machine Learning 
## prep_dataset_1

This script download COCO `train` and `val` data, and filter COCO classes dataset.


## prep_dataset_2_&_train

This script adjust the COCO `train` and `val` filtered annotations dataset to adjust the default classes number to the numbere of filtered classes.


Final Dataset: https://drive.google.com/file/d/1OW9g67a5n__nufpveFrv_5Yck1HOLy3I/view?usp=sharing

```
{
classes:
    bicycle: 0
    car: 1
    motorcycle: 2
    bus: 3
    truck: 4
}
```

Trained Model 116 epoch: https://drive.google.com/file/d/1FO1zZoR60iatcuoZ9CiKcjFbFnFAQPn_/view?usp=sharing

|epoch|train/box_loss|train/cls_loss|train/dfl_loss|metrics/precision(B)|metrics/recall(B)|metrics/mAP50(B)|metrics/mAP50-95(B)|val/box_loss|val/cls_loss|val/dfl_loss|lr/pg0   |lr/pg1   |lr/pg2   |
|-----|--------------|--------------|--------------|--------------------|-----------------|----------------|-------------------|------------|------------|------------|---------|---------|---------|
|
|                      116 (latest trained epoch)|                 1.1649|                 1.1808|                 1.3005|                0.63305|                0.50011|                0.54295|                0.34452|                 1.3287|                 1.2983|                 1.3942|               0.002575|               0.002575|               0.002575| 
|

