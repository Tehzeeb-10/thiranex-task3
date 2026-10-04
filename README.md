# Exploratory Data Analysis (EDA) Using Python

## 📌 Project Overview

This project was completed as **Task 3** of my **Data Science Internship at Thiranex**.

The project focuses on performing **Exploratory Data Analysis (EDA)** on a customer shopping dataset to understand customer demographics, purchasing patterns, product preferences, and factors associated with purchase amount.

## 🎯 Objectives

- Use statistical summaries and visualizations to explore the dataset.
- Identify correlations, patterns, and key factors associated with purchase amount.
- Analyze customer demographics and purchasing behavior.
- Present the findings and insights in a structured and easy-to-understand format.

## 📊 Dataset

- **Records:** 2,004
- **Features:** 11
- **Main Variable Analyzed:** Purchase Amount
- **Missing Values:** 0

### Features

- CustomerID
- Gender
- Age
- Items Purchased
- Category
- Purchase Amount
- Shipping Type
- Profession
- Subscription Status
- Season
- Country

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Microsoft Excel

## 🔍 EDA Performed

The following analyses were performed:

- Dataset shape and structure analysis
- Missing value analysis
- Statistical summary
- Purchase amount distribution
- Item type analysis
- Category analysis
- Seasonal purchase analysis
- Subscription status analysis
- Gender-wise analysis
- Shipping type analysis
- Profession-wise analysis
- Country-wise analysis
- Age distribution
- Age vs Purchase Amount analysis
- Correlation analysis
- Boxplot analysis

## 📈 Visualizations

A total of **16 EDA visualizations** were created and combined into a single **4×4 dashboard**.

The visualizations help identify patterns and differences in customer purchasing behavior.

### EDA Dashboard

![EDA Dashboard](EDA_All_Graphs_4x4.png)

## 💡 Key Findings

- The average purchase amount was **52.58**.
- **Sandals** had the highest average purchase amount among item types at **57.81**.
- **Scarf** had the lowest average purchase amount among item types at **49.32**.
- **Fall** had the highest average purchase amount among seasons at **53.05**.
- **Footwear** had the highest average purchase amount among categories at **53.22**.
- Customers with a **subscription** had a higher average purchase amount (**54.27**) compared with non-subscribers (**46.70**).
- The correlation between **Age and Purchase Amount** was **−0.0028**, indicating almost no linear relationship.

## 📌 Conclusion

The EDA provided insights into customer demographics and purchasing behavior. Subscription status showed a noticeable difference in average purchase amount, while seasonal, gender, shipping, and age-related differences were comparatively small.

The analysis helped identify patterns in the dataset without assuming that any single variable directly determines purchase amount.

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

- Data exploration using Python
- Data manipulation using Pandas
- Statistical analysis
- Data visualization
- Correlation analysis
- Identifying patterns and trends
- Extracting insights from datasets
- Presenting analytical findings in a structured format

## 📁 Project Files

```text
Thiranex-Task3/
│
├── eda_analysis1.py
├── EDA_All_Graphs_4x4.png
├── Internship Report - Task 3.pdf
└── README.md
