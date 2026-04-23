import pandas as pd
import numpy as np
import os

def load_data(file_path):
    """Loads the raw data file."""
    return pd.read_csv(file_path)

def apply_custom_cleaning(df):
    """Applies all business rules for data normalization and cleaning."""
    
    # 1. DROP UNNECESSARY COLUMNS
    # Removing Phone_Number as it is not needed for analysis
    if 'Phone_Number' in df.columns:
        df = df.drop(columns=['Phone_Number'])

    # 2. PRE-CLEAN: Standardize Names (Subscriptions and Countries)
    sub_map = {
        'Ent-1': 'enterprise', 'PRO': 'premium', 
        'basic': 'basic', 'Basic': 'basic', 'enterprise': 'enterprise'
    }
    if 'Subscription_Type' in df.columns:
        df['Subscription_Type'] = df['Subscription_Type'].str.strip().map(sub_map).fillna(df['Subscription_Type'])

    country_map = {
        'ARM': 'Armenia', 'Armenia': 'Armenia', 'US': 'USA', 
        'USA': 'USA', 'United States': 'USA', 'UK': 'UK', 'U.K.': 'UK'
    }
    if 'Country' in df.columns:
        df['Country'] = df['Country'].str.strip().map(country_map).fillna(df['Country'])

    # 3. REVENUE OUTLIERS & MISSING VALUES
    # Treat anything over 1000 as an error/outlier
    if 'Monthly_Revenue' in df.columns:
        df.loc[df['Monthly_Revenue'] > 1000, 'Monthly_Revenue'] = np.nan
        # Fill blanks with the average for that specific subscription type
        df['Monthly_Revenue'] = df['Monthly_Revenue'].fillna(
            df.groupby('Subscription_Type')['Monthly_Revenue'].transform('mean')
        )

    # 4. AGE OUTLIERS & MISSING VALUES
    if 'Customer_Age' in df.columns:
        # Neutralize impossible ages (-5, 250, etc.)
        df.loc[(df['Customer_Age'] < 1) | (df['Customer_Age'] > 100), 'Customer_Age'] = np.nan
        # Fill with rounded average of valid ages
        avg_age = round(df['Customer_Age'].dropna().mean())
        df['Customer_Age'] = df['Customer_Age'].fillna(avg_age)

    # 5. FORMATTING & BOOLEAN STANDARDIZATION
    if 'Join_Date' in df.columns:
        df['Join_Date'] = pd.to_datetime(df['Join_Date'], errors='coerce')
    
    logic_map = {
        'TRUE': 'Yes', '1': 'Yes', 'Yes': 'Yes', 'yes': 'Yes',
        'FALSE': 'No', '0': 'No', 'No': 'No', 'no': 'No'
    }
    if 'Discount_Applied' in df.columns:
        df['Discount_Applied'] = df['Discount_Applied'].astype(str).str.strip().map(logic_map).fillna('No')

    # 6. FINAL CLEANUP: Delete useless rows
    # Drop rows where both key identifiers are missing
    df = df.dropna(subset=['Subscription_Type', 'Monthly_Revenue'], how='all')

    return df

# --- BATCH PROCESSING EXECUTION ---
# This looks at every CSV in your folder and cleans them automatically
folder_path = './' 

print("🚀 Starting Data Cleaning Pipeline...")

files_processed = 0
for filename in os.listdir(folder_path):
    # Only process CSV files and ignore files we've already cleaned
    if filename.endswith(".csv") and not filename.startswith("cleaned_"):
        try:
            raw_df = load_data(filename)
            cleaned_df = apply_custom_cleaning(raw_df)
            
            output_name = f"cleaned_{filename}"
            cleaned_df.to_csv(output_name, index=False)
            
            print(f"✅ Successfully cleaned: {filename} -> Saved as: {output_name}")
            files_processed += 1
            
        except Exception as e:
            print(f"❌ Failed to process {filename}: {e}")

if files_processed == 0:
    print("⚠️ No new messy CSV files were found in the folder.")
else:
    print(f"✨ Pipeline Finished! Processed {files_processed} file(s).")