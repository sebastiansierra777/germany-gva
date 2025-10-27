# Germany GVA Analysis: Industry & Energy GVA influence on GDP (PPP) per capita

Analysis of Germany's Gross Value Added (GVA) in Industry & Energy and GDP (PPP) per capita, data sourced from the OECD.

## 📋 Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Data Sources](#data-sources)
- [Requirements](#requirements)
- [Author](#author)

## 🎯 Overview

This project aims to detect the influence of GVA in Industry & Energy on the German Economy, in particular, in GDP (PPP) Per Capita for the year 2021

## 🚀 Installation

### Prerequisites

- [Anaconda](https://www.anaconda.com/products/distribution) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- 🔧 Git

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
germany_gva/
├── Data/
│   ├── raw/            # Original OECD datasets 
│   └── processed/      # Transformed OECD datasets
├── mlr.py              # Main analysis script
├── environment.yml     # Conda environment specification
├── requirements.txt    # Python package versions
├── .gitignore          # Files/folders excluded from version control
└── README.md           # Project documentation
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

This project follows a clean data pipeline structure. Your datasets should be organized like this:
```
germany_gva/
└── Data/
    ├── raw/            # Original OECD datasets (user-added)
    └── processed/      # Generated outputs from analysis
```

## 📥 Adding the Data

Please manually download the required datasets from the **OECD Regions & Cities Database**:
🔗 https://www.oecd.org/en/data/tools/oecd-regions-and-cities-atlas.html

You may follow this process as an example:

1. **For GDP per capita (PPP):**
   - Select **Choose Indicator → Economy → Gross Domestic Product per capita, in USD**
   - Select **Territorial Level: TL3**
   - Click on **latest year available** on the bottom right of the **map**
   - **Download Data**
   - Save all downloaded files into `Data/raw/`

2. **For GVA (by industry):**
   - Select **Choose Indicator → Economy → Gross Value Added by Industry -> select industry, including energy, and manufacturing**
   - Make sure **Territorial Level: TL3** is still selected
   - Click on **latest year available** on the bottom right of the **map**
   - **Download Data**
   - Save all downloaded files into `Data/raw/`

## ⚙️ Processed Data

During analysis, cleaned, merged, or transformed datasets may be exported to the `Data/processed/` folder

✅ This structure supports reproducibility, scalability, and a professional analytical workflow.

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