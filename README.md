 Data Anonymization for Financial Data


📝 Project Overview
This project demonstrates data anonymization techniques on financial datasets to protect sensitive information while retaining analytical utility.  
It applies masking, generalization, and noise addition to real-world financial data, ensuring privacy compliance and safe analysis.  



📊 Dataset
- Sample dataset: `data/creditTest_sample.csv`  
- Sensitive columns: `cc_num`, `first`, `last`, `trans_num`, `amt`, latitude/longitude coordinates.  

 ⚠️ Note: Original sensitive datasets are not shared; only sample data is included for demonstration.


🛠 Features & Techniques


1️⃣ Data Cleaning & Preprocessing
- Remove duplicates  
- Handle missing values  
- Ensure correct numeric types  

2️⃣ Anonymization Techniques
- Masking: Hide sensitive columns like credit card numbers and names  
- Generalization:Convert numeric values into ranges (`amt`)  
- Noise Addition:Add random noise to continuous data (`lat`, `long`, etc.)  

3️⃣Privacy Metrics
- ✅ Reduction in unique values for sensitive columns  
- ✅ k-anonymity for generalized columns  
- ✅ Correlation analysis to ensure utility  

4️⃣ Visualization
- Histograms to compare original vs anonymized distributions
  
📂 Project Structure

data-anonymization-financial-data/
│
├── data/                  # Sample input dataset
│   └── creditTest_sample.csv
├── scripts/               # Python scripts
│   └── anonymize.py
├── results/               # Anonymized output
│   └── anonymized_credit_data.csv
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
