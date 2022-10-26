
# FEC: Fast Euclidean Clustering for Point Cloud Segmentation

[![Open In Colab][image-1]][1]  [![Binder][image-2]][2]

<p>
	<a href="https://github.com/sindresorhus/123"><img src="https://camo.githubusercontent.com/abb97269de2982c379cbc128bba93ba724d8822bfbe082737772bd4feb59cb54/68747470733a2f2f63646e2e7261776769742e636f6d2f73696e647265736f726875732f617765736f6d652f643733303566333864323966656437386661383536353265336136336531353464643865383832392f6d656469612f62616467652e737667"></a>
	<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://camo.githubusercontent.com/bca967b18143b8a5b2ffe78bd4a1a30f6bc21de83bd8336f748e96498af38b38/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d43432532304259253230342e302d6c69676874677265792e737667"></a>
	<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://camo.githubusercontent.com/33126b4770aa6f169b2a93e75678d52647f19972fa8d205e478049966e3b1a07/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646f63732d737461626c652d627269676874677265656e2e7376673f7374796c653d666c6174266c6f6e6743616368653d74727565"></a>
	<a href="https://github.com/allegroai/clearml"><img src="https://camo.githubusercontent.com/f60861e75a851f69a1fb8a5c671ef233147b7781a13dae226dcc2c32166654c0/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f636c6561726d6c2e737667"></a>
</p>

Language: English / [Chinese](./README_CN.md)

This is the _official_ repository for _**FEC**_.

Segmentation from point cloud data is essential in many applications ,such as remote sensing, mobile robots, or autonomous cars. However, the point clouds captured by the 3D range sensor are commonly sparse and unstructured, challenging efficient segmentation. A fast solution for point cloud instance segmentation with small computational demands is lacking. To this end, we propose a novel fast Euclidean clustering (FEC) algorithm which applies a point-wise scheme over the cluster-wise scheme used in existing works. The proposed method avoids traversing every point constantly in each nested loop, which is time and memory-consuming. Our approach is conceptually simple, easy to implement (40 lines in C++), and achieves two orders of magnitudes faster against the classical segmentation methods while producing high-quality results.

Code repository locate permenately at [here][3].

**THIS REPOSITORY IN UNDER DAILY UPDATING!**

## Table of Contents

## Background

## Maintainers

[@ YizhenLAO ][4]
[@IfeiHsueh][5]

## License

[MIT]()(LICENSE) © Yizhen LAO

[1]:	https://colab.research.google.com/github/bipinKrishnan/fastai_course/blob/master/bear_classifier.ipynb
[2]:	https://mybinder.org/v2/gh/bipinKrishnan/fastai_course/master
[3]:	https://github.com/YizhenLAO/FEC
[4]:	https://github.com/YizhenLAO
[5]:	https://github.com/IfeiHsueh


[image-1]:	https://colab.research.google.com/assets/colab-badge.svg
[image-2]:	https://mybinder.org/badge_logo.svg