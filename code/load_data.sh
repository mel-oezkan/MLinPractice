#!/bin/bash

# create directory if not yet existing
mkdir -p data/raw/

# download the three csv files
echo "Dowloading Data"
python -m wget -o data/raw/data_analysis.csv https://myshare.uni-osnabrueck.de/f/3e5276caf72b46e7ace2/?dl=1
python -m wget -o data/raw/data_science.csv https://myshare.uni-osnabrueck.de/f/e620aff7719948d18a52/?dl=1
python -m wget -o data/raw/data_visualization.csv https://myshare.uni-osnabrueck.de/f/9ddaab064c68483e9bff/?dl=1

