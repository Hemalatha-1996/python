# 🛒 Retail Order Data Analysis

An end-to-end data analytics project that extracts, cleans, analyzes, and visualizes retail sales data using **Python**, **SQL Server**, and **Streamlit**.

---

## 📌 Project Overview

| Detail | Info |
|---|---|
| **Domain** | Data Analytics |
| **Dataset** | Kaggle — Retail Orders |
| **Tools** | Python, SQL Server, Streamlit, Plotly |
| **Skills** | Kaggle API, Data Cleaning, SQL Queries, Dashboard |

---

## 🎯 Objectives

- Identify products and categories contributing most to revenue and profit
- Analyze Year-over-Year (YoY) and Month-over-Month (MoM) sales trends
- Highlight sub-categories with the highest profit margins
- Build an interactive Streamlit dashboard connected to SQL Server

---

## 🗂️ Project Structure

```
retail-order-analysis/
│
├── app.py                  # Streamlit dashboard
├── data_cleaning.py        # Data extraction and cleaning script
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| Data Source | Kaggle API |
| Data Cleaning | Python (Pandas) |
| Database | SQL Server |
| Dashboard | Streamlit |
| Charts | Plotly Express |
| DB Connector | PyODBC |



## 📊 Dashboard Features — 20 SQL Queries

| # | Query | Chart Type |
|---|---|---|
| Q1 | Top 10 Revenue Generating Products | Bar Chart |
| Q2 | Top 5 Cities by Profit Margin | Bar Chart |
| Q3 | Total Discount per Category | Bar Chart |
| Q4 | Avg Sale Price per Category | Bar Chart |
| Q5 | Region with Highest Avg Sale Price | Metric + Bar Chart |
| Q6 | Total Profit per Category | Bar Chart |
| Q7 | Top 3 Segments by Orders | Bar Chart |
| Q8 | Avg Discount % per Region | Bar Chart |
| Q9 | Category with Highest Total Profit | Metric Card |
| Q10 | Total Revenue per Year | Line Chart |
| Q11 | YoY Sales Growth per Category | Bar Chart |
| Q12 | Month with Highest Sales | Metric Card |
| Q13 | Top 5 Sub-Categories by Profit Margin | Bar Chart |
| Q14 | Products with Discount > 20% | Bar Chart / Info |
| Q15 | Rank Products by Revenue in Category | Table |
| Q16 | Segment-wise Profit Contribution % | Bar Chart |
| Q17 | Monthly MoM Revenue Change | Line Chart |
| Q18 | Region with Most Orders per Category | Grouped Bar |
| Q19 | Categories where Avg Profit > 100 | Bar Chart |
| Q20 | Bottom 5 Loss-Making Products | Bar Chart |

---

## 💡 Key Insights

- **Technology** is the most profitable category, contributing **37% of total profit**
- **TEC-CO-10004722** is the top revenue product at **$2,45,056**
- **October** is the peak sales month driven by year-end corporate spending
- **Furniture** showed a **-6.43% decline** in 2023 — needs strategic attention
- **Danbury & Goldsboro** have the highest profit margins at **29.82%**
- **5 products** are operating at a net loss and should be repriced or discontinued

---

## 📦 Requirements

```
streamlit
pandas
pyodbc
plotly
matplotlib
```

---

## 👤 Author

**HEMALATHA S**

---



This project is for educational purposes as part of a Data Analytics portfolio.
