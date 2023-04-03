# Satellite-Image-SuperResolution

This project is aim to apply super resolution (SR) model on satellite data. So far, SR models are developed for normal photos and it is interesting to see how would it be for such kind of data.

## Data

Using **2** satellite images around Taiwan to produce two datasets for training. These two datasets were uploaded on kaggle as following.

1. [Sentinel-2 satellite (kaggle)](https://www.kaggle.com/datasets/mchsieh/sentinel2-taiwan-dataset)
2. [Spot-6/7 satellites (kaggle)](https://www.kaggle.com/datasets/mchsieh/spot-taiwan-dataset)

|                   |     Sentinel-2     |      SPOT-6/7     |
|------------------:|:------------------:|:-----------------:|
|   Resolution      |           10 m     |           5 m     |
|   Number of Bands | 10?(RGB used only) | 4?(RGB used only) |
|   Number of Files |           ??       |           ??      |
|   File Size       |           ??       |           ??      | 

In order to training Super-Resolution (SR) model, **High-Resolution (HR)** and **Low-Resolution (LR)** patches are needed for whole processing. The original satellite data would be cropped into 512 $\times$ 512, considering as the **HR** patches. On the other hand, the **LR** patches are directly downsampling by factor of **2**, as well as 256 $\times$ 256 pixels per patch.


## EDSR model
Enhanced Deep Super-Resolution (EDSR) is based on [this paper](https://arxiv.org/abs/1707.02921), and [source code reference](https://keras.io/examples/vision/edsr/).

<div align=left>
<img src="https://github.com/H-MC/Satellite-Image-SuperResolution/blob/main/Figures/EDSR.png" width="350">
</div>

## Evaluation
To evaluate the performance of EDSR, we introduce 2 indexes to help us: Peak Signal-to-Noise Ratio (PSNR) and Structure Simmilarity (SSIM).
The 2 indexes are calculated by the following equations:
$$PSNR=10*log_{10}(\frac{MAX^2}{MSE})$$
where MSE is the Mean Squared Error between **Prediction** and **Ground Truth**; MAX is the 
$$SSIM=\frac{(2\mu_x\mu_y+C_1)(2\sigma_{xy}+C_2)}{(\mu_x^2+\mu_y^2+C_1)(\sigma_x^2+\sigma_y^2+C_2)}$$
where $\mu_x,\mu_y$ are the mean values, and $\sigma_x,\sigma_y$ are the standared deviations.

## Result
Here, we compared **EDSR**'s results with directly applying **bicubic** and **bilinear** method.
<div>
<img src="https://github.com/H-MC/Satellite-Image-SuperResolution/blob/main/Figures/Result1.png" width="350"><img src="https://github.com/H-MC/Satellite-Image-SuperResolution/blob/main/Figures/Result1.png" width="350">
</div>
<div>
<img src="https://github.com/H-MC/Satellite-Image-SuperResolution/blob/main/Figures/Result1.png" width="350"><img src="https://github.com/H-MC/Satellite-Image-SuperResolution/blob/main/Figures/Result1.png" width="350">
</div>
