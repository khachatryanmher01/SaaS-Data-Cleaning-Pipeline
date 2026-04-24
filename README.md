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
<pre>
SaaS_Data_Project/
│
│ ├── messy_customer_data.csv
│ └── cleaned_customer_data.csv
│ └── data_cleaner.py
└── README.md
</pre>
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

## 💼 Business Value & Impact

In a real-world SaaS environment, poor data quality leads to inaccurate financial reporting and failed marketing campaigns. This pipeline addresses those risks by providing:

* **Operational Efficiency:** Automates hours of manual data cleaning in Excel. What used to take a human half a day now takes a script 2 seconds.
* **Financial Accuracy:** By detecting and correcting revenue outliers (e.g., correcting $99,999 to the subscription average), the pipeline ensures that MRR (Monthly Recurring Revenue) and LTV (Lifetime Value) metrics are reliable for executive decision-making.
* **Data Integrity:** Standardizing country and subscription categories allows for accurate customer segmentation. This means marketing teams can target the right users in the right regions without "ghost" categories (like "USA" vs "US") skewing the results.
* **Scalability:** The pipeline is built to handle batch processing. As the business grows from 1,000 customers to 1,000,000, the same logic can be applied to process massive datasets instantly.

⭐ If you found this project useful, feel free to star the repository!
