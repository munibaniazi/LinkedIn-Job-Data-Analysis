# **LinkedIn Job Data Analysis & Transformation**

## 📌 **Project Overview**
This project focuses on **cleaning, transforming, and analyzing** LinkedIn job posting data to extract meaningful insights. The dataset is processed to improve usability for analytics and predictive modeling.

## 🎯 **Objective**
- Perform **data cleaning** to remove inconsistencies.
- Implement **data transformation** to create new features.
- Extract **key insights** related to hiring trends and job popularity.
- Prepare the dataset for future **machine learning applications**.

## 📂 **Dataset Details**
- **File Name:** `linkedin_Job_data.csv`
- **Key Features:**
  - Job Title, Company, Location, Work Type
  - Number of Employees, Number of Applications
  - LinkedIn Followers, Posting Age, Hiring Status

## 🛠 **Tech Stack**
- **Python** (pandas, numpy)
- ** VS Code**
- **Git & GitHub**

## 🔍 **Data Cleaning & Transformation**
- **Removed unnecessary columns** (e.g., `company_id`, `Column1`).
- **Converted data types** to appropriate formats.
- **Handled missing values** (filled with median or placeholder values).
- **Standardized posting age** to numerical values.
- **Created new features** such as:
  - `application_per_employee` = `no_of_application` / `no_of_employ`
  - `job_popularity_score` = `linkedin_followers` * `no_of_application`
  - `hiring_status` categorized as **High, Medium, Low**

## 🖥 **Project Structure**
```

├── linkedin_Job_data.csv (Raw Data)
├── transformed_linkedin_job_data.csv (Processed Data)
├── linkedin.py (Main Script)
├── README.md (Project Documentation)
```

## 🚀 **How to Run the Project**
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/munibaniazi/LinkedIn-Job-Data-Analysis.git
   cd LinkedIn-Job-Data-Analysis
   ```
2. **Install Dependencies:**
   ```sh
   pip install pandas numpy
   ```
3. **Run the Script:**
   ```sh
   python linkedin.py
   ```

## 📊 **Key Insights & Findings**
- Jobs with **higher LinkedIn followers** receive more applications.
- **Older job postings** have lower application rates.
- Hiring demand varies based on **industry and job type**.


## 📌 **Future Enhancements**
- **Apply Machine Learning** to predict job popularity.
- **Develop a Dashboard** for interactive visual analysis.
- **Integrate Real-Time Data Updates** from LinkedIn.
