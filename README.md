# A Scaling Law for Synthetic-to-Real Transfer: A Measure of Pre-Training

This repository is the official implementation of [A Scaling Law for Synthetic-to-Real Transfer: A Measure of Pre-Training](http://arxiv.org/abs/2108.11018). 

This repository contains the code to generate synthetic images, the results for reproducing the plots, and pre-trained models. 


## Generation of Synthetic Images

![image](https://media.github.pfidev.jp/user/285/files/e531d500-ef81-11eb-8fe5-ca07a487dbbf)

To generate synthetic images/annotations we used in the experiments, see [rendering](./rendering) directory.

## Results

To check the accuracy scores of various pre-training/fine-tuning task pairs, see [results](./results) directory. 

## Pre-trained Models

We provide pre-trained backbone networks used in the paper. Here, `task` means the pre-training task, `data` means the pre-training dataset (see [rendering](./rendering) for more details), and `# of examples` means the size of the dataset. All the pre-trained models are compatible with `resnetxx` of [torchvision](https://pytorch.org/vision/stable/index.html).

|task 	|data  	|# of examples  	|backbone   	|download   	|
|---	|----	|---	|---	|---	|
|object detection	          |bop 	|64k   	|ResNet50 |N/A  	|
|multiclass classification	|bop 	|64k   	|ResNet50 |N/A  	|
|surface normal estimation	|bop 	|64k   	|ResNet50 |N/A  	|
|semantic segmentation	    |bop 	|64k   	|ResNet50 |N/A  	|

Due to the filesize, we cannot put the download links here. If you are interested in, please let [me](mailto:hayasick@preferred.jp) know.

## Citation

If you cite our work, please use the following bibtex entry.
```
@article{mikami2021a,
    title={A Scaling Law for Synthetic-to-Real Transfer: A Measure of Pre-Training},
    author={Hiroaki Mikami and Kenji Fukumizu and Shogo Murai and Shuji Suzuki and Yuta Kikuchi and Taiji Suzuki and Shin-ichi Maeda and Kohei Hayashi},
    year={2021},
    journal={arXiv preprint arXiv:2108.11018}
}
```
