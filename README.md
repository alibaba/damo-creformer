# CREformer


## Introduction
This is the official codebase for CREformer: Multiomic foundation model predicts epigenetic regulation by zero-shot.

Cis-Regulatory Element Transformer (CREformer) is an LLM-based foundation model for zero-shot predictions of functional genomic elements and their regulatory effects on genes and cellular states. CREformer has 3 billion parameters and was pretrained on massive bulk and single-cell multiomic data. Typically, without the need of additional training data or fine-tuning, CREformer can realize the predictions of master regulators, enhancers, GRNs, variant effects, cell state transitions, and disease treatment in a zero-shot manner.


## Online apps
https://creformer.ibreed.cn

This is an online web application to utilize the CREformer model. Here, you can upload your own data and execute most of CREformer's zero-shot predictions through simple, coding-free web applications. This website is free for public registration and use, and we have provided the GPUs for cloud computing resources. Your data will be private and safe in your own account and cannot be seen by others.


## Environment requirements
* PyTorch 2.0.1 (cuda 11.7)
  * pip install torch==2.0.1 --index-url https://download.pytorch.org/whl/cu117
* numpy 1.21.5
  * pip install numpy==1.21.5
* einops 0.7.0
  * pip install einops==0.7.0
* pandas 1.4.4
  * pip install pandas==1.4.4

We recommend you to run the codes on NVIDIA A100 GPUs (80G). We do not recommend you to run the codes on a desktop computer.


## Pretrained CREformer parameter
* Download from Hugging Face:
  * https://huggingface.co/GenomicIntelligenceDamoAcademy/CREformer
  * The pretrained CREformer network parameters can be downloaded from the above Hugging Face repo (around 13GB). After downloading all the .pkl files (11 files in total), put them under the "pretrained_models/" path.


## Extract CREformer Attention Score 
Relevant codes were documented in "codes/example_attention_compute.ipynb". Briefly, you can input the relevant DNA+ATAC information of a specific gene, and the codes will execute the prediction of Attention Scores around this gene.

* Input Data
  * Example data can be found in "data/info_attention.txt".
  * You need to provide n x 1029-bp DNA sequences and n x 1029-bp ATAC signals, you need to specify the peak that is closest to the TSS, along with the strand of the gene.
  * Deatiled formatting can be found in the .ipynb file.
* Default file path
  * The codes will assume the input data to be placed in "data/info_attention.txt".
  * The codes will load the pretrained CREformer model from "pretrained_models/".
  * The downloading process requires installation of git-lfs. The instruction is: "git-lfs clone https://huggingface.co/GenomicIntelligenceDamoAcademy/CREformer".

After you have prepared the input data, run the codes cell by cell in the .ipynb file. The codes will print out the output information, which includes the Attention Score for each ATAC peak.
  * Output data format:
      >chrX_48648355_48648753 <br>
      Attention score:  0.8549946546554565 <br>
      >chrX_48652218_48652494 <br>
      Attention score:  1.2512104511260986 <br>
      ... ...


## CREformer simulation of perturbations (include Knockout, Knock-in, and etc.)
Relevant codes were documented in "codes/example_gexp_compute.ipynb". Briefly, you can input the relevant DNA+ATAC information of a specific gene, and the codes will execute the prediction of its expression level.

**To perform the *in silico* perturbation, you need to provide the DNA+ATAC profiles before (Ref) and after (KO, KI, and etc.) the perturbation respectively in two files.**

* Input Data format is similar to the previous section, you may refer to the .ipynb file for details.
* Default file path
  * The codes will assume the input data to be placed in "data/info_ko_org.txt" and "data/info_ko_ko.txt", respectively for the (Ref) and (KO, KI, and etc.) profiles.
  * The codes will load the pretrained CREformer model from "pretrained_models/".
 
After you have prepared the input data, run the codes cell by cell in the .ipynb file. The codes will print out the gene expressions before and after the perturbation, and you can check with their difference to model the perturbation.


## Citing CREformer
The manuscript is currently under review. You can cite the version of this paper on bioRxiv: https://doi.org/10.1101/2024.12.19.629561


## Correspondance
Fei Gu (gufei.gf@alibaba-inc.com), Damo Academy, Alibaba Group.

Zikun Yang (yangzikun.yzk@alibaba-inc.com), Damo Academy, Alibaba Group.
