# Mixture-of-Experts Learner for Single Long-Tailed Domain Generalization  

This repository is the official Pytorch implementation of [Mixture-of-Experts Learner for Single Long-Tailed Domain Generalization ].




## Datasets
### (1) Four bechmark datasets 
* Please download these datasets and put them to the /data file.
* ImageNet-LT and Places-LT can be found at [here](https://drive.google.com/drive/u/1/folders/1j7Nkfe6ZhzKFXePHdsseeeGI877Xu1yf).
* iNaturalist data should be the 2018 version from [here](https://github.com/visipedia/inat_comp).
* CIFAR-100 will be downloaded automatically with the dataloader.



## Pretrained models
* For the training on Places-LT, we follow previous methods and use [the pre-trained ResNet-152 model](https://github.com/zhmiao/OpenLongTailRecognition-OLTR).
* Please download the checkpoint. Unzip and move the checkpoint files to /model/pretrained_model_places/.



#### Training
* To train the expertise-diverse model, run this command:
```
python train.py -c configs/config_imagenet_lt_resnext50_sade.json
```



## Acknowledgements
This is a project based on  Self-Supervised Aggregation of Diverse Experts for Test-Agnostic Long-Tailed Recognition


