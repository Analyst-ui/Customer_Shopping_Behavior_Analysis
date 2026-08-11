# Customer_Shopping_Behavior_Analysis


## Customer Shopping Behavior Analysis | SQL, Python & Power BI

An end-to-end Data Analytics project that analyzes customer shopping behavior to uncover purchasing patterns, customer segments, product performance, and revenue insights using Python, PostgreSQL, and Microsoft Power BI.


### Project Overview

This project focuses on analyzing customer shopping behavior using transactional data to understand spending habits, customer preferences, purchasing frequency, subscription behavior, and product performance. The workflow covers data cleaning in Python, business analysis in PostgreSQL, and interactive dashboard development in Microsoft Power BI to support strategic business decisions.


### Problem Statement

Retail Businesses collect vast amounts of customer transaction data, but raw data alone does not provide actionable insights.
The objective of this project is to answer key business questions such as:

Which customer segments generate the highest revenue?

Do subscribers spend more than non-subscribers?

Which products perform best?

How do discounts influence purchasing behavior?

Which age groups contribute the most revenue?

What factors influence customer loyalty?

The goal is to transform raw shopping data into business intelligence that supports marketing, customer retention, and sales optimization.


### Dataset

The project uses a retail customer shopping dataset containing 3,900 purchase records and 18 features. 

Key Features: - Customer demographics (Age, Gender, Location, Subscription Status) 

Purchase details (Item Purchased, Category, Purchase Amount, Season, Size, Color) 

Shopping behavior (Discount Applied, Promo Code Used, Previous Purchases, Frequency of 
Purchases, Review Rating, Shipping Type) 

Missing Data: 37 values in Review Rating column


### Tools & Technologies

Python(Pandas, NumPy, Matplotlib, Seaborn, SQLAlchemy)
PostgreSQL (SQL)
Microsoft Power BI


### Methods

1️⃣ Data Cleaning & Preparation (Python)

Imported and explored the dataset

Checked data quality and summary statistics

Handled missing values in the Review Rating column using median imputation by product category

Renamed columns using snake_case

Performed feature engineering by creating:

Age Groups

Purchase Frequency

Removed redundant columns

Loaded the cleaned dataset into PostgreSQL for further analysis.

2️⃣ SQL Business Analysis

Performed SQL queries to answer business questions, including:

Revenue by Gender

High-Spending Discount Users

Top-Rated Products

Shipping Type Comparison

Subscriber vs Non-Subscriber Analysis

Discount-Dependent Products

Customer Segmentation

Top Products by Category

Repeat Buyer Analysis

Revenue by Age Group

3️⃣ Dashboard Development (Power BI)

Created an interactive dashboard to visualize:

Revenue Performance

Customer Segmentation

Subscription Analysis

Product Performance

Discount Analysis

Purchase Trends

Shipping Preferences

Customer Demographics

Age Group Analysis

KPIs and Interactive Filters


### Key Insights

Customer Behavior

Non-subscribers generated a significant share of total revenue, indicating strong purchasing activity even without memberships.

Loyal customers contributed substantially more revenue than new customers.

Revenue Analysis

Certain age groups consistently contributed the highest revenue.

Customers choosing Express Shipping spent more per transaction than those using Standard Shipping.

Product Performance

A small number of products accounted for a large portion of total sales.

Top-rated products demonstrated strong customer satisfaction and sales potential.

Discounts

Discounts increased purchase volume but should be balanced against profitability.

Subscription Analysis

Repeat buyers were more likely to become subscribers, highlighting the value of customer retention strategies.


### Business Recommendations

1. Increase Customer Retention

Expand loyalty programs and personalized rewards for repeat buyers.

4. Improve Subscription Adoption

Offer exclusive discounts and benefits to encourage non-subscribers to join membership programs.

6. Focus on High-Performing Products

Increase inventory and marketing efforts for top-selling and top-rated products.

8. Optimize Discount Strategy

Use targeted discounts instead of broad promotions to maximize profitability.

10. Promote Express Shipping

Encourage premium shipping options through bundled offers or loyalty benefits.

12. Personalize Marketing Campaigns

Target high-revenue age groups with tailored recommendations and promotions.

14. Enhance Customer Segmentation
    
Develop personalized campaigns for New, Returning, and Loyal customers to improve engagement and retention. These recommendations align with the project's documented findings and suggested actions.


### How to Run This Project

Step 1

Clone this repository.

Step 2

Install Python dependencies.

pip install pandas numpy matplotlib seaborn sqlalchemy psycopg2

Step 3

Run the Python script to clean and prepare the dataset.

Step 4

Import the cleaned dataset into PostgreSQL.

Step 5

Execute the SQL queries provided in the project.

Step 6

Open the Power BI (.pbix) file.

Step 7

Refresh the data model.

Step 8

Interact with the dashboard using filters and slicers.


### Results & Conclusion

This project demonstrates a complete end-to-end data analytics workflow using Python, PostgreSQL, and Microsoft Power BI.

By combining data preprocessing, SQL-based business analysis, and interactive dashboard development, the project converts raw customer transaction data into actionable business insights.

The analysis enables businesses to:

Understand customer purchasing behavior

Improve customer retention

Optimize marketing strategies

Increase subscription adoption

Enhance product positioning

Support data-driven decision-making


### Future Work

Develop customer lifetime value (CLV) models.

Build machine learning models for purchase prediction.

Forecast future sales trends.

Create recommendation systems for personalized shopping.

Integrate real-time transactional databases.

Deploy dashboards to the Power BI Service with automated refresh.

Build customer churn prediction models.


### Author

Nimisha Tripathy | Aspiring Data Analyst


##### Skills

Python, SQL, Microsoft Power BI,Exploratory Data Analysis (EDA),Excel


### Contact

LinkedIn : (Add your LinkedIn profile URL)

Email : n.tripathy200@gmail.com
