
# FEC: Fast Euclidean Clustering for Point Cloud Segmentation

[![Open In Colab][image-1]][1]  [![Binder][image-2]][2]

<p>
	<a href="https://github.com/sindresorhus/123"><img src="https://camo.githubusercontent.com/abb97269de2982c379cbc128bba93ba724d8822bfbe082737772bd4feb59cb54/68747470733a2f2f63646e2e7261776769742e636f6d2f73696e647265736f726875732f617765736f6d652f643733303566333864323966656437386661383536353265336136336531353464643865383832392f6d656469612f62616467652e737667"></a>
	<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://camo.githubusercontent.com/bca967b18143b8a5b2ffe78bd4a1a30f6bc21de83bd8336f748e96498af38b38/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d43432532304259253230342e302d6c69676874677265792e737667"></a>
	<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://camo.githubusercontent.com/33126b4770aa6f169b2a93e75678d52647f19972fa8d205e478049966e3b1a07/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646f63732d737461626c652d627269676874677265656e2e7376673f7374796c653d666c6174266c6f6e6743616368653d74727565"></a>
	<a href="https://github.com/allegroai/clearml"><img src="https://camo.githubusercontent.com/f60861e75a851f69a1fb8a5c671ef233147b7781a13dae226dcc2c32166654c0/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f636c6561726d6c2e737667"></a>
</p>

<p align="center">[English] / <a href="./README_CN.md">简体中文</a></p>

This is the _official_ repository for _**FEC**_.

Code repository locate permanently at [here][3].

**THIS REPOSITORY IN UNDER DAILY UPDATING!**

Segmentation from point cloud data is essential in many applications ,such as remote sensing, mobile robots, or autonomous cars. However, the point clouds captured by the 3D range sensor are commonly sparse and unstructured, challenging efficient segmentation. A fast solution for point cloud instance segmentation with small computational demands is lacking. To this end, we propose a novel fast Euclidean clustering (FEC) algorithm which applies a point-wise scheme over the cluster-wise scheme used in existing works. The proposed method avoids traversing every point constantly in each nested loop, which is time and memory-consuming. Our approach is conceptually simple, easy to implement (40 lines in C++), and achieves two orders of magnitudes faster against the classical segmentation methods while producing high-quality results.

## Table of Contents

- [Background][4]
- [Prerequisites][5]
- [Installation][6]
- [Data][7]
- [Examples][8]
- [Citation][9]
- [Maintainers][10]

## Background

## Prerequisites

In order to apply the _**FEC**_ to varies programming language environment, we provide _C++_, _Python_, and _Matlab_ style codes for implementation.
### C++ environment
### Python environment
The recommended way is to use Mini-/Anaconda and to create a new environment using:
```sh
$ conda env create -f environment.yml
```

## Installation

### C++ installation
If you are interested in building everything locally, it is recommended using [Docker][11]. To build, simply run:
```sh
$ make build
```

### Python installation
There are two ways how you can install _**FEC**_: Editable or non-editable. If all you want to do is run experiments with existing datasets and existing models, you can use the non-editable installation. To install the latest release from PyPI:
```sh
$ pip install fec(not registered yet)
```
To install the package directly from the current master branch of this repository, including any changes that are not yet part of a release, run:
```sh
$ pip install git+https://github.com/YizhenLAO/FEC.git
```
If you want to try implementing your own models or datasets, you’ll need an editable installation. For this, start by downloading or cloning the repository to your local machine. If you use git, you can run:
```sh
$ git clone https://github.com/YizhenLAO/FEC.git
```
If you don’t know git, you can also download the code from [here][12] and extract the zip-file.
After you cloned or downloaded the zip-file, you’ll end up with a directory called “fec” (or “fec-master”). Next, we’ll go to that directory and install a local, editable copy of the package:
```sh
$ cd fec
$ pip install -e .
```

## Data

## Examples

### C++ code example

### Python code example

### Matlab code example

## Citation

In case you use _**FEC**_ in your research or work, it would be highly appreciated if you include a reference to our [paper]() in any kind of publication.

> latex
```latex
@article{cao2022fec,
  title = {FEC: Fast Euclidean Clustering for Point Cloud Segmentation},
  author = {Yu Cao and Yancheng Wang and Yifei Xue and Huiqing Zhang and Yizhen Lao},
  journal = {},
  publisher = {},
  year = {2022},
  volume = {},
  number = {},
  pages = {},
  doi = {10.48550/arXiv.2208.07678},
  url = {https://doi.org/10.48550/arXiv.2208.07678}
}
```

## Maintainers

[@YizhenLAO][14]
[@IfeiHsueh][15]
[@Cyy-caoyu][16]

## License

[MIT]()(LICENSE) © Yizhen LAO

[1]:	https://colab.research.google.com/github/bipinKrishnan/fastai_course/blob/master/bear_classifier.ipynb
[2]:	https://mybinder.org/v2/gh/bipinKrishnan/fastai_course/master
[3]:	https://github.com/YizhenLAO/FEC
[4]:	#background
[5]:	#prerequisites
[6]:	#installation
[7]:	#data
[8]:	#examples
[9]:	#citation
[10]:	#maintainers
[11]:	https://docs.docker.com/get-docker/
[12]:	https://github.com/YizhenLAO/FEC/archive/refs/heads/master.zip
[14]:	https://github.com/YizhenLAO
[15]:	https://github.com/IfeiHsueh
[16]:	https://github.com/Cyy-caoyu


[image-1]:	https://colab.research.google.com/assets/colab-badge.svg
[image-2]:	https://mybinder.org/badge_logo.svg