# Satellite-Image-SuperResolution

This project is aim to apply super resolution (SR) model on satellite data. So far, SR models are developed for normal photos and it is interesting to see how would it be for such kind of data.

## Data

Using **2** satellite images around Taiwan to produce two datasets for training. These two datasets were uploaded on kaggle as following.

1. [Sentinel-2 satellite (kaggle)](https://www.kaggle.com/datasets/mchsieh/sentinel2-taiwan-dataset)
2. [Spot-6/7 satellites (kaggle)](https://www.kaggle.com/datasets/mchsieh/spot-taiwan-dataset)

|                   |      Sentinel-2     |      SPOT-6/7      |
|------------------:|:-------------------:|:------------------:|
|   Resolution      |           10 m      |           5 m      |
|   Number of Bands |  13 (RGB used only) |  4 (RGB used only) |
|   Number of Files |         1022        |        1000        |
|   File Size       |      487.99(MB)     |     489.3(MB)      | 

In order to training Super-Resolution (SR) model, **High-Resolution (HR)** and **Low-Resolution (LR)** patches are needed for whole processing. The original satellite data would be cropped into 512 $\times$ 512, considering as the **HR** patches. On the other hand, the **LR** patches are directly downsampling by factor of **2**, i.e. 256 $\times$ 256 pixels for a single patch.\
Most of images (~80%) were used for training the EDSR model and some of them (~20%) were used for validation during training phase. After training, the weight was saved in [```./edsr_wts_030_mae.h5```](https://github.com/H-MC/Satellite-Image-SuperResolution/blob/main/edsr_wts_030_mae.h5). 10 satellite images in [```./Samples```](https://github.com/H-MC/Satellite-Image-SuperResolution/tree/main/Samples) were additionally chosen for testing and evaluating the model performance.


## EDSR model
**Enhanced Deep Super-Resolution (EDSR)** is applied for this project, which is based on [this paper](https://arxiv.org/abs/1707.02921), and [source code reference](https://keras.io/examples/vision/edsr/).

<div align=left>
<img src="https://github.com/H-MC/Satellite-Image-SuperResolution/blob/main/Figures/EDSR.png" width="350">
</div>

The factor of increased resolution is only set by **2** here, and the total parameter is **926,723**, and trained for **30** epochs.

## Evaluation
To evaluate the performance of EDSR, we introduce 2 indexes to help us: **Peak Signal-to-Noise Ratio (PSNR)** and **Structure Simmilarity (SSIM)**.
The 2 indexes are calculated by the following equations:
$$PSNR=10*log_{10}(\frac{MAX^2}{MSE})$$
where MSE is the Mean-Squared Error between **Prediction** and **Ground Truth**; MAX is the maximum value of the image, the default is 256.
$$SSIM=\frac{(2\mu_x\mu_y+C_1)(2\sigma_{xy}+C_2)}{(\mu_x^2+\mu_y^2+C_1)(\sigma_x^2+\sigma_y^2+C_2)}$$
where $\mu_x,\mu_y$ are the mean values, and $\sigma_x,\sigma_y$ are the standared deviations, the x and y represent for the original image and prediction.

## Result
Here, we compared **EDSR**'s results with directly applying **bicubic** and **bilinear** method.\
The LR images are reduced their resolution by factor of 2 from the images in [```./Samples```](https://github.com/H-MC/Satellite-Image-SuperResolution/tree/main/Samples), and enlarged at the centers for better visibility.
<div>
<img src="https://github.com/H-MC/Satellite-Image-SuperResolution/blob/main/Figures/Result1.png" width="350"><img src="https://github.com/H-MC/Satellite-Image-SuperResolution/blob/main/Figures/Result2.png" width="350">
</div>
<div>
<img src="https://github.com/H-MC/Satellite-Image-SuperResolution/blob/main/Figures/Result3.png" width="350"><img src="https://github.com/H-MC/Satellite-Image-SuperResolution/blob/main/Figures/Result4.png" width="350">
</div>
<div>
<img src="https://github.com/H-MC/Satellite-Image-SuperResolution/blob/main/Figures/Result5.png" width="350"><img src="https://github.com/H-MC/Satellite-Image-SuperResolution/blob/main/Figures/Result6.png" width="350">
</div>
<div>
<img src="https://github.com/H-MC/Satellite-Image-SuperResolution/blob/main/Figures/Result7.png" width="350"><img src="https://github.com/H-MC/Satellite-Image-SuperResolution/blob/main/Figures/Result8.png" width="350">
</div>
<div>
<img src="https://github.com/H-MC/Satellite-Image-SuperResolution/blob/main/Figures/Result9.png" width="350"><img src="https://github.com/H-MC/Satellite-Image-SuperResolution/blob/main/Figures/Result10.png" width="350">
</div>
