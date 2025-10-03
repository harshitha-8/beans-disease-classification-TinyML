#!/usr/bin/env python3
"""
Prepare and organize the beans dataset for training
"""

import os
import shutil
from pathlib import Path
from collections import Counter

def count_images(directory):
    """Count images in each class"""
    classes = {}
    for class_dir in Path(directory).iterdir():
        if class_dir.is_dir():
            count = len(list(class_dir.glob("*.jpg"))) + len(list(class_dir.glob("*.png")))
            classes[class_dir.name] = count
    return classes

def prepare_dataset():
    """Analyze and prepare the dataset"""
    
    data_path = Path("data/beans/data")
    
    if not data_path.exists():
        print("Error: Dataset not found. Please run download_dataset.py first.")
        return
    
    print("Bean Disease Dataset Summary")
    print("=" * 50)
    
    # Analyze training set
    train_path = data_path / "train"
    if train_path.exists():
        print("\nTraining Set:")
        train_counts = count_images(train_path)
        for class_name, count in train_counts.items():
            print(f"  {class_name}: {count} images")
        print(f"  Total: {sum(train_counts.values())} images")
    
    # Analyze test set
    test_path = data_path / "test"
    if test_path.exists():
        print("\nTest Set:")
        test_counts = count_images(test_path)
        for class_name, count in test_counts.items():
            print(f"  {class_name}: {count} images")
        print(f"  Total: {sum(test_counts.values())} images")
    
    # Analyze validation set
    val_path = data_path / "validation"
    if val_path.exists():
        print("\nValidation Set:")
        val_counts = count_images(val_path)
        for class_name, count in val_counts.items():
            print(f"  {class_name}: {count} images")
        print(f"  Total: {sum(val_counts.values())} images")
    
    print("\n" + "=" * 50)
    print("Dataset preparation complete!")
    print("\nClasses detected:")
    all_classes = set()
    for path in [train_path, test_path, val_path]:
        if path.exists():
            all_classes.update([d.name for d in path.iterdir() if d.is_dir()])
    for cls in sorted(all_classes):
        print(f"  - {cls}")

if __name__ == "__main__":
    prepare_dataset()
