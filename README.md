# Satellite-Image-SuperResolution

## Data

Using **2** satellite images around Taiwan to produce two data set for training. These two dataset were uploaded on kaggle.

1. [Sentinel-2 satellite](https://www.kaggle.com/datasets/mchsieh/sentinel2-taiwan-dataset)
2. [Spot-6/7 satellites](https://www.kaggle.com/datasets/mchsieh/spot-taiwan-dataset)

|                   |     Sentinel-2     |      SPOT-6/7     |
|------------------:|:------------------:|:-----------------:|
|   Resolution      |           10 m     |           5 m     |
|   Number of Bands | 10?(RGB used only) | 4?(RGB used only) |
|   Number of Files |           ??       |           ??      |
|   File Size       |           ??       |           ??      | 

In order to training Super-Resolution (SR) model, **High-Resolution (HR)** and **Low-Resolution (LR)** patches are needed for whole processing. The original satellite data would be cropped into 512 $\times$ 512, considering as the **HR** patches. On the other hand, the **LR** patches are directly downsampling by factor of **2**, as well as 256 $\times$ 256 pixels per patch.


## EDSR model
Enhanced Deep Super-Resolution (EDSR) is based on [this paper](https://arxiv.org/abs/1707.02921), and [source code reference](https://keras.io/examples/vision/edsr/).

## Result

