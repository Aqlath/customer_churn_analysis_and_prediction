# 📊 Customer Churn Analysis and Prediction

This project analyzes customer churn behavior in the telecom industry using SQL, Python, Machine Learning, Power BI, and Streamlit. The goal is to identify factors influencing customer attrition, generate business insights, and build a predictive model that helps companies proactively reduce customer churn.

---

## 📌 Introduction

Customer churn is one of the most significant challenges faced by telecom companies. Losing customers directly impacts revenue, profitability, and market share. Understanding why customers leave and identifying at-risk customers can help businesses implement effective retention strategies.

This project combines business intelligence, data analytics, and machine learning techniques to analyze customer behavior and predict churn outcomes.

---

## 📂 Background

The primary objectives of this project are:

* Understand customer churn behavior
* Identify key factors influencing churn
* Perform SQL-based business analysis
* Conduct Exploratory Data Analysis (EDA)
* Build a Machine Learning model for churn prediction
* Develop an interactive Power BI dashboard
* Deploy predictions using Streamlit

The project uses a telecom customer dataset containing demographic information, service details, billing information, and customer churn status.

---

## 🛠 Tools Used

* **PostgreSQL** – Business analysis and SQL querying
* **Python** – Data cleaning, EDA, and Machine Learning
* **Pandas** – Data manipulation and preprocessing
* **NumPy** – Numerical operations
* **Matplotlib** – Data visualization
* **Seaborn** – Statistical visualization
* **Scikit-Learn** – Machine Learning model development
* **Power BI** – Dashboard creation and reporting
* **Streamlit** – Web application deployment
* **Jupyter Notebook** – Development environment

---

## 📊 The Analysis

### 🔹 1. Customer Churn Distribution

The initial analysis focused on understanding the overall churn rate within the telecom customer base.

* Identified the Count of customers who churned.
* Compared retained and churned customers.
* Established a baseline understanding of customer retention.

![Customer Churn Distribution](assets/churn_dist.png)

---

### 🔹 2. Contract Type vs Churn

Contract type was found to be one of the strongest indicators of churn behavior.

* Month-to-month customers showed significantly higher churn.
* One-year and two-year contracts had much lower churn rates.
* Long-term contracts contribute to improved customer retention.

![Contract Type Analysis](assets/contract_type.png)

---

### 🔹 3. Internet Service Analysis

Different internet services were analyzed to identify service-specific churn trends.

* Fiber optic customers exhibited higher churn rates.
* DSL customers showed comparatively better retention.
* Service quality and pricing may contribute to churn behavior.

![Internet Service Analysis](assets/internet_service.png)

---

### 🔹 4. Payment Method Analysis

Customer payment preferences were examined to understand their relationship with churn.

* Electronic check users had the highest churn rates.
* Customers using automatic payment methods showed better retention.
* Payment convenience appears to influence customer loyalty.

![Payment analysis](assets/payment_method.png)

---

### 🔹 5. Customer Tenure Analysis

Customer tenure was analyzed to understand retention patterns over time.

* New customers were more likely to churn.
* Long-term customers demonstrated higher loyalty.
* Customer engagement strategies are particularly important during early stages.

![Tenure Analysis](assets/tenure.png)

---

### 🔹 6. Monthly Charges Analysis

Billing information was evaluated to understand pricing-related churn behavior.

* Customers with higher monthly charges showed increased churn probability.
* Expensive plans may require additional value-added services.
* Pricing strategy plays an important role in retention.

![Monthly charge](assets/monthly_charge.png)

---

### 🔹 7. Correlation Analysis

A correlation analysis was conducted on numerical variables.

* TotalCharges showed a strong relationship with customer tenure.
* Long-term customers contributed higher lifetime value.
* The heatmap helped identify relationships among key variables.

![Correlation Analysis](assets/relation.png)

---

## 🤖 Machine Learning Model

Two machine learning algorithms were tested for churn prediction.

### Models Evaluated

| Model                    | Accuracy |
| ------------------------ | -------- |
| Logistic Regression      | 81%      |
| Decision Tree Classifier | 79%      |

### Model Selection

* Logistic Regression achieved the highest performance.
* The model was selected as the final predictive solution.
* The trained model was saved using Joblib for deployment.

<!-- INSERT MODEL PERFORMANCE VISUALIZATION HERE -->

---

## 📊 Power BI Dashboard

An interactive Power BI dashboard was developed to visualize churn patterns and business KPIs.

### Dashboard Features

* KPI Cards
* Interactive Slicers
* Navigation Buttons
* Dynamic Filtering
* Cross Filtering

### Dashboard KPIs

* Total Customers
* Churn Rate
* Churned Customers
* Retained Customers
* Total Revenue

![Dashboard overview](assets/dashboard.png)

---

### Dashboard Insights

The dashboard enables business users to:

* Monitor churn trends
* Analyze customer segments
* Evaluate contract performance
* Understand payment method behavior
* Track key business metrics

![Insight1](assets/insight1.png)
![Insight2](assets/insight2.png)

---

## 🌐 Streamlit Application

A Streamlit web application was developed to provide real-time churn predictions.

### Features

* Real-time churn prediction
* Interactive user interface
* Churn probability display
* Business recommendations
* Easy customer data input

![Model Homepage](assets/streamlit_home.png)

---

### Prediction Output

Users can enter customer information and instantly receive:

* Churn prediction result
* Churn probability score
* Business recommendations

![Model output](assets/streamlit_output.png)

---

## 🧠 What I Learned

* Performed end-to-end data analytics workflows
* Improved SQL querying and business analysis skills
* Gained hands-on experience in data cleaning and preprocessing
* Built machine learning models using Scikit-Learn
* Developed interactive Power BI dashboards
* Deployed machine learning solutions using Streamlit
* Learned how to translate data insights into business recommendations

---

## ✅ Conclusion

This project successfully demonstrates how SQL, Python, Machine Learning, Power BI, and Streamlit can be combined to create a complete customer churn analysis solution.

The analysis identified key churn drivers such as contract type, internet service, payment methods, customer tenure, and monthly charges. The machine learning model achieved strong predictive performance, while the Power BI dashboard and Streamlit application provided user-friendly interfaces for business decision-making.

---

## 🚀 Future Improvements

* Hyperparameter tuning
* Advanced machine learning models
* Deep learning approaches
* Cloud deployment
* Customer segmentation using clustering
* Real-time prediction pipelines

---

## 👤 Author

**Mohammed Aqlath A**

B.Tech Student | Data Science Enthusiastic

LinkedIn:
[www.linkedin.com/in/mohammed-aqlath-a-26baa3248](http://www.linkedin.com/in/mohammed-aqlath-a-26baa3248)
