# SALVQ: Scene-Adaptive Lattice Vector Quantization
This is the official PyTorch implementation of our paper "Improving 3D Gaussian Splatting Compression by Scene-Adaptive Lattice Vector Quantization". [ArXiv](https://arxiv.org/pdf/2509.13482)

* SALVQ is lightweight, combines the computational efficiency of uniform scalar quantization (USQ) with the coding efficiency of vector quantization (VQ), and achieves a cost-effective balance between USQ and VQ.  

* SALVQ is **plug-and-play** — it can be easily integrated into existing architectures, provides consistent performance gains, and introduces only negligible computational overhead.

# Abstract
3D Gaussian Splatting (3DGS) is rapidly gaining popularity for its photorealistic rendering quality and real-time performance, but it generates massive amounts of data. Hence compressing 3DGS data is necessary for the cost effectiveness of 3DGS models. Recently, several anchor-based neural compression methods have been proposed, achieving good 3DGS compression performance. However, they all rely on uniform scalar quantization (USQ) due to its simplicity. A tantalizing question is whether more sophisticated quantizers can improve the current 3DGS compression methods with very little extra overhead and minimal change to the system. The answer is yes by replacing USQ with lattice vector quantization (LVQ). To better capture scene-specific characteristics, we optimize the lattice basis for each scene, improving LVQ's adaptability and R-D efficiency. This scene-adaptive LVQ (SALVQ) strikes a balance between the R-D efficiency of vector quantization and the low complexity of USQ. SALVQ can be seamlessly integrated into existing 3DGS compression architectures, enhancing their R-D performance with minimal modifications and computational overhead. Moreover, by scaling the lattice basis vectors, SALVQ can dynamically adjust lattice density, enabling a single model to accommodate multiple bit rate targets. This flexibility eliminates the need to train separate models for different compression levels, significantly reducing training time and memory consumption.

# Installation
Please refer to [HAC](https://github.com/YihangChen-ee/HAC) for installation instructions and required packages.

# Training
We evaluate our method on three commonly used datasets: MipNeRF360, Tanks&Temples, and Deep Blending. We use the same training script as [HAC](https://github.com/YihangChen-ee/HAC). You can run the training with:  
```
python train_script/run_shell_xxx.py
```

# LICENSE
Please follow the LICENSE of [3DGS](https://github.com/graphdeco-inria/gaussian-splatting)

# Acknowledgments
* We thank all authors from [3DGS](https://github.com/graphdeco-inria/gaussian-splatting) for presenting such an excellent work.
* We thank all authors from [Scaffold-GS](https://github.com/city-super/Scaffold-GS) for presenting such an excellent work.
* We thank all authors from [HAC](https://github.com/YihangChen-ee/HAC) for presenting such an excellent work.
# Citation
If you find our project is useful, please consider citing:
```bibtex
@article{xu2025improving,
  title={Improving 3D Gaussian Splatting Compression by Scene-Adaptive Lattice Vector Quantization},
  author={Xu, Hao and Wu, Xiaolin and Zhang, Xi},
  journal={arXiv preprint arXiv:2509.13482},
  year={2025}
}
```
