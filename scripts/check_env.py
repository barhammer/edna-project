import sys
import numpy
import pandas
import torch
import umap
import hdbscan
from importlib.metadata import version

print("Python:", sys.version)
print("NumPy:", numpy.__version__)
print("Pandas:", pandas.__version__)
print("PyTorch:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
print("UMAP:", umap.__version__)
print("HDBSCAN:", version("hdbscan"))
