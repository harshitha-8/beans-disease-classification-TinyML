# beans-disease-classification-TinyML
TinyML image classification for bean disease detection using Hugging Face dataset. Classifies healthy, angular leaf spot, and bean rust using MobileNetV2.

# Bean Disease Classification using Hugging Face Dataset

An image classification project for identifying diseases in bean plants using deep learning. This project uses the beans dataset from Hugging Face to classify three categories: healthy, angular leaf spot, and bean rust.

## Overview

This project demonstrates TinyML image classification using a publicly available dataset from Hugging Face. The trained model can identify plant diseases in bean leaves, making it useful for agricultural monitoring and early disease detection.

## Dataset

The project uses the [beans dataset](https://huggingface.co/datasets/beans) from Hugging Face, which contains images of bean leaves in three categories:

- Healthy: Normal, disease-free bean leaves
- Angular Leaf Spot: Leaves affected by angular leaf spot disease
- Bean Rust: Leaves affected by bean rust disease

The dataset includes separate folders for training, testing, and validation images.

## Features

- Image classification for plant disease detection
- Uses MobileNetV2 architecture optimized for edge deployment
- 96x96 input image size for efficient processing
- Three-class classification (healthy, angular_leaf_spot, bean_rust)

## Getting Started

### Prerequisites

- Python 3.7+
- Git
- Git LFS (Large File Storage)

### Installation

1. Clone this repository:
```
git clone https://github.com/yourusername/beans-disease-classification.git
cd beans-disease-classification
```

2. Install required packages:
```
pip install -r requirements.txt
```

3. Install Git LFS (if not already installed):
```
git lfs install
```

### Downloading the Dataset

Run the dataset download script:
```
python scripts/download_dataset.py
```

Or manually download using:
```
cd data
git lfs install
git clone https://huggingface.co/datasets/beans
```

After cloning, unzip the file and navigate to the data folder where you'll find three subdirectories:
- `train/` - Training images
- `test/` - Testing images
- `validation/` - Validation images (optional)

### Data Preparation

The dataset is organized as follows after extraction:
```
data/beans/data/
├── train/
│   ├── healthy/
│   ├── angular_leaf_spot/
│   └── bean_rust/
├── test/
│   ├── healthy/
│   ├── angular_leaf_spot/
│   └── bean_rust/
└── validation/
    ├── healthy/
    ├── angular_leaf_spot/
    └── bean_rust/
```

## Model Architecture

The project uses MobileNetV2 96x96 0.35 with the following configuration:

- Input size: 96x96 pixels
- Final layer: 16 neurons
- Dropout: 0.1
- Training epochs: 120
- Validation set size: 10%
- Learning rate: 0.0005

These parameters can be adjusted to optimize accuracy for different use cases.

## Usage

### Training the Model

1. Ensure the dataset is downloaded and extracted in the `data/` folder
2. Open the Jupyter notebook:
```
jupyter notebook notebooks/model_training.ipynb
```
3. Follow the steps in the notebook to train and evaluate the model

### Testing

After training, test the model on unseen images from the test set to evaluate performance.

## Project Workflow

1. Data Acquisition: Download beans dataset from Hugging Face
2. Data Preparation: Organize images into training and testing sets
3. Feature Generation: Extract features from images
4. Model Training: Train MobileNetV2 classifier
5. Model Testing: Evaluate on test set
6. Deployment: Export model for edge device deployment

## Results

The model classifies bean leaf images into three categories with optimized accuracy for both training and testing datasets. Performance metrics include:

- Training accuracy
- Testing accuracy
- Confusion matrix
- Per-class precision and recall

### Model Performance Visualizations

<table>
  <tr>
    <td align="center">
      <img src="results/result_1.png" alt="Training and Validation Accuracy" width="400"/><br/>
      <b>Training and Validation Accuracy</b>
    </td>
    <td align="center">
      <img src="results/result_2.png" alt="Training and Validation Loss" width="400"/><br/>
      <b>Training and Validation Loss</b>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="results/result_3.png" alt="Confusion Matrix" width="400"/><br/>
      <b>Confusion Matrix</b>
    </td>
    <td align="center">
      <img src="results/result_4.png" alt="Sample Predictions" width="400"/><br/>
      <b>Sample Predictions</b>
    </td>
  </tr>
</table>

For more detailed results and additional visualizations, see the [results](results/) directory.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Hugging Face for providing the beans dataset
- The machine learning community for open-source tools and resources

## References

- [Hugging Face Beans Dataset](https://huggingface.co/datasets/beans)
- [MobileNetV2 Paper](https://arxiv.org/abs/1801.04381)
