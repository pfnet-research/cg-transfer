## Requirements

To run Jupyter notebook, you need the following R libraries: `repr`, `tidyverse`, `broom`.

## Usage

`results_finetune.csv` contains the main results used in our paper. This file consists of 11 columns that represent the setting of the experiment as follows:
- `n_eval`: Either the number of epochs or iterations
- `value`: Performance score (e.g. accuracy) for test data
- `pretrain.data`: The number of unique image/annotation pairs used for pre-training. 
- `pscale`: The total volume of datasets; either 64k or 1280k.
  - We first generated two datasets having 64k and 1280k examples. We then subsampled `pretrain.data` examples from them to create 'mini' datasets, which were used for pre-training.
- `ptask`: Pre-training task.
- `fdata`: Dataset used for fine-tuning.
- `fratio`: The percentage of a dataset used for fine-tuning.
- `ftask`: Fine-tuning task.
- `model`: Model name (e.g. `r50` means ResNet50).
- `nparam`: The number of parameters of the model.
- `pdata`: Dataset used for pre-training.

`results_pretrain.csv` contains the results at pre-training. 

`plot_figures.ipynb` demonstrates how to reproduce Figure 1 of the paper. 