# Germany GVA Analysis

Analysis of Germany's Gross Value Added (GVA) and GDP (PPP) per capita data sourced from the OECD.

## 📋 Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Data Sources](#data-sources)
- [Requirements](#requirements)
- [Author](#author)

## 🎯 Overview

This project performs data analysis on Germany's economic indicators, specifically focusing on Gross Value Added (GVA) and GDP purchasing power parity (PPP) per capita. The analysis uses Python data science tools to explore trends, patterns, and insights in the German economy.

## 🚀 Installation

### Prerequisites

- [Anaconda](https://www.anaconda.com/products/distribution) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- Git

### Setup

1. **Clone the repository**
```bash
   git clone https://github.com/sebastiansierra777/germany-gva.git
   cd germany-gva
```

2. **Create the conda environment**
```bash
   conda env create -f environment.yml
```

3. **Activate the environment**
```bash
   conda activate germany_gva
```

Alternatively, if using pip:
```bash
pip install -r requirements.txt
```

## 📁 Project Structure
```
germany-gva/
├── mlr.py              # Main analysis script
├── environment.yml     # Conda environment specification
├── requirements.txt    # Python package requirements
├── .gitignore         # Git ignore rules
└── README.md          # Project documentation
```

## 💻 Usage

1. **Activate the environment**
```bash
   conda activate germany_gva
```

2. **Run the analysis**
```bash
   python mlr.py
```

   Or open `mlr.py` in PyCharm/Jupyter and run cells individually using `# %%` cell markers.

## 📊 Data Sources

- **OECD Data**: https://www.oecd.org/en/data/tools/oecd-regions-and-cities-atlas.html
  - Germany economic indicators
  - Gross Value Added (GVA)
  - GDP per capita (PPP)
  - For TL3 Regions

## 📦 Requirements

### Main Dependencies

- Python 3.13.9
- pandas 2.3.3
- numpy 2.3.3
- matplotlib 3.10.6
- seaborn 0.13.2
- scikit-learn 1.7.2
- geopandas 1.1.1
- statsmodels 0.14.5

See `requirements.txt` or `environment.yml` for complete package list.

## 👤 Author

**Sebastian Sierra**

- GitHub: [@sebastiansierra777](https://github.com/sebastiansierra777)

## 📝 Notes

This project uses Jupyter-style cell markers (`# %%`) in Python files for interactive development in PyCharm or VS Code.

---

*Last updated: October 2025*