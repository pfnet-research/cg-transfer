# A Scaling Law for Synthetic-to-Real Transfer: A Measure of Pre-Training

This repository is the official implementation of [A Scaling Law for Synthetic-to-Real Transfer: A Measure of Pre-Training](https://arxiv.org/abs/xxxx). 

This repository contains the code to generate synthetic images, the results for reproducing the plots, and pre-trained models. 


## Generation of Synthetic Images

To generate synthetic images/annotations we used in the experiments, see [rendering](./rendering) directory.

## Results

To check the accuracy scores of various pre-training/fine-tuning task pairs, see [results](./results) directory. 

## Pre-trained Models

You can download pre-trained models. Here, `task` means the pre-training task, `data` means the pre-training dataset (see [results](./results) for more details), and `# of examples` means the size of the dataset. 

|task 	|data  	|# of examples  	|model   	|
|---	|----	|---	|---	|
|object detection	|bop 	|64k   	|[download](https://drive.google.com/mymodel.pth)  	|
|multiclass classification	|bop 	|64k   	|[download](https://drive.google.com/mymodel.pth)  	|
|surface normal estimation	|bop 	|64k   	|[download](https://drive.google.com/mymodel.pth)  	|
|semantic segmentation	|bop 	|64k   	|[download](https://drive.google.com/mymodel.pth)  	|


