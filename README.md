# Overview
The [Energy-Based Flow Classifier (EFC)](https://arxiv.org/pdf/1910.07266.pdf) is a new approach to Network Intrusion Detection Systems. Unlike previous trials of integrating Machine Learning with NIDS, EFC is capable of identifying new classes of attacks different from the ones used during the model's training phase, and classifying them in real-time. This repository aims to integrate Secure Multi-Party Computation into the algorithm in order to address privacy concerns related to data processing. To achieve this goal, we use the MP-SPDZ framework, an implementation of the SPDZ protocol, created by Damgård et al.

This repository extends the original [EFC repository](https://github.com/EnergyBasedFlowClassifier/EFC-package?tab=readme-ov-file) with the integration of the [MP-SPDZ framework](https://github.com/data61/MP-SPDZ).

Recent research in the field of privacy-preserving computation has been focusing on the integration of ML with MPC. One of the most important challenges related to this topic is the performance of MPC algorithms. This theme is vital because of the computational overhead associated with integrating MPC techniques.

# Requirements
Note that MP-SPDZ requires either a Linux distribution originally released 2014 or later (glibc 2.17) or macOS High Sierra or later as well as Python 3 and basic command-line utilities.

# Installation
Follow the MP-SPDZ framework installation instructions available at [MP-SPDZ GitHub Repository](https://github.com/data61/MP-SPDZ). Place this repo inside of Programs/Source and then run run.sh from inside the repository's folder.
