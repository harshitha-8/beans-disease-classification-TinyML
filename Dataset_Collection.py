#!/usr/bin/env python3
"""
Download the beans dataset from Hugging Face
"""

import os
import subprocess
from pathlib import Path

def download_beans_dataset():
    """Download beans dataset using git lfs"""
    
    # Create data directory if it doesn't exist
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    
    # Change to data directory
    os.chdir(data_dir)
    
    print("Installing Git LFS...")
    subprocess.run(["git", "lfs", "install"], check=True)
    
    print("Cloning beans dataset from Hugging Face...")
    subprocess.run([
        "git", "clone", 
        "https://huggingface.co/datasets/beans"
    ], check=True)
    
    print("\nDataset downloaded successfully!")
    print("Please unzip the file in data/beans/ to access the images.")
    print("\nDataset structure:")
    print("data/beans/data/")
    print("  ├── train/")
    print("  ├── test/")
    print("  └── validation/")

if __name__ == "__main__":
    download_beans_dataset()
