import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("linkdin_Job_data.csv")

# Drop unnecessary columns
df = df.drop(columns=["company_id", "Column1"], errors='ignore')

# Convert numeric columns safely
df["no_of_employ"] = df["no_of_employ"].astype(str).str.replace(",", "").str.extract("(\d+)").astype(float)
df["no_of_application"] = pd.to_numeric(df["no_of_application"], errors="coerce")
df["linkedin_followers"] = (
    df["linkedin_followers"].astype(str).str.replace(",", "").str.extract("(\d+)")[0].astype(float)
)

# Standardize `posted_day_ago`
def convert_posted_days(value):
    if pd.isna(value):
        return np.nan
    elif "hour" in str(value) or "minute" in str(value):
        return 0  # Assume within the same day
    elif "day" in str(value):
        return int(value.split()[0])  # Extract the number of days
    return np.nan

df["posted_day_ago"] = df["posted_day_ago"].apply(convert_posted_days)

# Split `full_time_remote`
df[["job_type", "seniority"]] = df["full_time_remote"].astype(str).str.split("·", expand=True)
df["job_type"] = df["job_type"].str.strip()
df["seniority"] = df["seniority"].str.strip()

# Handle missing values
df.fillna({
    "job": "Unknown", "location": "Unknown", "company_name": "Unknown", "work_type": "Unknown",
    "job_type": "Unknown", "seniority": "Unknown", "no_of_employ": df["no_of_employ"].median(),
    "no_of_application": df["no_of_application"].median(), "posted_day_ago": df["posted_day_ago"].median(),
    "linkedin_followers": df["linkedin_followers"].median()
}, inplace=True)

# Create new features
df["application_per_employee"] = df["no_of_application"] / df["no_of_employ"]
df["job_popularity_score"] = df["linkedin_followers"] * df["no_of_application"]

# Categorize hiring status based on applications received
def categorize_hiring_status(applications):
    return "High" if applications >= 100 else "Medium" if applications >= 50 else "Low"
df["hiring_status"] = df["no_of_application"].apply(categorize_hiring_status)

# Categorize `posted_day_ago`
def categorize_posted_days(days):
    return "Recent" if days <= 3 else "Moderate" if days <= 10 else "Old"
df["posting_age"] = df["posted_day_ago"].apply(categorize_posted_days)

# Convert Job Type to Categorical Numbers
job_type_mapping = {"Full-time": 1, "Part-time": 2, "Contract": 3, "Internship": 4, "Unknown": 0}
df["job_type_encoded"] = df["job_type"].map(job_type_mapping)

# Rearrange Columns
new_order = [
    "job_ID", "job", "company_name", "location", "work_type", "job_type", "job_type_encoded", 
    "seniority", "no_of_employ", "no_of_application", "application_per_employee", "linkedin_followers", 
    "job_popularity_score", "hiring_status", "posted_day_ago", "posting_age", "Hiring_person", "alumni", "hiring_person_link"
]
df = df[[col for col in new_order if col in df.columns]]  # Keep only existing columns

# Save the transformed dataset
df.to_csv("transformed_linkedin_job_data.csv", index=False)

print("Data transformation complete. File saved as transformed_linkedin_job_data.csv")
