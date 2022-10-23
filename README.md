
# FEC: Fast Euclidean Clustering for Point Cloud Segmentation

[![awesome][image-1]][1]
[![Open In Colab][image-2]][2]  
[![Binder][image-3]][3]

<p>
<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://camo.githubusercontent.com/bca967b18143b8a5b2ffe78bd4a1a30f6bc21de83bd8336f748e96498af38b38/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d43432532304259253230342e302d6c69676874677265792e737667"></a>
<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://camo.githubusercontent.com/33126b4770aa6f169b2a93e75678d52647f19972fa8d205e478049966e3b1a07/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646f63732d737461626c652d627269676874677265656e2e7376673f7374796c653d666c6174266c6f6e6743616368653d74727565"></a>
<a href="https://github.com/allegroai/clearml"><img src="https://camo.githubusercontent.com/f60861e75a851f69a1fb8a5c671ef233147b7781a13dae226dcc2c32166654c0/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f636c6561726d6c2e737667"></a>
</p>

This is the _official_ repository for _**FEC**_.

Segmentation from point cloud data is essential in many applications ,such as remote sensing, mobile robots, or autonomous cars. However, the point clouds captured by the 3D range sensor are commonly sparse and unstructured, challenging efficient segmentation. A fast solution for point cloud instance segmentation with small computational demands is lacking. To this end, we propose a novel fast Euclidean clustering (FEC) algorithm which applies a point-wise scheme over the cluster-wise scheme used in existing works. The proposed method avoids traversing every point constantly in each nested loop, which is time and memory-consuming. Our approach is conceptually simple, easy to implement (40 lines in C++), and achieves two orders of magnitudes faster against the classical segmentation methods while producing high-quality results.

This repository contains:

\1. 
\2. 

Standard Readme is designed for open source libraries. Although it’s [historically]()(#background) made for Node and npm projects, it also applies to libraries in other languages and package managers.


## Table of Contents

- [Background]()(#background)
- [Install]()(#install)
- [Usage]()(#usage)
	- [Generator]()(#generator)
- [Badge]()(#badge)
- [Example Readmes]()(#example-readmes)
- [Related Efforts]()(#related-efforts)
- [Maintainers]()(#maintainers)
- [Contributing]()(#contributing)
- [License]()(#license)

## Background

Standard Readme started with the issue originally posed by [@maxogden]()(https://github.com/maxogden) over at [feross/standard]()(https://github.com/feross/standard) in [this issue]()(https://github.com/feross/standard/issues/141), about whether or not a tool to standardize readmes would be useful. A lot of that discussion ended up in [zcei's standard-readme]()(https://github.com/zcei/standard-readme/issues/1) repository. While working on maintaining the [IPFS]()(https://github.com/ipfs) repositories, I needed a way to standardize Readmes across that organization. This specification started as a result of that.

> Your documentation is complete when someone can use your module without ever
having to look at its code. This is very important. This makes it possible for
you to separate your module's documented interface from its internal
implementation (guts). This is good because it means that you are free to
change the module's internals as long as the interface remains the same.

> Remember: the documentation, not the code, defines what a module does.

 Ken Williams, Perl Hackers(http://mathforum.org/ken/perlmodules.html#document)

Writing READMEs is way too hard, and keeping them maintained is difficult. By offloading this process - making writing easier, making editing easier, making it clear whether or not an edit is up to spec or not - you can spend less time worrying about whether or not your initial documentation is good, and spend more time writing and using code.

By having a standard, users can spend less time searching for the information they want. They can also build tools to gather search terms from descriptions, to automatically run example code, to check licensing, and so on.

The goals for this repository are:

1. A well defined **specification**. This can be found in the [Spec document]()(spec.md). It is a constant work in progress; please open issues to discuss changes.
2. **An example README**. This Readme is fully standard-readme compliant, and there are more examples in the `example-readmes` folder.
3. A **linter** that can be used to look at errors in a given Readme. Please refer to the [tracking issue]()(https://github.com/RichardLitt/standard-readme/issues/5).
4. A **generator** that can be used to quickly scaffold out new READMEs. See [generator-standard-readme]()(https://github.com/RichardLitt/generator-standard-readme).
5. A **compliant badge** for users. See [the badge]()(#badge).

## Install

This project uses [node]()(http://nodejs.org) and [npm]()(https://npmjs.com). Go check them out if you don't have them locally installed.

	`sh
$ npm install --global standard-readme-spec
	`

## Usage

This is only a documentation package. You can print out [spec.md]()(spec.md) to your console:

	`sh
$ standard-readme-spec
# Prints out the standard-readme spec
	`

### Generator

To use the generator, look at [generator-standard-readme]()(https://github.com/RichardLitt/generator-standard-readme). There is a global executable to run the generator in that package, aliased as `standard-readme`.

## Badge

If your README is compliant with Standard-Readme and you're on GitHub, it would be great if you could add the badge. This allows people to link back to this Spec, and helps adoption of the README. The badge is **not required**.

[![standard-readme compliant]()(https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

To add in Markdown format, use this code:

	`
[![standard-readme compliant]()(https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
	`

## Example Readmes

To see how the specification has been applied, see the [example-readmes]()(example-readmes/).

## Related Efforts

- [Art of Readme]()(https://github.com/noffle/art-of-readme) - 💌 Learn the art of writing quality READMEs.
- [open-source-template]()(https://github.com/davidbgk/open-source-template/) - A README template to encourage open-source contributions.

## Maintainers

[@ YizhenLAO ][33]
[@IfeiHsueh][34]

## Contributing

Feel free to dive in! [Open an issue]()(https://github.com/RichardLitt/standard-readme/issues/new) or submit PRs.

Standard Readme follows the [Contributor Covenant]()(http://contributor-covenant.org/version/1/3/0/) Code of Conduct.

### Contributors

This project exists thanks to all the people who contribute. 
\<a href="https://github.com/RichardLitt/standard-readme/graphs/contributors"\>\<img src="https://opencollective.com/standard-readme/contributors.svg?width=890&button=false" /\>\</a\>


## License

[MIT]()(LICENSE) © Yizhen LAO

[1]:	https://github.com/sindresorhus/awesome
[2]:	https://colab.research.google.com/github/bipinKrishnan/fastai_course/blob/master/bear_classifier.ipynb
[3]:	https://mybinder.org/v2/gh/bipinKrishnan/fastai_course/master
[33]:	https://github.com/YizhenLAO
[34]:	https://github.com/IfeiHsueh


[image-1]:	https://camo.githubusercontent.com/abb97269de2982c379cbc128bba93ba724d8822bfbe082737772bd4feb59cb54/68747470733a2f2f63646e2e7261776769742e636f6d2f73696e647265736f726875732f617765736f6d652f643733303566333864323966656437386661383536353265336136336531353464643865383832392f6d656469612f62616467652e737667
[image-2]:	https://colab.research.google.com/assets/colab-badge.svg
[image-3]:	https://mybinder.org/badge_logo.svg