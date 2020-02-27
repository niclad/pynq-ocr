# Advanced Digital Design - FPGA Optical Character Recognition Project
Optical character recognition (OCR) on Xilinx PYNQ-v2.

This is the repository for our ADD project. Our project aims to perform OCR on an FPGA -- specifically the Xilinx PYNQ-v2.

## Table of Contents
*to be determined*

## Timeline (2020)
- [x] Formal project proposal.
- [ ] Feb. 26: Initial project implementation: Training an neural network on [MNIST dataset](http://yann.lecun.com/exdb/mnist/).
- [ ] Implement trained Binarized Neural Network (BNN) on PYNQ processing system (PS).
- [ ] Mar. 18: Move (parts of) inference from PS to program logic (PL).
- [ ] Include additional character recognition (i.e. non-handwritten digits or re-train model to include alphabetic characters ).
- [ ] Apr. 22: If remiaining time permits, include camera functionality for (near) real-time OCR.
- [ ] Apr. 22: Final project report.
  
## Relevant Information
### Links
1. Training BNNs for PYNQ: [link](https://github.com/Xilinx/BNN-PYNQ/tree/master/bnn/src/training)
2. Information on FINN overlay: [link](https://github.com/Xilinx/BNN-PYNQ/) (from above)

### Research
1. FINN paper: [link](https://arxiv.org/abs/1612.07119)
2. Training BNNs: [link](https://arxiv.org/abs/1602.02830)