# Advanced Digital Design - FPGA Optical Character Recognition Project
Optical character recognition (OCR) on Xilinx PYNQ-v2.

This is the repository for our ADD project. Our project aims to perform OCR on an FPGA -- specifically the Xilinx PYNQ-v2.

## Table of Contents
*to be determined*

## Timeline
- [x] Formal project proposal.
- [ ] Initial project implementation: Training an neural network on [MNIST dataset](http://yann.lecun.com/exdb/mnist/).
- [ ] Implement trained Binarized Neural Network (BNN) on PYNQ processing system (PS).
- [ ] Move (parts of) inference from PS to program logic (PL).
- [ ] Include additional character recognition (i.e. non-handwritten digits or re-train model to include alphabetic characters ).
- [ ] If remiaining time permits, include camera functionality for (near) real-time OCR.
  
## Relevant Information
### Links
Training BNNs for PYNQ: [link](https://github.com/Xilinx/BNN-PYNQ/tree/master/bnn/src/training)
Information on FINN overlay: [link](https://github.com/Xilinx/BNN-PYNQ/) (from above)

### Research
FINN paper: [link](https://arxiv.org/abs/1612.07119)
Training BNNs: [link](https://arxiv.org/abs/1602.02830)
