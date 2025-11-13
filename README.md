# Lung Cancer Detection Project

This repository contains a lung cancer detection project with organized code, data, and documentation.

## Directory Structure

```
├── src/                          # Source code
│   ├── notebooks/               # Jupyter notebooks
│   │   └── Cancer_Detection.ipynb
│   ├── scripts/                 # Python scripts
│   │   ├── cell_magic_wand.py
│   │   ├── Configuration_Creation.py
│   │   ├── DataSet_Creation.py
│   │   └── utils.py
│   └── utils/                   # Utility functions
│
├── data/                        # Data files
│   ├── raw/                     # Raw dataset files
│   │   ├── heart.csv
│   │   ├── list3_2.csv
│   │   ├── LIDC-XML-only.zip
│   │   ├── TCIA_LIDC-IDRI_20200921.tcia
│   │   ├── lidc-idri nodule counts (6-23-2015).xlsx
│   │   └── tcia-diagnosis-data-2012-04-20.xls
│   ├── processed/               # Processed datasets
│   │   └── preprocessed_data/
│   └── metadata/                # Metadata files
│       ├── LIDC_IDRI_MetaData.csv
│       └── metadata.csv
│
├── models/                      # Model files
│   ├── trained/                 # Trained model files
│   └── weights/                 # Model weights
│       └── model_weights/
│
├── results/                     # Results and outputs
│   └── plots/                   # Generated plots and visualizations
│       └── histplots/
│
├── docs/                        # Documentation
│   ├── presentations/           # PowerPoint presentations
│   │   ├── REVIEW PPT- 2.pptx
│   │   ├── disease prediction.pptx
│   │   └── Final_PPT.pptx
│   └── reports/                 # Written reports and documents
│       ├── Sem1FinalReview.docx
│       ├── review2.docx
│       ├── projectreviewsem1.txt
│       ├── B14 FINAL REPORT.docx
│       ├── project_viva.doc
│       └── Guide.pdf
│
└── archive/                     # Archived files (HTML exports, etc.)
    ├── Cancer_Detection.html
    └── Cancer_Detection_v3.html
```

## Getting Started

1. **Notebooks**: Start with `src/notebooks/Cancer_Detection.ipynb` for the main analysis
2. **Data**: Raw data is in `data/raw/`, processed data in `data/processed/`
3. **Scripts**: Utility scripts are in `src/scripts/`
4. **Models**: Trained models and weights are in `models/`
5. **Results**: Generated plots and results are in `results/`

## File Descriptions

- **Cancer_Detection.ipynb**: Main Jupyter notebook for lung cancer detection analysis
- **LIDC-IDRI dataset**: Medical imaging dataset for lung cancer research
- **Configuration_Creation.py**: Script for creating model configurations
- **DataSet_Creation.py**: Script for dataset preprocessing
- **utils.py**: Utility functions for data processing

## Notes

- This project uses the LIDC-IDRI dataset for lung cancer detection research
- Model weights and preprocessed data are preserved in their respective directories
- Documentation includes project reports, presentations, and guides