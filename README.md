# 🧮 Psychometric Item Pipeline & Optimization – AWS · Python · Bees Algorithm

## 🎯 Overview  

This project focused on building an **end-to-end data pipeline and analytical workflow** for psychometric item analysis and optimization.  
The main objective was to process raw assessment data stored in **AWS**, clean and score responses, generate **exploratory statistics and psychometric indicators**, and use an **optimization algorithm (Bees Algorithm)** to create item versions that maximize explained variance.  

The project integrates **data engineering, statistical analysis, and algorithmic optimization**, providing a scalable foundation for psychometric evaluation and test versioning.  

---

## ⚙️ Project Workflow  

### **1️⃣ Data Extraction Pipeline (AWS)**
- Built a **data pipeline** to query and extract assessment data stored in an **AWS S3 bucket**.  
- Established connection credentials and query logic for scheduled data retrieval.  
- Automated file ingestion and transformation into a standardized format for analysis.  

🧰 *Tools:* Python (boto3, pandas) · AWS S3 · SQLAlchemy  

---

### **2️⃣ Data Cleaning & Preprocessing**
- Performed a **deep cleaning process** to handle missing responses, invalid records, and inconsistent IDs.  
- Applied normalization of item responses and scoring scales for comparability.  
- Generated clean, structured datasets ready for psychometric computation.  

🧰 *Tools:* Python (pandas, numpy) · Excel (validation templates)  

---

### **3️⃣ Dataset Scoring & Statistical Exploration**
- Implemented scoring functions in **Python** to calculate total and subscale scores per participant.  
- Conducted **exploratory data analysis (EDA)** to identify distributional characteristics, outliers, and response patterns.  
- Computed **item-level descriptive statistics** (mean, SD, skewness, kurtosis) for quality control.  

🧰 *Tools:* Python (pandas, scipy, matplotlib)  

---

### **4️⃣ Psychometric Indicators**
- Calculated **item difficulty** and **discrimination indices**, evaluating item performance across the dataset.  
- Grouped participants by performance levels (low, medium, high) to support **item response validation**.  
- Provided interpretable metrics to support future test calibration.  

🧠 *Key Concept:* Item difficulty and discrimination indices help identify the precision and validity of assessment instruments.  

🧰 *Tools:* Python · numpy · scipy.stats  

---

### **5️⃣ Test Versioning & Optimization (Bees Algorithm)**
- Designed and implemented an **optimization routine** using the **Bees Algorithm** to generate test versions with different item counts (24 and 48 items).  
- Objective: **maximize explained variance** while maintaining internal consistency and balanced item representation.  
- Evaluated convergence criteria and reproducibility of optimized test forms.  

🧠 *Algorithm Insight:* The Bees Algorithm mimics foraging behavior to explore solution spaces efficiently, ideal for multi-objective psychometric optimization.  

🧰 *Tools:* Python (custom Bees Algorithm implementation) · matplotlib  

---

## 📊 Results & Impact  

- Built a **reusable, automated psychometric analysis pipeline** integrated with AWS data sources.  
- Generated **clean, validated datasets** and item performance metrics for stakeholders.  
- Produced **optimized test versions (24 & 48 items)** with improved variance explanation and reliability.  
- Enabled future integration of automated test assembly processes using AI-driven optimization.  

---

## 🧰 Tech Stack  

| Category | Tools & Technologies |
|-----------|---------------------|
| Data Engineering | Python (boto3, pandas) · AWS S3 · SQLAlchemy |
| Data Cleaning | Pandas · Numpy · Excel Templates |
| Psychometric Analysis | Python (scipy.stats, matplotlib) |
| Optimization | Bees Algorithm (custom implementation) |
| Reporting | Power BI · Python Visualizations |

---

## 📁 Folder Structure  

```markdown
psychometric_item_pipeline/
│
├── 📘 README.md                         # Project documentation
│
├── 📂 notebooks/
│   ├── 01_data_extraction_aws.ipynb     # Pipeline connection and queries to AWS
│   ├── 02_data_cleaning.ipynb           # Data preprocessing and validation
│   ├── 03_scoring_eda.ipynb             # Scoring logic and exploratory statistics
│   ├── 04_item_analysis.ipynb           # Difficulty & discrimination indices
│   ├── 05_bees_algorithm_optimization.ipynb # Optimization routine for item selection
│
├── 📂 src/
│   ├── aws_pipeline.py                  # AWS data extraction scripts
│   ├── cleaning_utils.py                # Data cleaning helper functions
│   ├── scoring_functions.py             # Item scoring and metrics
│   ├── bees_algorithm.py                # Bees Algorithm optimization logic
│   ├── item_analysis.py                 # Item difficulty/discrimination calculations
│
├── 📂 data/
│   ├── raw_data/                        # Extracted data from AWS
│   ├── cleaned_data.csv                 # Cleaned dataset
│   ├── item_metrics.csv                 # Item-level indicators
│   └── optimized_versions.csv           # Optimized 24/48-item versions
│
├── 📂 results/
│   ├── bees_convergence_plot.png        # Optimization convergence visualization
│   ├── item_difficulty_distribution.png # Histogram of item difficulties
│   ├── group_performance_summary.pdf    # Group-level performance report
│
└── 📂 docs/
    ├── bees_algorithm_explained.md      # Technical explanation of algorithm
    ├── psychometric_formulas.md         # Difficulty/discrimination equations
    └── lessons_learned.md
