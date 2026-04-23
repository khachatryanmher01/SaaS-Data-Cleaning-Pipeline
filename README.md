🧹 Automated Customer Data Cleaning Pipeline (Python)

A robust Python-based data cleaning pipeline designed to process messy SaaS customer datasets and transform them into clean, structured, and analysis-ready data.

This project simulates real-world data preprocessing by applying business rules, handling inconsistencies, and automating batch data cleaning across multiple files.

📌 Key Highlights
✅ Automated batch processing of multiple CSV files
✅ Handles missing values and outliers
✅ Applies business logic for normalization
✅ Standardizes inconsistent categorical data
✅ Cleans and formats dates & boolean fields
✅ Outputs clean datasets ready for analytics or SQL
📂 Project Structure
SaaS_Data_Project/
│
├── messy_customer_data.csv        # Raw dataset (input)
├── cleaned_customer_data.csv      # Clean dataset (output)
├── data_cleaner.py                # Main pipeline script
└── README.md
⚙️ How It Works

The pipeline scans the project folder and automatically processes all .csv files that are not already cleaned.

🔄 Workflow
Load raw dataset
Apply cleaning rules
Save cleaned version with prefix: cleaned_
Repeat for all CSV files in the directory
🧠 Data Cleaning Logic (Business Rules)
1. Column Cleanup
Removes unnecessary fields like Phone_Number
2. Data Standardization
Normalizes Subscription_Type values:
PRO, Ent-1, Basic → standardized categories
Standardizes Country names:
US, United States → USA
ARM → Armenia
3. Revenue Handling
Detects outliers (> 1000) and treats them as missing
Fills missing values using:
Mean revenue per subscription type
4. Age Cleaning
Removes invalid ages (<1 or >100)
Replaces missing values with:
Average customer age
5. Formatting Fixes
Converts Join_Date to proper datetime format
Standardizes boolean values:
TRUE, 1, yes → Yes
FALSE, 0, no → No
6. Final Data Validation
Drops rows where critical fields are missing:
Subscription_Type
Monthly_Revenue
▶️ Usage
1. Install dependencies
pip install pandas numpy
2. Run the pipeline
python data_cleaner.py
3. Output

Cleaned files will be saved automatically:

cleaned_<original_filename>.csv

📊 Example
Input:

messy_customer_data.csv

Output:

cleaned_messy_customer_data.csv
